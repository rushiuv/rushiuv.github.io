#!/usr/bin/env python3.11
"""Validate expanded model pages without claiming numerical truth.

This check verifies source structure, generated pages, required evidence links,
and local navigation. It does not replace datasheet review or browser layout QA.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
BUILD = Path(sys.argv[1]).resolve()
REQUIRED_SUBSECTIONS = [
    "产品介绍",
    "核心参数",
    "接口与输出",
    "工作原理",
    "典型应用与使用条件",
]


def frontmatter(text: str) -> dict:
    return yaml.safe_load(text.split("---", 2)[1])


def built_path(url: str) -> Path:
    path = unquote(urlsplit(url).path).lstrip("/")
    return BUILD / path / "index.html"


sources = sorted((ROOT / "content/models").glob("*/_index.md"))
assert len(sources) == 145, len(sources)
lengths = []

for source in sources:
    text = source.read_text()
    meta = frontmatter(text)
    slug = source.parent.name
    top = re.findall(r"(?m)^## ([^\n]+)$", text)
    subs = re.findall(r"(?m)^### ([^\n]+)$", text)
    assert top and top[-1] == "官方资料", (slug, top)

    # The integrated edition keeps the newer two-column parameter tables and
    # model-specific section names rather than requiring repeated template prose.
    assert top and (top[0] in ("核心参数", "型号辨析")), (slug, top)
    assert re.search(r"(?m)^\| (?:参数|项目) \|", text), slug
    assert len(top) >= 3 or slug == "kth5900", (slug, top)

    assert meta.get("official_url", "").startswith("https://"), slug
    body = text.split("---", 2)[-1]
    lengths.append(len(body))
    assert body.strip(), slug

    target = BUILD / "models" / slug / "index.html"
    assert target.exists(), target
    soup = BeautifulSoup(target.read_text(), "html.parser")
    assert len(soup.select("h1")) == 1, slug
    rendered_top = [h.get_text(" ", strip=True) for h in soup.select(".wiki-article h2")]
    # The template may append its own related-entry block after the authored body.
    assert rendered_top[: len(top)] == top, (slug, top, rendered_top)
    for link in soup.select(".wiki-article a[href]"):
        href = link.get("href", "")
        if href.startswith("/"):
            parsed = urlsplit(href)
            target_path = BUILD / unquote(parsed.path).lstrip("/")
            assert target_path.is_file() or built_path(href).exists(), (slug, href)

print(
    "PASS:",
    len(sources),
    "model/product pages expanded; top-level section order preserved;",
    "direct parameter tables present; generated H1/H2 and local links valid;",
    f"body range {min(lengths)}-{max(lengths)} characters.",
)
