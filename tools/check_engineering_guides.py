#!/usr/bin/env python3
"""Check this content batch, rendered links, method coverage and search entries."""
import json,re,sys
from pathlib import Path
from urllib.parse import urlsplit,unquote
import yaml
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
build=Path(sys.argv[1]);items=[];seen=set()
expected={f'D{i:02}' for i in range(1,13)}-{"D10"}
expected|={f'R{i:02}' for i in range(1,13)}
expected|={f'E{i:02}' for i in [1,2,3,6,9,10,11,12]}
expected|={"P0-02","TOOLS"}
for path in sorted((ROOT/'content/wiki/engineering').glob('*.md')):
 if path.name=='_index.md':continue
 _,raw,body=path.read_text().split('---',2);meta=yaml.safe_load(raw)
 assert meta['engineering_entry'] and meta['layout']=='engineering-single',path
 pid=meta['plan_id'];assert pid not in seen,pid;seen.add(pid)
 assert len(body.strip())>=500,(path,'too little substantive text')
 assert not re.search(r'(?m)^# ',body),path
 assert not any(x in body for x in ['[[','0-System/','3-wiki/','雅可比','等面积映射','太岳','南岭']),path
 target=build/'wiki/engineering'/path.stem/'index.html';assert target.is_file(),path
 soup=BeautifulSoup(target.read_text(),'html.parser');assert len(soup.select('h1'))==1,path
 content=soup.select_one('.content');assert content and content.get_text(strip=True),path
 assert not content.select('merror'),path
 for table in content.select('table'):
  rows=[len(tr.find_all(['th','td'],recursive=False)) for tr in table.select('tr')]
  assert len(set(rows))==1,(path,rows)
 for a in soup.select('main a[href]'):
  u=urlsplit(a['href'])
  if u.scheme or u.netloc:continue
  dest=(build/unquote(u.path).lstrip('/')) if u.path else target
  assert dest.is_file() or (dest/'index.html').is_file(),(path,a['href'])
  if u.fragment:
   f=dest if dest.is_file() else dest/'index.html'
   assert BeautifulSoup(f.read_text(),'html.parser').find(id=unquote(u.fragment)),(path,a['href'])
 for math in content.select('math'):
  assert math.get_text(strip=True),path
  for n in math.find_all(['mfrac','msub','msup','mover','msubsup']):
   assert len(n.find_all(recursive=False))==(3 if n.name=='msubsup' else 2),(path,n.name)
 items.append({'id':pid,'slug':path.stem,'body_chars':len(body.strip()),'math':len(content.select('math')),'sources':len(content.select('a[href^="https://"]'))})
assert seen==expected,(seen^expected)
index=BeautifulSoup((build/'wiki/engineering/index.html').read_text(),'html.parser')
assert len(index.select('.guide-card'))==33
assert len(index.select('.guide-path'))==3
home=BeautifulSoup((build/'index.html').read_text(),'html.parser')
data=json.loads(home.select_one('#portal-search-data').string)
assert len([x for x in data if x['kind']=='guide'])==33
assert home.select('a[href="/wiki/engineering/"]')
for item in items:assert any(x['url']==f"/wiki/engineering/{item['slug']}/" for x in data)
for slug in ['kin52','as5047p']:
 s=BeautifulSoup((build/'models'/slug/'index.html').read_text(),'html.parser')
 assert s.select('.guide-backlinks a'),slug
for slug in ['robot-joint','servo-motor','water-meter','pneumatic-cylinder']:
 s=BeautifulSoup((build/'applications'/slug/'index.html').read_text(),'html.parser')
 assert s.select('.guide-backlinks a'),slug
assert not (build/'wiki/engineering/bidirectional-error/index.html').exists()
assert not (build/'wiki/engineering/encoder-cable-return-path/index.html').exists()
print(json.dumps({'guides':len(items),'expected_exclusions':['D10','E04'],'items':items},ensure_ascii=False,indent=2))
