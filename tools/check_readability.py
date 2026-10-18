"""Validate the built article pages, not only Markdown syntax.

Usage: python3.11 tools/check_readability.py /absolute/path/to/hugo/output
       python3.11 tools/check_readability.py /absolute/path/to/hugo/output --posts-only
Requires beautifulsoup4, used only for this check, not for building the site.
The default covers posts, basics and applications. --posts-only keeps the old
article diagnostic scope available; neither mode performs browser layout tests.
"""
import argparse
import collections
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit
from bs4 import BeautifulSoup


def signature(s):
    return re.sub(r'[^\w]', '', unicodedata.normalize('NFKC', s)).lower()


def stylesheet_paths(root):
    """Collect global stylesheets for a conservative declaration scan, not CSS cascade resolution."""
    paths = {root / 'css/site.css'}
    if (root / 'css/refined.css').is_file():
        paths.add(root / 'css/refined.css')
    home = root / 'index.html'
    if home.is_file():
        soup = BeautifulSoup(home.read_text(encoding='utf-8'), 'html.parser')
        for link in soup.select('link[rel~="stylesheet"][href]'):
            url = urlsplit(link['href'])
            if not url.netloc and url.path.startswith('/'):
                paths.add(root / unquote(url.path).lstrip('/'))
    return sorted(paths)


def check(root, posts_only=False):
    counts = collections.Counter()
    issues = []
    # Guard the regression that DOM arity alone cannot detect: ordinary block
    # layout on <math> destroys its inferred row, stacking tokens vertically.
    css_files = stylesheet_paths(root)
    for css_path in css_files:
        if not css_path.is_file():
            issues.append({'kind': 'missing_stylesheet', 'detail': str(css_path.relative_to(root))})
            continue
        css = re.sub(r'/\*.*?\*/', '', css_path.read_text(encoding='utf-8'), flags=re.S)
        for selector, declarations in re.findall(r'([^{}]+)\{([^{}]*)\}', css):
            if re.search(r'\bmath\b', selector):
                for value in re.findall(r'(?:^|;)\s*display\s*:\s*([^;]+)', declarations):
                    if 'math' not in value.lower().replace('!important', '').split():
                        issues.append({'kind': 'math_css_layout', 'detail':
                                       str(css_path.relative_to(root)) + ': ' + selector.strip() + ': display:' + value})
    families = [('posts', 'articles')]
    if not posts_only:
        families.extend([('wiki/basics', 'basics'), ('applications', 'applications')])
    pages = [(page, family) for folder, family in families
             for page in sorted((root / folder).glob('*/index.html'))]
    for page, family in pages:
        soup = BeautifulSoup(page.read_text(encoding='utf-8'), 'html.parser')
        content = soup.select_one('.content')
        if content is None:
            continue
        counts[family] += 1
        name = page.parent.name
        def issue(kind, detail):
            location = {'post': name} if family == 'articles' else {'page': str(page.relative_to(root))}
            issues.append({**location, 'kind': kind, 'detail': detail})
        headings = soup.find_all('h1')
        if len(headings) != 1 or not headings[0].get_text(strip=True):
            issue('single_h1', len(headings))
        title = signature(headings[0].get_text()) if headings else ''
        if soup.select('.post-head .chips'):
            issue('opening_keywords', 'Article header still has tag chips')
        for heading in content.select('h1,h2,h3,h4,h5,h6'):
            text = heading.get_text(' ', strip=True)
            if not text:
                issue('empty_heading', '')
            elif heading.name not in ('h2', 'h3'):
                issue('heading_level', heading.name + ': ' + text[:80])
            elif signature(text) == title:
                issue('duplicate_title', text)
        for table in content.find_all('table'):
            counts['tables'] += 1
            rows = [r.find_all(['td', 'th'], recursive=False) for r in table.find_all('tr')]
            if len({len(row) for row in rows}) != 1:
                issue('table_columns', [len(row) for row in rows])
            for i, row in enumerate(rows):
                for j, cell in enumerate(row):
                    if not cell.get_text(strip=True) and not cell.find(['math','img']):
                        issue('empty_table_cell', [i, j])
        for math in content.find_all('math'):
            counts['formulas'] += 1
            if not math.get_text(strip=True):
                issue('empty_formula', '')
            for node in math.find_all(['mfrac','msub','msup','mover','msubsup']):
                expected = 3 if node.name == 'msubsup' else 2
                children = node.find_all(recursive=False)
                if len(children) != expected:
                    issue('math_structure', node.name + ': ' + str(len(children)))
        for image in content.find_all('img'):
            counts['illustrations'] += 1
            target = urlsplit(image.get('src', ''))
            src = unquote(target.path)
            if not target.netloc and src.startswith('/') and not (root / src.lstrip('/')).is_file():
                issue('missing_image', src)
        for link in soup.find_all('a', href=True):
            target = urlsplit(link['href'])
            if not target.netloc and target.path.startswith('/'):
                dest = root / unquote(target.path).lstrip('/')
                if not dest.exists():
                    issue('broken_internal_link', link['href'])
        # TeX in MathML annotation is accessible source, not visible raw markup.
        for math in content.find_all('math'):
            math.decompose()
        for code in content.find_all(['pre','code']):
            code.decompose()
        for block in content.find_all(['p','li','h2','h3']):
            text = block.get_text(' ', strip=True)
            if '**' in text or re.search(r'\\(?:frac|theta|omega|Delta|text|mathrm)|\$\$', text):
                issue('raw_markdown_or_tex', text[:160])
            if re.search(r'\[[^\]]+\]\[\d+\]', text):
                issue('unresolved_reference_link', text[:160])
            if text and re.fullmatch(r'[|，。、：；()\s]+', text):
                issue('punctuation_only', text)
    return {'scope': 'posts-only' if posts_only else 'posts, basics, applications',
            'stylesheets': [str(path.relative_to(root)) for path in css_files],
            'counts': dict(counts), 'issues': issues, 'passed': not issues,
            'boundary': 'Static built-HTML checks, not browser, accessibility or traffic validation. '
                        'Run check_site_release.py as well: absent pages cannot be discovered by this scan.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('build_dir', type=Path)
    parser.add_argument('--posts-only', action='store_true', help='Keep the previous article-only diagnostic scope')
    args = parser.parse_args()
    result = check(args.build_dir.resolve(), posts_only=args.posts_only)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['passed'] else 1)
