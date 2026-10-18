#!/usr/bin/env python3
"""Read-only checks for the October 2026 sensor.fans release.

Usage: python3.11 -B tools/check_site_release.py /absolute/path/to/hugo/build
Requires the project's existing beautifulsoup4 dependency. Does not build, fetch,
publish, write reports, or claim that browser/mobile rendering has been tested.
The previously published KTH7111 article contained five inline SVG illustrations.
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    from bs4 import BeautifulSoup, Tag
except ImportError:
    sys.exit("Missing beautifulsoup4; use the environment for check_readability.py.")


AI_PATH = "/posts/xj9-s7mw310cahxsmi_jda/"
MODEL_PATH = "/models/tle5012b/"
KTH_PATH = "/posts/kth7111-1us-vs-510us/"
REQUIRED_LINKS = (
    "/wiki/basics/mounting/",
    "/tags/非线性校准/",
)
FORBIDDEN_FIELDS = ("current_owner", "直白标题", "目标平台", "下一步任务")
UNPUBLISHED_TITLE = "双编码器估扭矩，空载差值曲线能不能直接扣掉"
# ECMAScript whitespace, used by /\s+/ and the existing portal.js normalizer.
JS_SPACE = r"[\u0009-\u000d\u0020\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]"
SEARCH_STRIP = re.compile(JS_SPACE + r"|[\-‐‑–—_·]")


def normalize_search(value):
    """Match portal.js for the Chinese/ASCII release query, not word stemming."""
    return SEARCH_STRIP.sub("", unicodedata.normalize("NFKC", str(value)).lower())


def search_matches(item, query):
    tokens = [normalize_search(t) for t in re.split(JS_SPACE + "+", query)]
    tokens = [t for t in tokens if t]
    text = " ".join(str(item.get(k, "")) for k in ("title", "description", "keywords"))
    haystack = normalize_search(text)
    return bool(tokens) and all(token in haystack for token in tokens)


def normalized_path(value):
    path = unquote(urlsplit(str(value)).path)
    return ("/" + path.strip("/") + "/") if path.strip("/") else "/"


def site_path(value):
    """A matching path on an unrelated domain is not an internal link."""
    parsed = urlsplit(str(value))
    if parsed.hostname and parsed.hostname.lower() not in ("sensor.fans", "www.sensor.fans"):
        return None
    return normalized_path(value)


def title_key(value):
    # Ignore punctuation changes, but never match the broad term "双编码器".
    value = unicodedata.normalize("NFKC", value).lower()
    return "".join(c for c in value if not c.isspace() and not unicodedata.category(c).startswith("P"))


def faq_section(content):
    if content is None:
        return None
    heading = next((h for h in content.find_all(["h2", "h3"])
                    if "离轴" in h.get_text()), None)
    if heading is None:
        return None
    level = int(heading.name[1])
    parts = [str(heading)]
    for node in heading.next_siblings:
        if isinstance(node, Tag) and re.fullmatch(r"h[1-6]", node.name or ""):
            if int(node.name[1]) <= level:
                break
        parts.append(str(node))
    return BeautifulSoup("".join(parts), "html.parser")


def is_latest_link(anchor):
    if anchor.find_parent(class_="home-reading") is not None:
        return False
    if "最新文章" in anchor.get_text(" ", strip=True) + anchor.get("aria-label", ""):
        return True
    section = anchor.find_parent(["section", "aside"])
    return bool(section and "最新文章" in (
        section.get("aria-label", "") + section.get_text(" ", strip=True)))


class Checks:
    def __init__(self, root):
        self.root = root
        self.results = []

    def record(self, name, passed, detail):
        self.results.append({"check": name, "passed": bool(passed), "detail": detail})

    def page_path(self, url_path):
        return self.root / unquote(urlsplit(url_path).path).lstrip("/") / "index.html"

    def page(self, url_path):
        path = self.page_path(url_path)
        if not path.is_file():
            self.record("page_exists", False, str(path.relative_to(self.root)))
            return None
        return BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")

    def single_h1(self, label, page):
        headings = page.find_all("h1")
        self.record(label + "_single_h1", len(headings) == 1 and bool(headings[0].get_text(strip=True)),
                    "h1_count=" + str(len(headings)))


def check_release(root, forbidden_titles, forbidden_slugs, minimum_svg, baseline=None):
    checks = Checks(root)
    home = checks.page("/")
    ai = checks.page(AI_PATH)
    model = checks.page(MODEL_PATH)
    kth = checks.page(KTH_PATH)

    if ai is not None:
        checks.single_h1("ai_article", ai)
        content = ai.select_one(".post .content, article .content")
        description = ai.select_one('meta[name="description"]')
        checks.record("ai_article_content", content is not None, ".content must exist")
        checks.record("ai_article_description", bool(description and description.get("content", "").strip()),
                      "non-empty meta description must exist")
        for label, value in (("body", content.get_text(" ", strip=True) if content else ""),
                             ("description", description.get("content", "") if description else "")):
            found = [field for field in FORBIDDEN_FIELDS if field in unicodedata.normalize("NFKC", value).lower()]
            checks.record("ai_clean_" + label, not found, "residue=" + repr(found))

    index = []
    if home is not None:
        script = home.select_one("script#portal-search-data")
        try:
            index = json.loads(script.get_text() if script else "")
            if not isinstance(index, list) or not all(isinstance(item, dict) for item in index):
                raise ValueError("index must be an array of objects")
            checks.record("portal_index_json", True, "entries=" + str(len(index)))
        except (ValueError, TypeError) as error:
            checks.record("portal_index_json", False, str(error))
            index = []
        matches = [item for item in index if search_matches(item, "TLE5012 离轴")]
        paths = [site_path(item.get("url", "")) for item in matches]
        checks.record("tle_multiword_and_search", MODEL_PATH in paths,
                      "query='TLE5012 离轴'; result_paths=" + repr(paths))

        kth_links = [a for a in home.find_all("a", href=True)
                     if site_path(a["href"]) == KTH_PATH]
        checks.record("kth_latest_banner", any(is_latest_link(a) for a in kth_links),
                      "KTH must be linked from a latest-article banner, not just the search JSON")
        reading = home.select_one(".home-reading, .home-reading-grid")
        featured = bool(reading and any(site_path(a["href"]) == KTH_PATH
                                       for a in reading.find_all("a", href=True)))
        checks.record("kth_featured_reading", featured, "KTH must remain in the curated reading section")

    if model is not None:
        content = model.select_one(".wiki-content, article .content")
        faq = faq_section(content)
        checks.record("tle_off_axis_faq", faq is not None, "heading containing 离轴 must exist")
        checks.record("tle_faq_no_markdown_residue", bool(faq) and "**" not in faq.get_text(),
                      "FAQ must not expose unrendered strong markers")
        links = faq.find_all("a", href=True) if faq else []
        official = any((urlsplit(a["href"]).hostname or "").lower() in
                       ("infineon.com", "www.infineon.com", "assets.infineon.com")
                       and "tle5012b" in urlsplit(a["href"]).path.lower()
                       and urlsplit(a["href"]).path.lower().endswith(".pdf") for a in links)
        checks.record("tle_faq_official_datasheet", official, "FAQ must link an official TLE5012B PDF")
        paths = {site_path(a["href"]) for a in links}
        for target in REQUIRED_LINKS:
            checks.record("tle_faq_internal_link", target in paths, target)
            checks.record("tle_faq_link_target_exists", checks.page_path(target).is_file(), target)

    if kth is not None:
        checks.single_h1("kth_article", kth)
        if baseline is not None:
            old_path = baseline / KTH_PATH.strip("/") / "index.html"
            if old_path.is_file():
                old = BeautifulSoup(old_path.read_text(encoding="utf-8"), "html.parser")
                old_content = old.select_one(".post, article")
                old_count = len(old_content.find_all("svg")) if old_content else 0
                minimum_svg = max(minimum_svg, old_count)
                checks.record("kth_baseline_svg", old_count >= 5, "baseline_article_with_hero_svg=" + str(old_count))
            else:
                checks.record("kth_baseline_svg", False, "baseline KTH article is missing")
        content = kth.select_one(".post, article")
        count = len(content.find_all("svg")) if content else 0
        checks.record("kth_article_svg_preserved", count >= minimum_svg,
                      "article_svg=" + str(count) + "; minimum=" + str(minimum_svg))

    forbidden = {title_key(t) for t in forbidden_titles if t.strip()}
    leaked = ["portal: " + str(item.get("title")) for item in index
              if item.get("kind") == "post" and title_key(str(item.get("title", ""))) in forbidden]
    for path in sorted((root / "posts").rglob("index.html")):
        page = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        if any(title_key(h.get_text(" ", strip=True)) in forbidden for h in page.find_all("h1")):
            leaked.append(str(path.relative_to(root)))
    # RSS can publish an otherwise unlinked draft too. Match exact item titles.
    for path in sorted(root.rglob("index.xml")):
        text = path.read_text(encoding="utf-8")
        for title in re.findall(r"<title(?:\s[^>]*)?>(.*?)</title>", text, re.S):
            if title_key(BeautifulSoup(title, "html.parser").get_text()) in forbidden:
                leaked.append(str(path.relative_to(root)))
    for slug in forbidden_slugs:
        target = normalized_path("/posts/" + slug.strip("/") + "/")
        if checks.page_path(target).is_file() or any(normalized_path(item.get("url", "")) == target for item in index):
            leaked.append(target)
    checks.record("unpublished_draft_absent", not leaked, "leaks=" + repr(sorted(set(leaked))))
    return checks.results


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("build_dir", type=Path, help="Hugo destination directory containing index.html")
    parser.add_argument("--baseline-build", type=Path, help="Optional previous build; compare KTH article SVG count")
    parser.add_argument("--min-kth-svg", type=int, default=5, help="Minimum article SVG count; cannot be below 5")
    parser.add_argument("--unpublished-title", action="append", default=[], help="Additional exact draft title; repeatable")
    parser.add_argument("--unpublished-slug", action="append", default=[], help="Draft slug if assigned later; repeatable")
    parser.add_argument("--json", action="store_true", help="Print checks as JSON, without writing a report")
    args = parser.parse_args()
    root = args.build_dir.resolve()
    if not root.is_dir():
        parser.error("build_dir is not a directory: " + str(root))
    if args.min_kth_svg < 5:
        parser.error("--min-kth-svg cannot weaken the published baseline of five SVGs")
    results = check_release(root, [UNPUBLISHED_TITLE] + args.unpublished_title,
                            args.unpublished_slug, args.min_kth_svg,
                            args.baseline_build.resolve() if args.baseline_build else None)
    failed = sum(not item["passed"] for item in results)
    if args.json:
        print(json.dumps({"scope": "static built HTML only; not UI, mobile, or traffic validation",
                          "passed": len(results) - failed, "failed": failed, "checks": results},
                         ensure_ascii=False, indent=2))
    else:
        for item in results:
            print(("PASS" if item["passed"] else "FAIL") + " " + item["check"] + ": " + item["detail"])
        print(str(len(results) - failed) + " passed; " + str(failed) + " failed. Static build checks only, not UI validation.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
