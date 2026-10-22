#!/usr/bin/env python3.11
"""Read-only source/build checks. Run after Hugo; needs PyYAML and bs4.

Checks evidence metadata and navigation, not the truth of numerical specs or
current availability of remote files. Series pages are not counted as new ICs.
"""
import json
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit, unquote

import yaml
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
BUILD = Path(sys.argv[1]).resolve()
ALLOWED = {"www.conntek.com.cn", "www.monolithicpower.com", "www.sg-micro.com",
           "www.novosns.com", "www.magntek.com.cn", "www.dowaytech.com",
           "www.ichaus.de", "www.ichauschina.com", "de-shop.ichaus.com",
           "www.gw-sensor.com", "www.reagles.cn"}


def page(url):
    path = unquote(urlsplit(url).path).lstrip("/")
    return BUILD / path / "index.html"


def soup(url):
    return BeautifulSoup(page(url).read_text(), "html.parser")


def fm(path):
    return yaml.safe_load(path.read_text().split("---", 2)[1])


data = json.loads((ROOT / "data/model_catalog_20261018.json").read_text())
rows = data["entries"]
assert len(rows) == len({r["slug"] for r in rows}) == 67
directory = soup("/wiki/")
cards = {a["href"]: a for a in directory.select(".wiki-index-card")}
home = soup("/")
index = json.loads(home.select_one("#portal-search-data").string)
models = [fm(p) for p in (ROOT / "content/models").glob("*/_index.md")]
assert len(models) == 145
assert len(cards) == 145  # Model directory no longer mixes in company entries.
assert all(url.startswith('/models/') for url in cards)
company_cards = soup('/companies/').select('#company-entries .wiki-index-card')
assert len(company_cards) == 132
assert all(a['href'].startswith('/companies/') for a in company_cards)
assert directory.select_one('#wiki-kind') is None
for control in ['wiki-vendor', 'wiki-type', 'wiki-form', 'wiki-reset']:
    assert directory.select_one('#' + control), control
for row in rows:
    slug = row["slug"]
    url = f"/models/{slug}/"
    source = ROOT / f"content/models/{slug}/_index.md"
    meta = fm(source)
    text = source.read_text()
    assert meta["title"] == row["title"], slug
    assert meta["model_card"] and meta["catalog_type"] == row["type"], slug
    assert meta["official_url"] == row["url"], slug
    assert len(row["features"]) >= 4, slug
    assert "## 核心性能" in text and "## 官方资料" in text, slug
    for feature in row["features"]:
        label, value = feature.split("|", 1)
        assert f"- **{label}** {value}" in text, (slug, label)
    for link in [row["url"], *row.get("sources", [])]:
        parsed = urlsplit(link)
        assert parsed.scheme == "https" and parsed.hostname in ALLOWED, link
        assert "token=" not in parsed.query, link
    built = soup(url)
    assert len(built.select("h1")) == 1, slug
    assert built.select_one(".model-card-overview"), slug
    assert url in cards, slug
    entry = next(i for i in index if i["url"] == url)
    keywords = (entry["title"] + " " + entry["keywords"]).lower()
    for member in row["members"]:
        assert member.lower() in keywords, (slug, member)
        assert member.lower() in cards[url]["data-search"], (slug, member)
    for a in built.select(".wiki-article a[href]"):
        href = a["href"]
        if href.startswith("/"):
            assert page(href).exists(), (slug, href)

family = soup("/models/kth78/")
assert family.h1.get_text() == "KTH78系列"
for member in ["kth7801", "kth7803", "kth7812", "kth7813", "kth7814", "kth7815", "kth7816", "kth7823"]:
    assert family.select_one(f'.model-family a[href="/models/{member}/"]'), member
    assert soup(f"/models/{member}/").select_one('.model-family a[href="/models/kth78/"]'), member
for vendor in {r["vendor"] for r in rows}:
    slug = {"MPS": "mps", "iC-Haus": "ic-haus"}.get(vendor, vendor)
    links = {a["href"] for a in soup(f"/companies/{slug}/").select(".wiki-relations a")}
    expected = {f'/models/{r["slug"]}/' for r in rows if r["vendor"] == vendor}
    assert expected <= links, (vendor, expected - links)
if len(sys.argv) > 2:
    baseline = Path(sys.argv[2])
    missing = [str(p.relative_to(baseline)) for p in baseline.rglob("*")
               if p.is_file() and not (BUILD / p.relative_to(baseline)).exists()]
    assert not missing, missing[:10]
print("PASS: 67 catalog additions; 145 model/product pages; separate directory of 132 companies; filters preserved; family/member links; official source metadata; all member search aliases; company backlinks; old static paths preserved.")
print("New cards by manufacturer:", dict(Counter(r["vendor"] for r in rows)))
print("Member names (including series aliases; NOT unique new IC count):", len({m for r in rows for m in r["members"]}))
