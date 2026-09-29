"""把 VerySync_notes 里存档的公众号「如是有为」已发表文章导入 Hugo content/posts。

用法（在博客根目录）：
    python tools/import_wechat.py
可重复运行：每次先清空 content/posts 下由本脚本生成的文件再重建。
微信 CDN 配图下载到 static/images/wx/（文件名＝URL 的 md5），已下载的不重复下载；
下载失败的图保留原外链并在结尾列出。
标签按 tools/tag_vocab.txt 在标题和正文里匹配，分成 models（芯片型号）、companies（公司/品牌）、tags（主题）。
"""
import hashlib
import html
import re
import shutil
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SRC = Path(r"D:\VerySync\VerySync_notes\2-Resources\2K-公众号-如是有为")
IMG_SRC = Path(r"D:\VerySync\VerySync_notes\2-Resources\_source")
ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "content" / "posts"
IMG_DST = ROOT / "static" / "images"
WX_DST = IMG_DST / "wx"
WX_RE = re.compile(r"https?://mmbiz\.qpic\.cn/[^\s)\"']+")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"

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


VOCAB = Path(__file__).resolve().parent / "tag_vocab.txt"
SECTIONS = {"型号": "models", "公司": "companies", "主题": "tags"}
# 主题词出现太随意，至少命中 2 次才打（标题里命中算 2 次）；型号和公司命中 1 次即打
MIN_HITS = {"models": 1, "companies": 1, "tags": 2}


def load_vocab():
    vocab = {v: [] for v in SECTIONS.values()}
    cur = None
    for line in VOCAB.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            cur = SECTIONS[line[1:-1]]
            continue
        names = [x.strip() for x in line.split("|") if x.strip()]
        pats = []
        for a in names:
            if re.fullmatch(r"[\x00-\x7f]+", a):
                pats.append(r"(?<![A-Za-z0-9])" + re.escape(a) + r"(?![A-Za-z0-9])")
            else:
                pats.append(re.escape(a))
        vocab[cur].append((names[0], re.compile("|".join(pats))))
    return vocab


def match_tags(vocab, title: str, body: str):
    text = re.sub(r"!?\[[^\]]*\]\([^)]*\)", " ", body)
    text = re.sub(r"https?://\S+", " ", text)
    out = {}
    for kind, entries in vocab.items():
        hits = []
        for name, rx in entries:
            n = len(rx.findall(text)) + 2 * len(rx.findall(title))
            if n >= MIN_HITS[kind]:
                hits.append(name)
        out[kind] = hits
    return out


def yaml_list(key: str, items) -> str:
    return f"{key}: [" + ", ".join(yaml_str(x) for x in items) + "]"


def sniff_ext(data: bytes) -> str:
    if data.startswith(b"\x89PNG"):
        return ".png"
    if data.startswith(b"\xff\xd8"):
        return ".jpg"
    if data.startswith(b"GIF8"):
        return ".gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return ".webp"
    head = data[:512].lstrip().lower()
    if head.startswith(b"<?xml") or head.startswith(b"<svg") or b"<svg" in head:
        return ".svg"
    return ""


def local_wx(url: str):
    """已下载则返回站内路径，否则 None。"""
    key = hashlib.md5(url.encode("utf-8")).hexdigest()
    for f in WX_DST.glob(key + ".*"):
        return f"/images/wx/{f.name}"
    return None


def fetch_wx(url: str):
    if local_wx(url):
        return url, True
    real = url.replace("http://", "https://", 1)
    for _ in range(3):
        try:
            req = urllib.request.Request(real, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            ext = sniff_ext(data)
            if not ext:
                continue
            key = hashlib.md5(url.encode("utf-8")).hexdigest()
            (WX_DST / (key + ext)).write_bytes(data)
            return url, True
        except Exception:
            pass
    return url, False


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    for old in POSTS.glob("*.md"):
        if old.name != "_index.md":
            old.unlink()
    IMG_DST.mkdir(parents=True, exist_ok=True)
    WX_DST.mkdir(parents=True, exist_ok=True)
    used_images: set = set()
    n = 0
    skipped = []
    posts = []
    vocab = load_vocab()
    for path in sorted(SRC.glob("*.md")):
        r = parse(path)
        if not r:
            skipped.append(path.name)
            continue
        day, title, stats, body = r
        body = clean_body(body, used_images)
        posts.append((day, title, stats, body))

    urls = sorted({u for p in posts for u in WX_RE.findall(p[3])})
    failed = []
    with ThreadPoolExecutor(8) as ex:
        for i, (u, ok) in enumerate(ex.map(fetch_wx, urls), 1):
            if not ok:
                failed.append(u)
            if i % 100 == 0:
                print(f"  配图 {i}/{len(urls)}", flush=True)

    def to_local(m):
        return local_wx(m.group(0)) or m.group(0)

    for day, title, stats, body in posts:
        body = WX_RE.sub(to_local, body)
        link = stats.get("原文链接", "")
        slug = link.rsplit("/", 1)[-1] if "mp.weixin.qq.com/s/" in link else ""
        if not slug:
            slug = hashlib.md5((day + title).encode("utf-8")).hexdigest()[:10]
        pub = stats.get("发布时间", "") or day
        date = pub.replace(" ", "T") + (":00+08:00" if " " in pub else "T12:00:00+08:00")
        fm = ["---", f"title: {yaml_str(title)}", f"date: {date}", f"slug: {yaml_str(slug)}"]
        desc = description(body)
        if desc:
            fm.append(f"description: {yaml_str(desc)}")
        if link:
            fm.append(f"original: {yaml_str(link)}")
        for kind, items in match_tags(vocab, title, body).items():
            if items:
                fm.append(yaml_list(kind, items))
        fm.append("---\n")
        (POSTS / f"{day}-{slug}.md").write_text("\n".join(fm) + "\n" + body, encoding="utf-8")
        n += 1
    # 不再被任何文章引用的微信配图删掉（例如 2026-09-29 修掉的贴图水印版、封面版）
    referenced = set()
    for f in POSTS.glob("*.md"):
        referenced.update(re.findall(r"/images/wx/([^)\s\"']+)", f.read_text(encoding="utf-8")))
    orphans = [f for f in WX_DST.iterdir() if f.is_file() and f.name not in referenced]
    for f in orphans:
        f.unlink()
    if orphans:
        print(f"删除未被引用的配图 {len(orphans)} 张")

    missing = []
    for name in sorted(used_images):
        src = IMG_SRC / name
        if src.exists():
            shutil.copy2(src, IMG_DST / name)
        else:
            missing.append(name)
    print(f"导入 {n} 篇；库内本地图 {len(used_images) - len(missing)} 张；"
          f"微信配图 {len(urls) - len(failed)}/{len(urls)} 张已本地化")
    if failed:
        print("微信配图下载失败（保留外链）：", *failed, sep="\n  ")
    if skipped:
        print("跳过（非文章或无正文）：", *skipped, sep="\n  ")
    if missing:
        print("缺图：", *missing, sep="\n  ")
    if missing or failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
