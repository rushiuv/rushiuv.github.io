#!/usr/bin/env python3
"""One-time faithful import of six publicly accessible WeChat articles.

Source HTML was fetched from the original WeChat pages, staged as sanitized
js_content on main, and is read back to source here. Never fabricate article text.
"""
from pathlib import Path
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from io import BytesIO
from datetime import datetime
from zoneinfo import ZoneInfo
import re, json, hashlib, html, time
import requests
import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify
from PIL import Image

REPO="rushiuv/rushiuv.github.io"
IDS=[
 ("xb_1-RnJ2q4bopwS0Go1-g","电感编码器的精度，为什么可能败在一颗过孔上？","如是有为","电感编码器双码道耦合、PCB过孔对称性和偏心误差的工程分析。",["电感编码器","PCB","角度误差"]),
 ("hPMIYOi4WDUB2cOHexarqA","美国本土钕铁硼磁体，开始进入通用汽车电机验证","电机新材料平台","MP Materials和通用汽车的美国稀土永磁供应链及电机验证进展。",["永磁体","电机","产业观察"]),
 ("_qeWfmjppoJFfVnkF9OCuw","工业伺服 / 协作机器人 / 人形关节：三种工况的选型分歧点","方寸技研","工业伺服、协作机器人与人形关节的编码器选型硬约束。",["编码器选型","伺服","机器人关节"]),
 ("C7SsdYMjnsStYrpSEJtp-g","从磁到电涡流：同一家芯片公司为什么同时押两条技术路线","方寸技研","磁编码器与电感式编码器在磁干扰和金属耦合等工况中的取舍。",["磁编码器","电感编码器","选型"]),
 ("q9cMO5NaMLGnKUu6ghrQfA","管脚兼容替代实战：TMR 芯片对标 AMR，迁移到底要改什么","方寸技研","从封装管脚、通信协议到零位、磁场与温漂验证的TMR对标AMR芯片迁移。",["TMR","AMR","芯片替代"]),
 ("qzeVfb98UsskLX-7mxCM-Q","精度是在 25℃ 标出来的，机上 120℃ 还准吗？","方寸技研","磁编码器的常温精度、全温漂移、永磁体退磁及整机误差预算。",["温度漂移","磁编码器","精度"]),
]
HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0.0.0 Safari/537.36'}
session=requests.Session()
report=[]
out=Path('content/posts')
out.mkdir(parents=True,exist_ok=True)

def download_image(job):
    i,url,referer=job
    for attempt in range(3):
        try:
            r=requests.get(url,headers={**HEADERS,'Referer':referer},timeout=55)
            r.raise_for_status()
            data=r.content
            assert 500<len(data)<20_000_000,f"Unexpected image size {len(data)}"
            im=Image.open(BytesIO(data)); im.verify()
            im=Image.open(BytesIO(data))
            assert im.width>=8 and im.height>=8,(im.width,im.height)
            fmt=im.format
            assert fmt in ('JPEG','PNG','GIF','WEBP'),fmt
            ext={'JPEG':'jpg','PNG':'png','GIF':'gif','WEBP':'webp'}[fmt]
            sha=hashlib.sha256(data).hexdigest()
            return (i,data,f'{i:03d}-{sha[:10]}.{ext}',im.size)
        except Exception as e:
            if attempt==2:raise RuntimeError(f'Image {i} download error from {url}: {e}')
            time.sleep(2*(attempt+1))

for artidx,(aid,expected_title,account,description,tags) in enumerate(IDS):
    src=f'https://raw.githubusercontent.com/{REPO}/main/.incoming_wechat/{aid}.json'
    sr=session.get(src,headers=HEADERS,timeout=65)
    sr.raise_for_status()
    entry=sr.json()
    assert entry.get('success') and entry.get('title')==expected_title,(aid,entry.get('title'))
    assert len(entry.get('text',''))>1000
    original=entry['url']
    slug='wechat-'+aid.lower().replace('_','-')
    path=out/slug/'index.md'
    assert not path.exists(),f'Already exists: {path}'
    doc=BeautifulSoup(entry['html'],'lxml')
    root=doc.select_one('#js_content') or doc.select_one('.rich_media_content')
    assert root is not None and len(root.get_text(' ',strip=True))>1100,aid
    # Preserve paragraph and illustration order, but remove WeChat-only UI.
    for elem in list(root.find_all(['script','style','iframe','mpvideo','video','audio','button','input','noscript'])):
        elem.decompose()
    imgs=root.find_all('img')
    jobs=[]
    seen=[]
    for i,img in enumerate(imgs,1):
        u=html.unescape(img.get('data-src') or img.get('src') or '')
        if u.startswith('//'):u='https:'+u
        host=urlparse(u).hostname
        assert host in ('mmbiz.qpic.cn','mmbiz.qlogo.cn'),f'Unexpected image host {host}'
        jobs.append((i,u,original))
        seen.append(img)
    assert len(jobs)>=3,(aid,len(jobs))
    print('FETCHING',expected_title,len(jobs),'images',flush=True)
    files={}
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures=[pool.submit(download_image,job) for job in jobs]
        for future in as_completed(futures):
            i,data,name,size=future.result()
            files[i]=(data,name,size)
            print('IMAGE_OK',aid,i,name,size,flush=True)
    img_dir=path.parent/'images'
    img_dir.mkdir(parents=True,exist_ok=True)
    for i,img in enumerate(seen,1):
        data,name,size=files[i]
        (img_dir/name).write_bytes(data)
        alt=img.get('alt','') or f'文章插图 {i}'
        img.attrs={'src':'images/'+name,'alt':alt}
    # Keep legitimate links; remove event handlers and exotic WeChat styling.
    for a in root.find_all('a'):
        u=a.get('href','')
        if u.startswith('http://') or u.startswith('https://'):
            a.attrs={'href':u}
        else:
            a.attrs={}
    for el in root.find_all(True):
        if el.name not in ('img','a'):
            el.attrs={}
    body=markdownify(str(root),heading_style='ATX',bullets='-',strip=['div','section','span','font']).strip()
    body=re.sub(r'\n{3,}','\n\n',body)
    references=re.findall(r'images/(\d{3}-[a-f0-9]{10}\.(?:jpg|png|gif|webp))',body)
    assert len(references)==len(imgs),(aid,len(references),len(imgs))
    assert references==[files[i][1] for i in range(1,len(imgs)+1)],(aid,'illustration order wrong')
    clean_text=BeautifulSoup(str(root),'lxml').get_text(' ',strip=True)
    assert len(clean_text)>=1100 and len(body)>=1300
    # Date is the date published to this blog; original URL is preserved separately.
    publish_time=f'2026-10-20T12:{50+artidx:02d}:00+08:00'
    front={
        'title':expected_title,
        'date':publish_time,
        'slug':slug,
        'description':description,
        'original':original,
        'original_from':f'首发于公众号「{account}」',
        'tags':tags
    }
    frontmatter=yaml.safe_dump(front,allow_unicode=True,sort_keys=False,width=1000).strip()
    path.write_text('---\n'+frontmatter+'\n---\n\n'+body+'\n',encoding='utf-8')
    rec={'slug':slug,'title':expected_title,'account':account,'images':len(imgs),'body_length':len(body),'original':original,'path':str(path)}
    report.append(rec)
    print('POST_READY',json.dumps(rec,ensure_ascii=False),flush=True)
Path('/tmp/wechat-six-publish-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
assert len(report)==6
print('ALL_SIX_ARTICLES_READY',flush=True)
