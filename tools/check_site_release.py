#!/usr/bin/env python3
"""Read-only checks for the October 2026 sensor.fans release.

Usage: python3.11 -B tools/check_site_release.py /absolute/path/to/hugo/build
Requires the project's existing beautifulsoup4 and PyYAML dependencies. Does not build, fetch,
publish, write reports, or claim that browser/mobile rendering has been tested.
The previously published KTH7111 article contained five inline SVG illustrations.
Also checks the current 37 basics / 43 applications and the explicit reference
topic mapping. Source validation is read-only and uses this script's repository.
"""

import argparse
from collections import Counter
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

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
SOURCE_ROOT = Path(__file__).resolve().parent.parent
EXPECTED_BASICS = 37
EXPECTED_APPLICATIONS = 43
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


def read_json(checks, path, label, expected_type):
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, expected_type):
            raise ValueError("unexpected JSON type")
    except (OSError, ValueError) as error:
        checks.record(label, False, str(path) + ": " + str(error))
        return expected_type()
    return value


def source_entries(checks, source_root, folder, flag):
    entries, errors = [], []
    for path in sorted((source_root / "content" / folder).glob("*.md")):
        if path.name.startswith("_"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---"):
                raise ValueError("missing front matter")
            # Hugo accepts YAML front matter, including the older JSON objects.
            params = yaml.safe_load(text.split("---", 2)[1])
            if not isinstance(params, dict):
                raise ValueError("front matter must be an object")
            if not params.get(flag):
                continue
            slug = params.get("slug", path.stem)
            if not re.fullmatch(r"[a-z0-9-]+", slug):
                raise ValueError("unexpected slug: " + str(slug))
            entries.append({"slug": slug, "url": "/" + folder + "/" + slug + "/",
                            "params": params, "file": path})
        except (OSError, ValueError, TypeError, yaml.YAMLError) as error:
            errors.append(str(path.relative_to(source_root)) + ": " + str(error))
    checks.record(folder + "_source_format", not errors, "errors=" + repr(errors))
    return entries


def grouped_navigation(nav):
    groups, current = {}, None
    if nav is not None:
        for node in nav.find_all(["h2", "a"]):
            if node.name == "h2":
                current = node.get_text(" ", strip=True)
                groups.setdefault(current, set())
            elif current is not None and node.has_attr("href"):
                target = site_path(node["href"])
                if target is not None:
                    groups[current].add(target)
    return groups


def navigation_duplicates(nav):
    """Set-based completeness alone would hide repeated groups or links."""
    if nav is None:
        return {}
    headings = Counter(h.get_text(" ", strip=True) for h in nav.find_all("h2"))
    links = Counter(site_path(a["href"]) for a in nav.find_all("a", href=True))
    duplicate_groups = {name: count for name, count in headings.items() if count > 1}
    duplicate_links = {path: count for path, count in links.items() if path is not None and count > 1}
    return {key: value for key, value in (("groups", duplicate_groups), ("links", duplicate_links)) if value}


def check_entry_families(checks, home, index, source_root):
    """Check source -> built page -> group navigation -> searchable result."""
    families = (
        ("wiki/basics", "basic", "basic_entry", "basic_group", "basics.json",
         EXPECTED_BASICS, ".basics-group", ".basics-card"),
        ("applications", "application", "application_entry", "application_group", "applications.json",
         EXPECTED_APPLICATIONS, ".application-group", ".application-card"),
    )
    all_entries = {}
    for folder, kind, flag, group_key, data_file, expected_count, section_selector, card_selector in families:
        entries = source_entries(checks, source_root, folder, flag)
        all_entries[kind] = entries
        checks.record(kind + "_source_count", len(entries) == expected_count,
                      "actual=" + str(len(entries)) + "; expected=" + str(expected_count))
        groups = read_json(checks, source_root / "data" / data_file, kind + "_group_data", list)
        group_names = [group.get("title") for group in groups if isinstance(group, dict)]
        expected_groups = {name: {entry["url"] for entry in entries
                                if entry["params"].get(group_key) == name} for name in group_names}
        unknown = [entry["slug"] for entry in entries if entry["params"].get(group_key) not in group_names]
        checks.record(kind + "_source_groups", not unknown and len(group_names) == len(set(group_names)),
                      "unknown=" + repr(unknown) + "; groups=" + repr(group_names))
        overview = checks.page("/" + folder + "/")
        if overview is not None:
            section_counts = Counter(section.select_one("h2").get_text(" ", strip=True)
                                     for section in overview.select(section_selector) if section.select_one("h2"))
            sections = {section.select_one("h2").get_text(" ", strip=True): section
                        for section in overview.select(section_selector) if section.select_one("h2")}
            group_errors = []
            for name, targets in expected_groups.items():
                section = sections.get(name)
                actual = [site_path(a["href"]) for a in section.select(card_selector + "[href]")] if section else []
                if set(actual) != targets or len(actual) != len(targets) or section_counts[name] != 1:
                    group_errors.append({"group": name, "expected": len(targets), "actual": len(actual),
                                         "section_count": section_counts[name],
                                         "missing": sorted(targets - set(actual))})
            checks.record(kind + "_overview_groups", not group_errors and set(sections) == set(expected_groups),
                          "group_errors=" + repr(group_errors))
        missing, content_errors, navigation_errors, index_errors, empty_sections = [], [], [], [], []
        for entry in entries:
            target = checks.page_path(entry["url"])
            if not target.is_file():
                missing.append(entry["url"])
                continue
            page = BeautifulSoup(target.read_text(encoding="utf-8"), "html.parser")
            h1 = page.find_all("h1")
            if len(h1) != 1 or not h1[0].get_text(strip=True) or page.select_one("article .content") is None:
                content_errors.append(entry["url"])
            nav = page.select_one(".basic-sidebar nav")
            if grouped_navigation(nav) != expected_groups:
                navigation_errors.append(entry["url"])
            duplicates = navigation_duplicates(nav)
            if duplicates:
                navigation_errors.append({"page": entry["url"], "duplicates": duplicates})
            if any(not section.select("a[href]") for section in page.select(".basic-practice, .basic-related")):
                empty_sections.append(entry["url"])
            matches = [item for item in index if item.get("kind") == kind
                       and site_path(item.get("url", "")) == entry["url"]]
            query = entry["params"].get("reference_topic") if kind == "application" else entry["params"].get("title")
            if len(matches) != 1 or not search_matches(matches[0], query or ""):
                index_errors.append(entry["url"])
        checks.record(kind + "_built_pages", not missing, "missing=" + repr(missing))
        checks.record(kind + "_page_content", not content_errors, "invalid_h1_or_body=" + repr(content_errors))
        checks.record(kind + "_sidebar_groups", not navigation_errors, "incorrect_group_navigation=" + repr(navigation_errors))
        checks.record(kind + "_optional_links_not_empty", not empty_sections,
                      "empty_related_or_practice_section=" + repr(empty_sections))
        checks.record(kind + "_search_entries", not index_errors and
                      sum(item.get("kind") == kind for item in index) == len(entries),
                      "missing_duplicate_or_unsearchable=" + repr(index_errors))
        checks.record(kind + "_search_filter", bool(home and home.select_one(
            '[data-search-kind="' + kind + '"]')), "home must expose the " + kind + " search filter")

    applications = read_json(checks, source_root / "data/applications.json", "application_home_data", list)
    home_links = {(site_path(a["href"]), unquote(urlsplit(a["href"]).fragment))
                  for a in home.select(".home-app-card[href]")} if home else set()
    required_links = {("/applications/", group.get("id")) for group in applications if isinstance(group, dict)}
    checks.record("application_home_group_links", bool(required_links) and required_links <= home_links,
                  "required=" + repr(sorted(required_links, key=str)) + "; actual=" + repr(sorted(home_links, key=str)))

    application_overview = checks.page("/applications/")
    if application_overview is not None:
        ids = {section.get("id") for section in application_overview.select(".application-group")}
        jump_ids = {unquote(urlsplit(a["href"]).fragment)
                    for a in application_overview.select(".application-jump a[href]")}
        required_ids = {group.get("id") for group in applications if isinstance(group, dict)}
        checks.record("application_group_anchors", bool(required_ids) and required_ids <= ids and required_ids <= jump_ids,
                      "required=" + repr(sorted(required_ids, key=str)) + "; sections=" + repr(sorted(ids, key=str)))

    known_basics = {entry["slug"] for entry in all_entries["basic"]}
    invalid_relations = []
    for entries in all_entries.values():
        for entry in entries:
            related = entry["params"].get("related_basics", [])
            if not isinstance(related, list) or any(not isinstance(slug, str) or slug not in known_basics for slug in related):
                invalid_relations.append(entry["url"])
    checks.record("related_basics_source_targets", not invalid_relations,
                  "unresolved_or_invalid_related_basics=" + repr(invalid_relations))

    coverage = read_json(checks, source_root / "data/reference_coverage.json", "reference_coverage_data", dict)
    for key, kind, folder, expected_count in (("basics", "basic", "wiki/basics", 30),
                                             ("applications", "application", "applications", 43)):
        rows = coverage.get(key, [])
        if not isinstance(rows, list):
            rows = []
        known = {entry["slug"]: entry for entry in all_entries[kind]}
        errors, topics = [], []
        for row in rows:
            if not isinstance(row, dict):
                errors.append("non-object row")
                continue
            topic, slug = row.get("topic", ""), row.get("slug", "")
            if not isinstance(topic, str) or not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9-]+", slug):
                errors.append("invalid topic/slug: " + repr(row))
                continue
            topics.append(topic)
            entry = known.get(slug)
            url = "/" + folder + "/" + slug + "/"
            matches = [item for item in index if item.get("kind") == kind
                       and site_path(item.get("url", "")) == url]
            if not topic or entry is None or not checks.page_path(url).is_file():
                errors.append(str(topic) + ": source or built page missing")
            elif kind == "application" and (row.get("group") != entry["params"].get("application_group")
                                             or topic != entry["params"].get("reference_topic")):
                errors.append(str(topic) + ": source reference_topic/group differs from manifest")
            elif len(matches) != 1 or not search_matches(matches[0], topic):
                errors.append(str(topic) + ": canonical topic does not find its own page")
        checks.record("reference_" + key + "_coverage", len(rows) == expected_count and
                      len(set(topics)) == len(topics) and not errors,
                      "rows=" + str(len(rows)) + "; expected=" + str(expected_count) + "; errors=" + repr(errors))


def check_release(root, forbidden_titles, forbidden_slugs, minimum_svg, baseline=None, source_root=SOURCE_ROOT):
    checks = Checks(root)
    home = checks.page("/")
    ai = checks.page(AI_PATH)
    model = checks.page(MODEL_PATH)
    kth = checks.page(KTH_PATH)

    required_nav = [("首页", "/"), ("基础知识", "/wiki/basics/"),
                    ("型号资料", "/wiki/"), ("应用场景", "/applications/"),
                    ("技术专题", "/topics/"), ("公司品牌", "/companies/"),
                    ("博客", "/archives/")]
    for path, active in (("/", "/"), ("/wiki/", "/wiki/"),
                         ("/wiki/basics/", "/wiki/basics/"),
                         ("/applications/", "/applications/"),
                         ("/archives/", "/archives/")):
        page = home if path == "/" else checks.page(path)
        nav = page.select_one(".site-header nav") if page else None
        links = nav.find_all("a", href=True) if nav else []
        actual = [(a.get_text(" ", strip=True), site_path(a["href"])) for a in links]
        selected = [site_path(a["href"]) for a in links if a.get("aria-current") == "page"]
        checks.record("top_level_navigation", actual == required_nav and selected == [active],
                      path + ": links=" + repr(actual) + "; active=" + repr(selected))
    model_directory = checks.page("/wiki/")
    checks.record("model_directory_separate_from_basics", bool(model_directory) and
                  model_directory.select_one(".wiki-basics-banner") is None and
                  model_directory.select_one("h1").get_text(strip=True) == "型号资料库",
                  "Basics has its own top-level entry, not a large banner in the model directory")
    caption_residue = []
    for path, selector in (("/applications/", ".application-group figure figcaption"),
                           ("/wiki/basics/", ".basics-hero-art figcaption")):
        page = checks.page(path)
        if page and page.select(selector):
            caption_residue.append(path)
    checks.record("decorative_captions_removed", not caption_residue,
                  "repeated AI/not-to-scale captions=" + repr(caption_residue))

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
    check_entry_families(checks, home, index, source_root)
    return checks.results


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("build_dir", type=Path, help="Hugo destination directory containing index.html")
    parser.add_argument("--baseline-build", type=Path, help="Optional previous build; compare KTH article SVG count")
    parser.add_argument("--min-kth-svg", type=int, default=5, help="Minimum article SVG count; cannot be below 5")
    parser.add_argument("--unpublished-title", action="append", default=[], help="Additional exact draft title; repeatable")
    parser.add_argument("--unpublished-slug", action="append", default=[], help="Draft slug if assigned later; repeatable")
    parser.add_argument("--json", action="store_true", help="Print checks as JSON, without writing a report")
    parser.add_argument("--source-dir", type=Path, default=SOURCE_ROOT,
                        help="Source repository containing content and data/reference_coverage.json")
    args = parser.parse_args()
    root = args.build_dir.resolve()
    if not root.is_dir():
        parser.error("build_dir is not a directory: " + str(root))
    if args.min_kth_svg < 5:
        parser.error("--min-kth-svg cannot weaken the published baseline of five SVGs")
    results = check_release(root, [UNPUBLISHED_TITLE] + args.unpublished_title,
                            args.unpublished_slug, args.min_kth_svg,
                            args.baseline_build.resolve() if args.baseline_build else None,
                            args.source_dir.resolve())
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
