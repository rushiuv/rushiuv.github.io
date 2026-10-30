#!/usr/bin/env python3
"""Check every expanded model's rendered parameters, links and retained identity.

Usage: python3 tools/check_model_details.py BUILD BASELINE_SOURCE
Checks presentation and coverage, not the truth of datasheet values.
"""
import collections
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
build = Path(sys.argv[1]).resolve()
baseline = Path(sys.argv[2]).resolve()
errors, records, paragraphs = [], [], collections.defaultdict(list)
all_paths = sorted((ROOT / 'content/models').glob('*/_index.md'))
paths = []
for path in all_paths:
    meta0 = yaml.safe_load(path.read_text().split('---', 2)[1]) or {}
    if meta0.get('wiki_type') == 'model_redirect':
        continue
    paths.append(path)
if not paths:
    errors.append('Expected at least one non-redirect model page')
for path in paths:
    slug = path.parent.name
    text = path.read_text()
    meta = yaml.safe_load(text.split('---', 2)[1])
    old = baseline / path.relative_to(ROOT)
    if old.exists():
        old_meta = yaml.safe_load(old.read_text().split('---', 2)[1])
        for key in ('title', 'linkTitle', 'aliases', 'search_aliases', 'series_parent', 'related_companies', 'product_image'):
            if meta.get(key) != old_meta.get(key):
                errors.append(f'{slug}: changed identity field {key}')
    if not meta.get('lastmod'):
        errors.append(f'{slug}: missing revision date')
    page = build / 'models' / slug / 'index.html'
    if not page.exists():
        errors.append(f'{slug}: missing generated page')
        continue
    soup = BeautifulSoup(page.read_text(), 'html.parser')
    content = soup.select_one('.wiki-content')
    if content is None:
        errors.append(f'{slug}: missing rendered model body')
        continue
    if len(soup.select('h1')) != 1:
        errors.append(f'{slug}: expected one H1')
    # CDN email protection mistakes compact current@voltage notation for email.
    if re.search(r'@\d', content.get_text()):
        errors.append(f'{slug}: compact @condition can be hidden by CDN email protection')
    tables = content.select('table')
    rows = 0
    for table in tables:
        for row in table.select('tr'):
            cells = row.find_all(['th', 'td'], recursive=False)
            if len(cells) != 2 or any(not c.get_text(strip=True) for c in cells):
                errors.append(f'{slug}: non-two-column or empty parameter row')
            if row.find('td'):
                rows += 1
    if not rows:
        errors.append(f'{slug}: no visible parameter table')
    for a in content.select('a[href]'):
        u = urlsplit(a['href'])
        if u.scheme or u.netloc or not u.path.startswith('/'):
            continue
        target = build / unquote(u.path).lstrip('/')
        if not target.is_file() and not (target / 'index.html').is_file():
            errors.append(f"{slug}: missing internal target {a['href']}")
    for p in content.select('p'):
        t = re.sub(r'\s+', '', p.get_text())
        if len(t) >= 90:
            paragraphs[t].append(slug)
    records.append({'slug': slug, 'title': meta['title'], 'parameter_rows': rows,
                    'sections': len(content.select('h2')), 'body_characters': len(content.get_text()),
                    'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
duplicates = [slugs for slugs in paragraphs.values() if len(set(slugs)) > 1]
report = {'scope': f'{len(paths)} non-redirect model pages; rendered tables and local body links only',
          'errors': errors, 'duplicate_long_paragraph_groups': duplicates,
          'pages': records, 'total_parameter_rows': sum(r['parameter_rows'] for r in records)}
print(json.dumps(report, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
