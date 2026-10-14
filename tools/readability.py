"""Repair downloaded Markdown without re-importing or deleting any article.

python3 tools/readability.py --fix   # current posts and hand-written sources
python3 tools/readability.py         # fail when a formatting repair remains
"""
import argparse
import difflib
import json
import html
import re
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from readability_fixes import apply_fixes

ROOT = Path(__file__).resolve().parent.parent
OVERRIDES = ROOT / 'tools' / 'readability_overrides.json'


def formula_mathml(url):
    if not url.startswith('/images/') or not url.endswith('.svg'):
        return None
    path = ROOT / 'static' / url.lstrip('/')
    if not path.exists():
        return None
    svg = ET.fromstring(path.read_text())
    source = next((el for el in svg.iter() if el.get('data-mml-node') == 'math'), None)
    if source is None:
        return None

    def convert(el):
        kind = el.get('data-mml-node')
        if not kind:
            return ''.join(convert(child) for child in el)
        if kind in ('mi', 'mn', 'mo', 'mtext'):
            glyphs = ''.join(chr(int(x.get('data-c'), 16))
                             for x in el.iter() if x.get('data-c'))
            texts = ''.join(''.join(x.itertext()) for x in el.iter()
                            if x.tag.rsplit('}', 1)[-1] == 'text')
            value = glyphs or texts
            if not value:
                raise ValueError('Missing formula glyph: ' + str(path))
            return '<' + kind + '>' + html.escape(value) + '</' + kind + '>'
        if kind == 'mspace':
            return '<mspace width="0.22em"/>'
        kind = {'TeXAtom': 'mrow', 'mstyle': 'mrow'}.get(kind, kind)
        if kind not in ('math', 'mrow', 'mfrac', 'msub', 'msup', 'msubsup', 'mover', 'msqrt'):
            raise ValueError('Unsupported formula node: ' + kind)
        inner = ''.join(convert(child) for child in el)
        if kind == 'math':
            return '<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">' + inner + '</math>'
        return '<' + kind + '>' + inner + '</' + kind + '>'

    output = convert(source)
    # Every original mathematical glyph is retained, in the same order.
    expected = ''.join(chr(int(x.get('data-c'), 16)) for x in source.iter() if x.get('data-c'))
    actual = ''.join(ET.fromstring(output).itertext())
    if expected and expected != actual:
        raise ValueError('Formula glyph sequence changed: ' + str(path))
    return output


def signature(text):
    text = unicodedata.normalize('NFKC', text)
    return re.sub(r'[^\w]', '', text).lower()


def table_row(cells):
    return '| ' + ' | '.join(c.strip().replace('\n', '<br>') for c in cells) + ' |'


def repair_tables(body):
    """The downloader preserved row starts as '|', cell ends as ' |'."""
    lines = body.splitlines()
    starts = [i for i, line in enumerate(lines) if re.fullmatch(r'\|\s*', line)]
    spans = []
    for pos, start in enumerate(starts):
        limit = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        # A complete Markdown row is another boundary, not a cell.
        for i in range(start + 1, limit):
            if lines[i].startswith('|') and not re.fullmatch(r'\|\s*', lines[i]):
                limit = i
                break
        ends = [i for i in range(start + 1, limit)
                if re.match(r'^[ \t]+\|', lines[i])]
        if not ends:
            spans.append((start, start + 1, []))
            continue
        chunk = '\n'.join(lines[start:ends[-1] + 1])
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', chunk)[1:-1]]
        spans.append((start, ends[-1] + 1, cells))
    # Merge contiguous rows; narrative between tables stays outside the table.
    groups = []
    for start, end, cells in spans:
        if groups and not '\n'.join(lines[groups[-1][1]:start]).strip():
            groups[-1][1] = end
            if any(cells):
                groups[-1][2].append(cells)
        else:
            groups.append([start, end, [cells] if any(cells) else []])
    for group in groups:
        start, end, rows = group
        # Preserve a complete HTML-converted header directly before split rows.
        previous = start - 1
        while previous >= 0 and not lines[previous].strip():
            previous -= 1
        if previous >= 0 and re.fullmatch(r'\|.+\|', lines[previous]):
            before = lines[previous - 1] if previous else ''
            if not before.startswith('|'):
                header = re.split(r'(?<!\\)\|', lines[previous])[1:-1]
                if rows and len(header) == len(rows[0]):
                    rows.insert(0, [c.strip() for c in header])
                    group[0] = previous
    for start, end, rows in reversed(groups):
        rows = [r for r in rows if any(r)]
        # Layout-only containers become ordinary paragraphs, never empty tables.
        if len(rows) < 2 or max(map(len, rows), default=0) == 1:
            replacement = '\n\n'.join(c for row in rows for c in row if c)
        elif len({len(row) for row in rows}) == 1:
            replacement = '\n'.join([table_row(rows[0]),
                table_row(['---'] * len(rows[0]))] + [table_row(r) for r in rows[1:]])
        else:
            raise ValueError('Ambiguous table columns: ' + repr(rows)[:250])
        lines[start:end] = replacement.splitlines() + ['']
    body = '\n'.join(lines)
    # Complete rows lacking a separator came from HTML layout tables too.
    def complete_table(m):
        rows = m.group(0).strip().splitlines()
        if any(re.fullmatch(r'\|[\s:|\-]+\|', r) for r in rows):
            return m.group(0)
        cells = [re.split(r'(?<!\\)\|', r.strip())[1:-1] for r in rows]
        if len(rows) == 1 or all(len(c) == 1 for c in cells):
            return '\n\n'.join(c.strip() for row in cells for c in row) + '\n'
        if len({len(c) for c in cells}) != 1:
            raise ValueError('Uneven inline table')
        return '\n'.join([rows[0], table_row(['---'] * len(cells[0]))] + rows[1:]) + '\n'
    return re.sub(r'(?m)(?:^\|[^\n]+\|[ \t]*\n?)+', complete_table, body)


def _normalize_once(body, title='', overrides=(), filename=''):
    # Empty downloaded list items must never swallow a fenced code block.
    body = re.sub(r'(?m)^(?:[-+][ \t]+)+(?=```|~~~)', '', body)
    body = re.sub(r'(?m)^[-+][ \t]*\n\s*\n(?=```|~~~|[-+][ \t])', '', body)
    body = apply_fixes(body, filename)
    for old, new in overrides:
        if old in body:
            body = body.replace(old, new)
    body = body.replace('\u200b', '').replace('\u200c', '').replace('\ufeff', '')
    body = re.sub(r'!\[[^\]]*\]\((/images/[^\s)]+\.svg)\)',
                  lambda m: formula_mathml(m[1]) or m[0], body)
    # The downloader put inline formula images in separate paragraphs. Restore
    # short variables to the surrounding sentence, keeping real equations apart.
    def inline_variable(m):
        value = ''.join(ET.fromstring(m[0]).itertext())
        if len(value) <= 14 and not re.search(r'[=≈<>≤≥∼→]', value):
            return m[0].replace('display="block"', 'display="inline"')
        return m[0]
    body = re.sub(r'<math\b[^>]*>.*?</math>', inline_variable, body)
    for _ in range(6):
        body = re.sub(r'([^\n。！？：:])\n\s*\n[ \t]*(<math [^>]*display="inline"[^>]*>.*?</math>)',
                      lambda m: m[1] + (' ' if m[1] in '-+*' else '') + m[2], body)
        body = re.sub(r'(<math [^>]*display="inline"[^>]*>.*?</math>)\n\s*\n[ \t]*(?=[，。、；：）)\u4e00-\u9fff])', r'\1', body)
    body = re.sub(r'(<math [^>]*display="block"[^>]*>.*?</math>)(?=[\u4e00-\u9fff])', r'\1\n\n', body)
    body = re.sub(r'([\u4e00-\u9fff])\n[ \t]*(?=[，。、；：])', r'\1', body)
    body = re.sub(r'(</strong>)\n\s*\n[ \t]*(?=[，。：；])', r'\1', body)
    body = re.sub(r'(?m)^([-+] )?•\s*', '- ', body)
    body = re.sub(r'(?m)^。$', '', body)
    body = re.sub(r'(?m)^\d{2}\s*/\s*[A-Z][A-Z0-9 ≠±µ/ -]+$', '', body)
    body = re.sub(r'(?m)^(#{2,3})\s+[◆◤]\s*', r'\1 ', body)
    body = re.sub(r'(?m)^(#{2,3} \d{2})(?=[\u4e00-\u9fff])', r'\1 ', body)
    # Metadata accidentally published as a fenced YAML block is not article text.
    body = re.sub(r'\A\s*```[^\n]*\n(?=title:).*?\n```\s*', '', body, flags=re.S)
    body = repair_tables(body)
    body = re.sub(r'(?m)^[ \t]*\|[ \t]*$', '', body)
    # Without a blank line Goldmark treats a following image as another row.
    body = re.sub(r'(?m)(^\|[^\n]+\|[ \t]*\n)(?=\S)(?!\|)', r'\1\n', body)
    # Missing reference definitions came with the download. Keep the named
    # attribution readable; do not invent a URL for a missing source target.
    defined = set(re.findall(r'(?m)^\[(\d+)\]:', body))
    body = re.sub(r'\[([^\]\n]+)\]\[(\d+)\]',
                  lambda m: m[0] if m[2] in defined else m[1], body)
    lines = body.splitlines()
    clean = []
    in_code = False
    for line in lines:
        if re.match(r'^\s*(```|~~~)', line):
            in_code = not in_code
        if in_code:
            clean.append(line)
            continue
        if re.fullmatch(r'#{1,6}\s*', line):
            continue
        if re.fullmatch(r'\s*\*{1,3}\s*', line):
            # Repair formatting only. Content is kept on its original line.
            continue
        m = re.match(r'^#{1,6}\s+(.+)$', line)
        if m:
            text = m[1].strip()
            # Long prose was wrapped in h4 by the download converter.
            if len(text) > 65 and re.search(r'[。；！]', text):
                line = text
        clean.append(line)
    body = '\n'.join(clean)
    # An orphan bullet/quote marker belongs to the following paragraph.
    body = re.sub(r'(?m)^([ \t]*[-+]|\d+[.)])\s*\n\s*\n(?=\S)(?!```|~~~)', r'\1 ', body)
    body = re.sub(r'(?m)^(?:[-+][ \t]+){2,}', '- ', body)
    body = re.sub(r'(?m)^>\s*\n\s*\n(?=\S)', '> ', body)
    # Keep emphasis inside one paragraph. Unmatched imported ** becomes text.
    paragraphs = re.split(r'(\n\s*\n)', body)
    fenced = False
    for i in range(0, len(paragraphs), 2):
        p = paragraphs[i]
        if '```' in p or '~~~' in p:
            fenced = not fenced if (p.count('```') + p.count('~~~')) % 2 else fenced
            continue
        if fenced:
            continue
        if len(re.findall(r'(?<!\\)\*\*', p)) % 2:
            p = re.sub(r'(?<!\\)\*\*', '', p)
        # Goldmark cannot emphasize punctuation at a CJK/Latin word boundary.
        p = re.sub(r'\*\*([^*\n]+)\*\*', r'<strong>\1</strong>', p)
        paragraphs[i] = p
    body = ''.join(paragraphs)
    # Remove duplicated title, including title split across lines by a cover layout.
    blocks = re.split(r'\n\s*\n', body)
    title_sig = signature(title)
    body = re.sub(r'(?m)^#{2,6}\s+(.+)$',
                  lambda m: '' if signature(re.sub(r'<[^>]+>', '', m[1])) == title_sig else m[0], body)
    blocks = re.split(r'\n\s*\n', body)
    for i, block in enumerate(blocks):
        if i > 18:
            break
        plain = re.sub(r'<[^>]+>|^[#*\s]+', '', block)
        sig = signature(plain)
        if not sig or block.lstrip().startswith(('!', '|', '```')):
            continue
        ratio = difflib.SequenceMatcher(None, sig, title_sig).ratio()
        if sig == title_sig or (title_sig and title_sig in sig and len(sig)<len(title_sig)*1.5) or (len(sig) >= 12 and ratio >= .82) or (
                len(sig) >= 12 and len(sig) / max(1, len(title_sig)) >= .45 and sig in title_sig):
            blocks[i] = ''
        elif i < 8 and len(plain) < 60 and title_sig.startswith(sig) and len(sig) >= 6:
            # Stacked title: test following short blocks as a single title.
            end = i
            combined = sig
            while end + 1 < min(len(blocks), i + 5) and len(blocks[end+1]) < 90:
                end += 1
                combined += signature(re.sub(r'<[^>]+>|^[#*\s]+', '', blocks[end]))
                if difflib.SequenceMatcher(None, combined, title_sig).ratio() >= .86:
                    for j in range(i, end + 1):
                        blocks[j] = ''
                    break
    # Imported opening labels are presentation metadata, not the lead paragraph.
    for i, block in enumerate(blocks[:16]):
        plain = re.sub(r'<[^>]+>|[#*]', '', block).strip()
        if not plain or block.lstrip().startswith('!'):
            continue
        is_label = (re.match(r'^(?:关键词|关键字|标签|阅读约|阅读时间|工程手记|工程拆解|工程科普|产品路线判断|全文三句话|先记住三个判断|读完这篇，你会带走三件事|核心观点|三个数先看完)', plain)
                    or re.fullmatch(r'[A-Z0-9][A-Z0-9 /·×—–.,:−-]{3,}', plain)
                    or (len(plain) < 65 and re.search(r'[·｜]', plain) and not re.search(r'[。！？]', plain)))
        if is_label:
            blocks[i] = ''
        else:
            # Stop at the first real lead; internal section labels have meaning.
            break
    body = '\n\n'.join(b for b in blocks if b.strip())
    # Promote first-level sections to h2, keeping only genuine subheadings at h3.
    levels = [len(m[1]) for m in re.finditer(r'(?m)^(#{2,6})\s+\S', body)]
    if levels:
        base = min(levels)
        body = re.sub(r'(?m)^(#{2,6})(\s+)',
            lambda m: '#' * min(3, len(m[1]) - base + 2) + m[2], body)
    # Some reviewed repairs match canonical emphasis; apply them after the
    # structural pass too, so raw archive re-imports get the same result.
    body = apply_fixes(body, filename)
    body = re.sub(r'\n{3,}', '\n\n', body).strip() + '\n'
    return body


def normalize(body, title='', overrides=(), filename=''):
    # Inline repairs can expose punctuation boundaries after emphasis is fixed.
    # Reach a stable representation now, rather than requiring repeated imports.
    for _ in range(5):
        updated = _normalize_once(body, title, overrides, filename)
        if updated == body:
            return updated
        body = updated
    raise ValueError('Formatting did not converge: ' + filename)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fix', action='store_true')
    args = parser.parse_args()
    overrides = json.loads(OVERRIDES.read_text()) if OVERRIDES.exists() else {}
    changed, checked = [], 0
    for folder in ('content/posts', 'posts_extra'):
        for path in sorted((ROOT / folder).glob('*.md')):
            if path.name == '_index.md':
                continue
            raw = path.read_bytes()
            text = raw.decode('utf-8').replace('\r\n', '\n')
            fm = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
            if not fm:
                raise ValueError('Missing frontmatter: ' + str(path))
            title = re.search(r'^title: "(.*)"$', fm[1], re.M)
            title = title[1] if title else ''
            body = text[fm.end():].lstrip('\n')
            new_body = normalize(body, title, overrides.get(path.name, []), path.name)
            # Every original illustration must survive, in its original order.
            images = lambda s: [m[0] for m in re.finditer(r'!\[[^\]]*\]\(([^\n]+?)\)', s)
                                if not formula_mathml(m[1])]
            if images(body) != images(new_body):
                raise ValueError('Illustration inventory changed: ' + path.name)
            checked += 1
            if body != new_body:
                changed.append(str(path.relative_to(ROOT)))
                if args.fix:
                    output = text[:fm.end()] + '\n' + new_body
                    newline = '\r\n' if b'\r\n' in raw else '\n'
                    path.write_bytes(output.replace('\n', newline).encode())
    print(json.dumps({'checked': checked, 'changed': len(changed), 'files': changed}, ensure_ascii=False, indent=2))
    return 0 if args.fix or not changed else 1


if __name__ == '__main__':
    raise SystemExit(main())
