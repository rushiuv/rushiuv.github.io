"""Validate the built article pages, not only Markdown syntax.

Usage: python3.11 tools/check_readability.py /absolute/path/to/hugo/output
Requires beautifulsoup4, used only for this check, not for building the site.
"""
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


def check(root):
    counts = collections.Counter()
    issues = []
    for page in sorted((root / 'posts').glob('*/index.html')):
        soup = BeautifulSoup(page.read_text(), 'html.parser')
        content = soup.select_one('.content')
        if content is None:
            continue
        counts['articles'] += 1
        name = page.parent.name
        def issue(kind, detail):
            issues.append({'post': name, 'kind': kind, 'detail': detail})
        title = signature(soup.select_one('h1').get_text())
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
    return {'counts': dict(counts), 'issues': issues, 'passed': not issues}


if __name__ == '__main__':
    result = check(Path(sys.argv[1]).resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['passed'] else 1)
