"""把 VerySync_notes 里存档的公众号「如是有为」已发表文章导入 Hugo content/posts。

用法（在博客根目录）：
    python tools/import_wechat.py
可重复运行：每次先清空 content/posts 下由本脚本生成的文件再重建。
"""
import hashlib
import html
import re
import shutil
import sys
from pathlib import Path

SRC = Path(r"D:\VerySync\VerySync_notes\2-Resources\2K-公众号-如是有为")
IMG_SRC = Path(r"D:\VerySync\VerySync_notes\2-Resources\_source")
ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "content" / "posts"
IMG_DST = ROOT / "static" / "images"

FNAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}) (.+)\.md$")
STAT_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*$")
EMBED_RE = re.compile(r"!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\\?\|([^\]]*))?\]\]")
TOPIC_RE = re.compile(r'<a[^>]*class="wx_topic_link"[^>]*>(.*?)</a>', re.S)
MUSIC_RE = re.compile(r'<a[^>]*class="[^"]*js_plain-music_entry[^"]*"[^>]*>.*?</a>', re.S)
TAG_RE = re.compile(r"<[^>]+>")


def yaml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def parse(path: Path):
    m = FNAME_RE.match(path.name)
    if not m:
        return None
    day, title = m.groups()
    text = path.read_text(encoding="utf-8")
    # 去掉 frontmatter
    if text.startswith("---"):
        end = text.find("\n---", 3)
        text = text[end + 4:] if end != -1 else text
    stats = {}
    s0, s1 = text.find("<!-- stats:start -->"), text.find("<!-- stats:end -->")
    if s0 != -1 and s1 != -1:
        for line in text[s0:s1].splitlines():
            mm = STAT_RE.match(line)
            if mm:
                stats[mm.group(1)] = mm.group(2)
    i = text.find("## 正文")
    if i == -1:
        return None
    body = text[i + len("## 正文"):].strip("\n")
    return day, title.strip(), stats, body


def clean_body(body: str, used_images: set) -> str:
    def embed(m):
        name = m.group(1).strip()
        used_images.add(name)
        return f"![](/images/{name})"

    body = EMBED_RE.sub(embed, body)
    body = WIKILINK_RE.sub(lambda m: (m.group(2) or m.group(1)).strip(), body)
    body = TOPIC_RE.sub(lambda m: m.group(1), body)
    body = MUSIC_RE.sub("", body)
    body = body.replace("\u200c", "")
    body = body.replace("](http://mmbiz.qpic.cn", "](https://mmbiz.qpic.cn")
    return body.rstrip() + "\n"


def description(body: str) -> str:
    for para in body.split("\n\n"):
        p = para.strip()
        if not p or p.startswith(("!", "#", "|", "<!--", ">")):
            continue
        p = TAG_RE.sub("", html.unescape(p))
        p = re.sub(r"[*_`\[\]]", "", p)
        p = re.sub(r"\(https?://[^)]*\)", "", p)
        p = re.sub(r"\s+", " ", p).strip()
        if len(p) >= 20:
            return p[:120] + ("…" if len(p) > 120 else "")
    return ""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    for old in POSTS.glob("*.md"):
        if old.name != "_index.md":
            old.unlink()
    IMG_DST.mkdir(parents=True, exist_ok=True)
    used_images: set = set()
    n = 0
    skipped = []
    for path in sorted(SRC.glob("*.md")):
        r = parse(path)
        if not r:
            skipped.append(path.name)
            continue
        day, title, stats, body = r
        link = stats.get("原文链接", "")
        slug = link.rsplit("/", 1)[-1] if "mp.weixin.qq.com/s/" in link else ""
        if not slug:
            slug = hashlib.md5(path.name.encode("utf-8")).hexdigest()[:10]
        pub = stats.get("发布时间", "") or day
        date = pub.replace(" ", "T") + (":00+08:00" if " " in pub else "T12:00:00+08:00")
        body = clean_body(body, used_images)
        fm = ["---", f"title: {yaml_str(title)}", f"date: {date}", f"slug: {yaml_str(slug)}"]
        desc = description(body)
        if desc:
            fm.append(f"description: {yaml_str(desc)}")
        if link:
            fm.append(f"original: {yaml_str(link)}")
        fm.append("---\n")
        (POSTS / f"{day}-{slug}.md").write_text("\n".join(fm) + "\n" + body, encoding="utf-8")
        n += 1
    missing = []
    for name in sorted(used_images):
        src = IMG_SRC / name
        if src.exists():
            shutil.copy2(src, IMG_DST / name)
        else:
            missing.append(name)
    print(f"导入 {n} 篇；本地图 {len(used_images) - len(missing)} 张")
    if skipped:
        print("跳过（非文章或无正文）：", *skipped, sep="\n  ")
    if missing:
        print("缺图：", *missing, sep="\n  ")
        sys.exit(1)


if __name__ == "__main__":
    main()
