#!/usr/bin/env python3
"""Evaluate v1.4.0 MVP site classification hit rate.

MVP logic:
- score = 0.7 * TitleScore + 0.3 * URLScore
- output Top-1 only
- fallback to hybrid when score is too low
"""

from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple


UA = "Mozilla/5.0 (compatible; SEOAuditSkill/1.4.0; +https://github.com/wonfull888/seo-audit)"
TIMEOUT = 8

TYPES = [
    "corporate",
    "ecommerce",
    "content",
    "tool_saas",
    "community",
    "portal",
    "single_page",
    "hybrid",
]

TITLE_KEYWORDS = {
    "corporate": [
        "official",
        "官网",
        "company",
        "corporate",
        "group",
        "home",
        "services",
        "solutions",
        "home |",
    ],
    "ecommerce": [
        "shop",
        "store",
        "buy",
        "商城",
        "购物",
        "electronics store",
        "electronics",
        "fashion",
        "collectibles",
        "commerce",
        "deals",
        "product",
    ],
    "content": [
        "blog",
        "news",
        "article",
        "insights",
        "search central blog",
    ],
    "tool_saas": [
        "platform",
        "software",
        "tool",
        "workspace",
        "saas",
        "productivity",
        "design tool",
        "collaborative",
    ],
    "community": [
        "forum",
        "forums",
        "community",
        "discuss",
        "discussion",
        "thread",
    ],
    "portal": [
        "mail",
        "weather",
        "finance",
        "sports",
        "videos",
        "portal",
        "msn",
        "yahoo",
    ],
    "single_page": [
        "landing page",
        "one page",
        "single page",
        "start bootstrap",
        "theme",
    ],
}

URL_PATTERNS = {
    "corporate": ["/about", "/services", "/solutions", "/company", "/contact", "/case"],
    "ecommerce": ["/product", "/shop", "/store", "/cart", "/checkout", "/category", "/itm", "/p/"],
    "content": ["/blog", "/news", "/article", "/post", "/insights"],
    "tool_saas": ["/features", "/pricing", "/integrations", "/app", "/workspace", "/product"],
    "community": ["/forum", "/forums", "/thread", "/topic", "/community", "/discuss"],
    "portal": ["/news", "/finance", "/sports", "/weather", "/video", "/mail", "/entertainment"],
    "single_page": [],
}


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ssl.create_default_context()) as resp:
        data = resp.read(400_000)
    return data.decode("utf-8", errors="ignore")


def extract_title(html: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1)).strip()


def extract_links(html: str, base_url: str) -> Tuple[Set[str], int]:
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.IGNORECASE)
    links: Set[str] = set()
    anchor_count = 0
    base = urllib.parse.urlparse(base_url)

    for h in hrefs:
        if h.startswith("#"):
            anchor_count += 1
            continue
        full = urllib.parse.urljoin(base_url, h)
        p = urllib.parse.urlparse(full)
        if p.scheme not in {"http", "https"}:
            continue
        if p.netloc != base.netloc:
            continue
        clean = f"{p.scheme}://{p.netloc}{p.path}"
        links.add(clean)

    return links, anchor_count


def fetch_sitemap_urls(site_url: str) -> Set[str]:
    p = urllib.parse.urlparse(site_url)
    root = f"{p.scheme}://{p.netloc}"
    sitemap_url = root + "/sitemap.xml"
    urls: Set[str] = set()

    try:
        xml = fetch_text(sitemap_url)
    except Exception:
        return urls

    locs = re.findall(r"<loc>(.*?)</loc>", xml, flags=re.IGNORECASE)
    for loc in locs[:120]:
        loc = loc.strip()
        if not loc.endswith(".xml"):
            urls.add(loc)
    return urls


def pathset(urls: Set[str]) -> Set[str]:
    out: Set[str] = set()
    for u in urls:
        p = urllib.parse.urlparse(u)
        out.add(p.path.lower() or "/")
    return out


def count_hits(text: str, keywords: List[str]) -> int:
    s = text.lower()
    return sum(1 for kw in keywords if kw in s)


def score_site(site_url: str) -> Dict[str, object]:
    html = fetch_text(site_url)
    title = extract_title(html)
    home_links, anchor_count = extract_links(html, site_url)

    sitemap_urls = fetch_sitemap_urls(site_url)
    if sitemap_urls and len(sitemap_urls) >= 5:
        candidates = sitemap_urls
    else:
        candidates = set(home_links)
        candidates.update(sitemap_urls)
    if not candidates:
        candidates = {site_url}

    paths = pathset(candidates)
    unique_paths = len(paths)

    title_hits: Dict[str, int] = {}
    url_hits: Dict[str, int] = {}
    final_scores: Dict[str, float] = {}

    for t in TYPES:
        if t == "hybrid":
            continue

        t_hits = count_hits(title, TITLE_KEYWORDS[t])
        u_hits = 0
        for pat in URL_PATTERNS[t]:
            if any(pat in path for path in paths):
                u_hits += 1

        # Single-page structural bonus
        if t == "single_page" and unique_paths <= 3 and anchor_count >= 3:
            t_hits += 2

        title_hits[t] = t_hits
        url_hits[t] = u_hits
        final_scores[t] = 0.7 * t_hits + 0.3 * u_hits

    best_type, best_score = max(final_scores.items(), key=lambda kv: kv[1])
    predicted = best_type if best_score >= 0.6 else "hybrid"

    return {
        "url": site_url,
        "title": title,
        "predicted": predicted,
        "best_score": round(best_score, 3),
        "title_hits": title_hits,
        "url_hits": url_hits,
        "used_sitemap": bool(sitemap_urls),
        "candidate_paths": unique_paths,
        "anchor_links": anchor_count,
    }


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    samples_path = repo / "tests" / "site_classification_samples_v140.json"
    out_json = repo / "tests" / "v1.4.0-site-classification-results.json"
    out_md = repo / "tests" / "v1.4.0-site-classification-results.md"

    samples = json.loads(samples_path.read_text(encoding="utf-8"))
    rows = []
    total = 0
    correct = 0
    errors = []

    per_type_total = defaultdict(int)
    per_type_correct = defaultdict(int)

    for sample in samples:
        url = sample["url"]
        expected = sample["expected"]
        try:
            result = score_site(url)
            predicted = str(result["predicted"])
            ok = predicted == expected
            total += 1
            correct += int(ok)
            per_type_total[expected] += 1
            per_type_correct[expected] += int(ok)
            rows.append(
                {
                    "url": url,
                    "expected": expected,
                    "predicted": predicted,
                    "ok": ok,
                    "score": result["best_score"],
                    "title": str(result["title"])[:100],
                    "used_sitemap": result["used_sitemap"],
                    "paths": result["candidate_paths"],
                }
            )
        except Exception as exc:  # noqa: BLE001
            errors.append({"url": url, "expected": expected, "error": f"{type(exc).__name__}: {exc}"})

    accuracy = (correct / total) if total else 0.0

    summary = {
        "total_tested": total,
        "correct": correct,
        "accuracy": round(accuracy, 4),
        "errors": errors,
        "rows": rows,
    }
    out_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = []
    lines.append("# v1.4.0 MVP Site Classification Test Results")
    lines.append("")
    lines.append(f"- Tested: {total}")
    lines.append(f"- Correct: {correct}")
    lines.append(f"- Accuracy: {accuracy:.2%}")
    lines.append(f"- Unreachable/Errors: {len(errors)}")
    lines.append("")
    lines.append("## Case Results")
    lines.append("")
    lines.append("| URL | Expected | Predicted | Score | Sitemap | Paths | Result |")
    lines.append("|-----|----------|-----------|-------|---------|-------|--------|")
    for row in rows:
        mark = "PASS" if row["ok"] else "FAIL"
        lines.append(
            f"| {row['url']} | {row['expected']} | {row['predicted']} | {row['score']} | "
            f"{str(row['used_sitemap'])} | {row['paths']} | {mark} |"
        )

    lines.append("")
    lines.append("## Per-Type Hit Rate")
    lines.append("")
    lines.append("| Type | Correct | Total | Hit Rate |")
    lines.append("|------|---------|-------|----------|")
    for t in ["corporate", "ecommerce", "content", "tool_saas", "community", "portal", "single_page"]:
        t_total = per_type_total[t]
        t_correct = per_type_correct[t]
        rate = (t_correct / t_total) if t_total else 0.0
        lines.append(f"| {t} | {t_correct} | {t_total} | {rate:.2%} |")

    if errors:
        lines.append("")
        lines.append("## Errors")
        lines.append("")
        for err in errors:
            lines.append(f"- {err['url']}: {err['error']}")

    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Tested={total} Correct={correct} Accuracy={accuracy:.2%} Errors={len(errors)}")
    print(f"JSON: {out_json}")
    print(f"MD:   {out_md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
