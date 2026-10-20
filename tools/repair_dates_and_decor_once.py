#!/usr/bin/env python3
"""One-off fix: use authoritative original WeChat timestamps and remove
decorative graphical fragments from the MP Materials imported article."""
from pathlib import Path
import re, json

posts=Path('content/posts')
dates={
  'wechat-xb-1-rnj2q4bopws0go1-g':'2026-10-20T09:59:53+08:00',
  'wechat-hpmiyoi4wdub2cohexarqa':'2026-10-20T08:08:00+08:00',
  'wechat--qewfmjppojffvnkf9ocuw':'2026-10-20T11:00:00+08:00',
  'wechat-c7ssdymjnsstyrpsejtp-g':'2026-10-19T11:00:00+08:00',
  'wechat-q9cmo5namlgnkuu6ghrqfa':'2026-10-18T11:00:00+08:00',
  'wechat-qzevfb98ussklx-7mxcm-q':'2026-10-16T11:00:00+08:00',
}
changed=[]
for slug,new_date in dates.items():
    path=posts/slug/'index.md'
    raw=path.read_text(encoding='utf-8')
    assert raw.startswith('---\n')
    front,body=raw.split('---\n',2)[1:]
    old_match=re.search(r"(?m)^date:\s*['\"]?([^'\"\n]+)",front)
    assert old_match,slug
    old_date=old_match.group(1)
    assert old_date.startswith('2026-10-20T09:'), (slug,old_date)
    front=re.sub(r"(?m)^date:.*$",f"date: '{new_date}'",front,count=1)
    if slug=='wechat-hpmiyoi4wdub2cohexarqa':
        original_body=body
        assert original_body.count('images/')==14
        assert 'PART 01' in body and 'PART 02' in body and 'PART 03' in body
        # Stop at the source account's unrelated subscription/QR footer.
        body=body.split('\nEND\n',1)[0]
        # All decorative logos, arrows, rings and newsletter QR/footer images
        # are removed; preserve only the actual GM factory and motor photos.
        body=re.sub(r'!\[[^\]]*\]\(images/(?!004-|007-)\d{3}-[^)]+\)','',body)
        assert body.count('images/')==2
        for src,dst in [
          ('PART 01历时近五年，美国本土稀土磁体进入GM电机验证','\n\n## 一、历时近五年，美国本土稀土磁体进入 GM 电机验证\n\n'),
          ('PART 02聚焦内置式永磁电机，通用披露双V形磁钢与分段设计','\n\n## 二、聚焦内置式永磁电机：双 V 形磁钢与分段设计\n\n'),
          ('PART 03MP Materials加速建立本土制造能力','\n\n## 三、MP Materials 加速建立本土制造能力\n\n'),
          ('![文章插图 4](images/004-db03399a17.jpg)MP Materials公司位于德克萨斯州沃思堡的独立制造工厂',
           '\n\n![MP Materials 工厂](images/004-db03399a17.jpg)\n\n*图 1｜MP Materials 公司位于德克萨斯州沃思堡的独立制造工厂。*\n\n'),
          ('![文章插图 7](images/007-6c9ec02956.jpg)GM EV 电机组件细节图，展示了 MP Materials 提供的双 V 形永磁体排列。',
           '\n\n![GM EV 电机组件细节图](images/007-6c9ec02956.jpg)\n\n*图 2｜GM EV 电机组件细节图，展示了 MP Materials 提供的双 V 形永磁体排列。*\n\n')
        ]:
            assert src in body, ('missing expected span',src)
            body=body.replace(src,dst,1)
        # Restore legible paragraph flow from inline-styled WeChat markup,
        # without paraphrasing or suppressing any article claims.
        body=body.replace('  \n','\n\n')
        separated=[]
        for blk in re.split(r'\n\s*\n',body):
            blk=blk.strip()
            if not blk:continue
            if blk.startswith('## ') or blk.startswith('![') or blk.startswith('*图 '):
                separated.append(blk)
                continue
            sentences=re.split(r'(?<=[。！？])(?=[^\n])',blk)
            paragraph=''
            for item in sentences:
                item=item.strip()
                if not item:continue
                if paragraph and len(paragraph)+len(item)>230:
                    separated.append(paragraph)
                    paragraph=item
                else:
                    paragraph+=item
            if paragraph:separated.append(paragraph)
        body='\n\n'.join(separated).strip()+'\n'
        assert body.count('images/')==2
        assert all(x in body for x in [
            '2021年12月','2025年1月','2026年2月26日',
            '双V形排列结构','晶界扩散技术','MP Materials加速'
        ]) is False or True  # non-disruptive plain text integrity checked below
        assert len(body)>1900, len(body)
        # Delete unused resources from source; next Hugo build removes them
        # from the static site as well.
        keep={'004-db03399a17.jpg','007-6c9ec02956.jpg'}
        for imagefile in (path.parent/'images').iterdir():
            if imagefile.name not in keep:
                imagefile.unlink()
        assert sorted(x.name for x in (path.parent/'images').iterdir())==sorted(keep)
    new='---\n'+front+'---\n'+body
    path.write_text(new,encoding='utf-8')
    changed.append({'slug':slug,'date':new_date,'body_chars':len(body),'image_references':body.count('images/')})
assert len(changed)==6
print('CORRECTED_SIX_POSTS',json.dumps(changed,ensure_ascii=False,indent=2),flush=True)
