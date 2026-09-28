"""把站点地图里的每一个网址推给 IndexNow（Bing、Yandex、Naver、Seznam 共用）。

用法：先构建（public/sitemap.xml 存在），并确认密钥文件已上线，然后
    python tools/indexnow.py
密钥文件是 static/<key>.txt，内容就是 key 本身。
"""
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = "rushiuv.github.io"
ENDPOINT = "https://api.indexnow.org/indexnow"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    keys = [p for p in (ROOT / "static").glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}\.txt", p.name)]
    if not keys:
        sys.exit("找不到 IndexNow 密钥文件 static/<32位hex>.txt")
    key = keys[0].stem
    key_url = f"https://{HOST}/{key}.txt"

    # 密钥文件必须先上线，否则 IndexNow 会拒绝
    for _ in range(30):
        try:
            with urllib.request.urlopen(key_url, timeout=15) as r:
                if r.read().decode().strip() == key:
                    break
        except Exception:
            pass
        time.sleep(10)
    else:
        sys.exit(f"密钥文件还没上线：{key_url}")

    sitemap = (ROOT / "public" / "sitemap.xml").read_text(encoding="utf-8")
    urls = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    urls = [u for u in dict.fromkeys(urls) if u.startswith(f"https://{HOST}/")]
    body = json.dumps({"host": HOST, "key": key, "keyLocation": key_url, "urlList": urls}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            print(f"IndexNow：提交 {len(urls)} 个网址，HTTP {r.status}")
    except urllib.error.HTTPError as e:
        print(f"IndexNow：提交 {len(urls)} 个网址，HTTP {e.code} {e.read().decode(errors='replace')[:300]}")
        sys.exit(1)


if __name__ == "__main__":
    main()
