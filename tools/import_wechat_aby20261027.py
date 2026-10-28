#!/usr/bin/env python3
"""Import one public WeChat article into the Hugo blog. Fail closed on incomplete pages."""
import datetime as dt
import hashlib
import html
import pathlib
import re
import sys
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from curl_cffi import requests
from PIL import Image
from io import BytesIO

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE_ID = "ABYg9OZbkaFjGJch201cgQ"
URL = "https://mp.weixin.qq.com/s/" + SOURCE_ID
SLUG = "wechat-" + SOURCE_ID.lower()
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Referer": "https://mp.weixin.qq.com/",
}
client = requests.Session(impersonate="chrome")
def fetch(url):
    r = client.get(url, headers=HEADERS, timeout=45)
    r.raise_for_status()
    return r
def valid_page(title, content):
    if len(title.strip()) < 3 or len(title) > 180 or len(content.strip()) < 500:
        return False
    checks = ("环境异常", "请完成安全验证", "请在微信客户端打开", "Too Many Requests", "Access denied")
    if any(q in title for q in checks) or any(q in content[:180] for q in checks):
        return False
    return True
def yml(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'
def image_local(url, n):
    if url.startswith("//"):
        url = "https:" + url
    parsed = urlparse(url)
    if parsed.scheme != "https" or not (parsed.hostname or "").endswith((".qpic.cn", ".qq.com")):
        raise ValueError("Unexpected image host " + str(parsed.hostname))
    data = fetch(url).content
    if len(data) < 100 or len(data) > 14_000_000:
        raise ValueError("Image bytes outside limit: " + str(len(data)))
    im = Image.open(BytesIO(data))
    im.verify()
    fmt = im.format
    ext = {"JPEG":".jpg","PNG":".png","GIF":".gif","WEBP":".webp","BMP":".bmp"}.get(fmt)
    if ext is None:
        raise ValueError("Image format not supported: " + str(fmt))
    file = f"{SLUG}-{n:03d}-{hashlib.sha256(data).hexdigest()[:12]}{ext}"
    dest = ROOT / "static" / "images" / "wx" / file
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return "/images/wx/" + file

print("SOURCE", URL, flush=True)
mode = None
try:
    r = fetch(URL)
    raw = r.text
    soup = BeautifulSoup(raw, "html.parser")
    title_tag = soup.select_one("#activity-name") or soup.select_one("h1.rich_media_title")
    node = soup.select_one("#js_content")
    title = title_tag.get_text(" ", strip=True) if title_tag else ""
    body_plain = node.get_text(" ", strip=True) if node else ""
    if valid_page(title, body_plain):
        mode = "html"
except Exception as err:
    print("WECHAT_DIRECT_ERROR", type(err).__name__, str(err)[:240], flush=True)

if mode == "html":
    name_node = soup.select_one("#js_name") or soup.select_one(".rich_media_meta_nickname")
    byline = name_node.get_text(" ", strip=True) if name_node else ""
    for bad in node.select("script,style,noscript,iframe,form,button,svg,mpvoice,mp-common-profile"):
        bad.decompose()
    seen = {}
    for element in node.select("img"):
        url = element.get("data-src") or element.get("src")
        if not url or url.startswith("data:"):
            # An inline data URI cannot be trusted as the source of an original image.
            if url and url.startswith("data:") and len(url) > 250:
                raise RuntimeError("Unexpected embedded image")
            continue
        if url not in seen:
            if len(seen) >= 60:
                raise RuntimeError("More than 60 source images; review manually.")
            seen[url] = image_local(url, len(seen) + 1)
        element["src"] = seen[url]
        for key in list(element.attrs):
            if key not in ("src", "alt", "width", "height"):
                del element.attrs[key]
        element["loading"] = "lazy"
        element["decoding"] = "async"
    for element in node.select("*"):
        for key in list(element.attrs):
            if key.lower().startswith("on") or key in ("data-src", "data-ratio", "data-w", "contenteditable", "style"):
                del element.attrs[key]
    # The native WeChat root is invisible until WeChat JavaScript reveals it.
    # Give standalone Hugo posts a neutral, visible content wrapper.
    node.attrs = {"class": ["wechat-article-content"]}
    body = str(node)
    pub_match = re.search(r'(?:var\s+ct\s*=\s*|publish_time\s*[:=]\s*)["\u0027](\d{10})', raw)
    pub = dt.datetime.fromtimestamp(int(pub_match.group(1)), dt.timezone(dt.timedelta(hours=8))) if pub_match else None
    img_count = len(seen)
else:
    print("USING_JINA_READER", flush=True)
    result = fetch("https://r.jina.ai/" + URL).text
    tm = re.search(r"(?m)^Title:\s*(.+)$", result)
    source_line = re.search(r"(?m)^URL Source:\s*(.+)$", result)
    main = re.search(r"Markdown Content:\s*([\s\S]+)$", result)
    title = tm.group(1).strip() if tm else ""
    content = main.group(1).strip() if main else ""
    if not source_line or SOURCE_ID not in source_line.group(1):
        raise RuntimeError("Reader did not confirm the supplied article URL.")
    if not valid_page(title, content):
        raise RuntimeError("Reader returned incomplete/challenge text; no article written.")
    byline = ""
    pub = None
    seen = {}
    def replace_img(match):
        alt, src = match.group(1), match.group(2)
        if src.startswith("//"):
            src = "https:" + src
        if src not in seen:
            if len(seen) >= 60:
                raise RuntimeError("Too many images")
            seen[src] = image_local(src, len(seen) + 1)
        return "![" + alt + "](" + seen[src] + ")"
    body = re.sub(r"!\[([^\]]*)\]\((https?:\/\/[^ )]+|\/\/[^ )]+)\)", replace_img, content)
    img_count = len(seen)

if len(re.sub(r"<[^>]+>", "", body).strip()) < 400:
    raise RuntimeError("Article not complete")
now = dt.datetime.now(dt.timezone(dt.timedelta(hours=8)))
post_date = pub or now
stamp = post_date.isoformat(timespec="seconds")
from_name = "微信公众号「" + byline + "」" if byline else "微信公众号（见原文链接）"
text_only = BeautifulSoup(body, "html.parser").get_text(" ", strip=True) if mode == "html" else re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)
intro = re.sub(r"\s+", " ", text_only).strip()[:110]
meta = (
    "---\n"
    "title: " + yml(title) + "\n"
    "date: " + stamp + "\n"
    "slug: " + yml(SLUG) + "\n"
    "description: " + yml(intro) + "\n"
    "original: " + yml(URL) + "\n"
    "original_from: " + yml("转载自" + from_name) + "\n"
    "tags: [\"转载\"]\n"
    "---\n\n"
)
notice = (
    "<p class=\"post-meta\">本文转载自" + html.escape(from_name) +
    "，<a href=\"" + URL + "\" rel=\"noopener noreferrer\">点击阅读原文</a>。"
    "版权归原作者所有。</p>\n\n"
)
post = meta + "<div class=\"wechat-reprint\">\n" + notice + body + "\n</div>\n"
fname = (pub or now).date().isoformat() + "-" + SLUG + ".md"
for dirname in ("content/posts", "posts_extra"):
    target = ROOT / dirname / fname
    target.parent.mkdir(exist_ok=True, parents=True)
    if target.exists():
        raise RuntimeError("Article file already exists: " + str(target))
    target.write_text(post, encoding="utf-8")
print("SUCCESS", title, "mode=", mode, "images=", img_count, "date=", stamp, "file=", fname, flush=True)
