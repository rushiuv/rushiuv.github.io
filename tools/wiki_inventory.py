"""Rank existing model/company tags by associated post count; never retag posts."""
from collections import Counter
from pathlib import Path
import argparse,json,re

def inventory(root):
    counts={k:Counter() for k in ('models','companies')}
    posts=sorted((root/'content/posts').glob('*.md'))
    for p in posts:
        text=p.read_text(encoding='utf-8-sig')
        if not text.startswith('---'):raise ValueError(f'No front matter: {p}')
        fm=text.split('---',2)[1]
        for kind,counter in counts.items():
            m=re.search(r'^'+kind+r':\s*(\[.*\])\s*$',fm,re.M)
            if m:counter.update(set(json.loads(m.group(1))))
            elif re.search(r'^'+kind+r':',fm,re.M):raise ValueError(f'Unsupported tag format: {p}:{kind}')
    rows=[dict(kind=k,name=n,count=v) for k,c in counts.items() for n,v in c.items()]
    rows.sort(key=lambda x:(-x['count'],x['name'].casefold()))
    return dict(post_count=len(posts),metric='associated post count, once per post',tie_break='name.casefold() ascending',terms=rows)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=20);ap.add_argument('--output',type=Path);args=ap.parse_args()
    data=inventory(Path(__file__).resolve().parent.parent);data['terms']=data['terms'][:args.limit]
    out=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(out,encoding='utf-8')
    else:print(out)
