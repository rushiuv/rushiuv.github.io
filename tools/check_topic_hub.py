#!/usr/bin/env python3.11
"""Read-only topic-hub inventory and rendered-link checks; not browser layout QA."""
import json
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parents[1]
build = Path(sys.argv[1])
tracks = json.loads((root / "data/topic_paths.json").read_text())["tracks"]
html = BeautifulSoup((build / "topics/index.html").read_text(), "html.parser")
assert len(html.select("h1")) == 1
assert len(tracks) == len(html.select(".topic-dossier")) == 6
assert len(html.select(".topic-reading-path li")) == 12
assert len({r["file"] for t in tracks for r in t["reads"]}) == 12
assert len(html.select(".topic-hub-nav a")) == 6
for t in tracks:
    article = html.select_one("#" + t["id"])
    assert article and t["question"] in article.get_text()
    assert len(article.select(".topic-resources .chip")) == len(t["basics"]) + len(t["models"])
    assert article.select_one("footer a"), t["id"]
for a in html.select("main a[href]"):
    href = a["href"]
    if href.startswith("#"):
        assert html.find(id=href[1:]), href
    elif href.startswith("/"):
        parsed = urlsplit(href)
        path = build / unquote(parsed.path).lstrip("/")
        assert (path / "index.html").is_file(), href
for image in html.select(".topic-hub-hero img"):
    assert (build / image["src"].lstrip("/")).is_file()
assert "双编码器估扭矩，空载差值曲线能不能直接扣掉" not in html.get_text()
print("PASS topic hub: 6 question paths, 12 distinct published readings, basics/model links, 6 archives, local illustration, no broken internal links or unpublished draft.")
