#!/usr/bin/env python3
"""Evaluate v1.4.1 site classification enhancements.

v1.4.1 logic:
- score = 0.5 * TitleScore + 0.3 * URLScore + 0.2 * NavScore
- output Top-2 + confidence
- low/medium confidence uses non-blocking default Top-1 strategy
- measure article-page hit with secondary path search
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
from typing import Any, Dict, List, Set, Tuple


UA = "Mozilla/5.0 (compatible; SEOAuditSkill/1.4.1; +https://github.com/wonfull888/seo-audit)"
TIMEOUT = 8

WEIGHTS = {"title": 0.5, "url": 0.3, "nav": 0.2}

ARTICLE_PRIMARY = ["/blog", "/news", "/article", "/post"]
ARTICLE_SECONDARY = ["/insights", "/docs"]

TYPES = [
    "corporate",
    "ecommerce",
    "content",
    "tool_saas",
    "community",
    "portal",
    "single_page",
]

KEYWORDS = {
    "title": {
        "corporate": ["official", "官网", "company", "corporate", "group", "services", "solutions", "home"],
        "ecommerce": ["shop", "store", "buy", "商城", "购物", "electronics", "fashion", "deals", "product"],
        "content": ["blog", "news", "article", "insights", "search central"],
        "tool_saas": ["platform", "software", "tool", "workspace", "saas", "productivity", "ai workspace"],
        "community": ["forum", "forums", "community", "discuss", "discussion", "thread"],
        "portal": ["mail", "weather", "finance", "sports", "videos", "portal", "headline", "yahoo"],
        "single_page": ["landing page", "one page", "single page", "theme", "start bootstrap"],
    },
    "url": {
        "corporate": ["/about", "/services", "/solutions", "/company", "/contact", "/case"],
        "ecommerce": ["/product", "/shop", "/store", "/cart", "/checkout", "/category", "/itm", "/p/"],
        "content": ["/blog", "/news", "/article", "/post", "/insights"],
        "tool_saas": ["/features", "/pricing", "/integrations", "/workspace", "/app", "/product"],
        "community": ["/forum", "/forums", "/thread", "/topic", "/community", "/discuss"],
        "portal": ["/news", "/finance", "/sports", "/weather", "/video", "/mail"],
        "single_page": [],
    },
    "nav": {
        "corporate": ["about", "services", "solutions", "company", "contact", "about us"],
        "ecommerce": ["shop", "store", "product", "cart", "checkout", "deals"],
        "content": ["blog", "news", "article", "insights", "guides"],
        "tool_saas": ["features", "pricing", "integrations", "login", "sign up", "start free"],
        "community": ["forum", "community", "discussion", "topics", "threads"],
        "portal": ["news", "finance", "sports", "weather", "video", "entertainment"],
        "single_page": ["learn more", "get started", "contact", "pricing"],
    },
}


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ssl.create_default_context()) as resp:
        return resp.read(400_000).decode("utf-8", errors="ignore")


def extract_title(html: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1)).strip()


def extract_links_and_nav(html: str, base_url: str) -> Tuple[Set[str], List[str], int]:
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.IGNORECASE)
    links: Set[str] = set()
    anchor_count = 0
    nav_texts: List[str] = []
    base = urllib.parse.urlparse(base_url)

    nav_blocks = re.findall(r"<nav[^>]*>(.*?)</nav>", html, flags=re.IGNORECASE | re.DOTALL)
    nav_html = " ".join(nav_blocks) if nav_blocks else html[:60_000]
    nav_anchors = re.findall(r"<a[^>]*>(.*?)</a>", nav_html, flags=re.IGNORECASE | re.DOTALL)
    for a in nav_anchors[:60]:
        text = re.sub(r"<[^>]+>", " ", a)
        text = re.sub(r"\s+", " ", text).strip().lower()
        if text:
            nav_texts.append(text)

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
        links.add(f"{p.scheme}://{p.netloc}{p.path}")

    return links, nav_texts, anchor_count


def fetch_sitemap_urls(site_url: str) -> Set[str]:
    parsed = urllib.parse.urlparse(site_url)
    root = f"{parsed.scheme}://{parsed.netloc}"
    sitemap_url = root + "/sitemap.xml"
    try:
        xml = fetch_text(sitemap_url)
    except Exception:
        return set()

    locs = re.findall(r"<loc>(.*?)</loc>", xml, flags=re.IGNORECASE)
    urls: Set[str] = set()
    for loc in locs[:120]:
        loc = loc.strip()
        if not loc.endswith(".xml"):
            urls.add(loc)
    return urls


def pathset(urls: Set[str]) -> Set[str]:
    output: Set[str] = set()
    for u in urls:
        p = urllib.parse.urlparse(u)
        output.add((p.path or "/").lower())
    return output


def count_keyword_hits(text: str, words: List[str]) -> int:
    s = text.lower()
    return sum(1 for w in words if w in s)


def count_nav_hits(nav_texts: List[str], words: List[str]) -> int:
    corpus = " | ".join(nav_texts)
    return count_keyword_hits(corpus, words)


def detect_article_path(paths: Set[str]) -> Tuple[bool, bool, str]:
    primary_hit = any(any(k in p for k in ARTICLE_PRIMARY) for p in paths)
    if primary_hit:
        return True, False, "primary"
    secondary_hit = any(any(k in p for k in ARTICLE_SECONDARY) for p in paths)
    if secondary_hit:
        return True, True, "secondary"
    return False, False, "none"


def confidence_from_scores(top1: float, top2: float) -> float:
    if top1 <= 0:
        return 0.0
    gap = max(0.0, top1 - top2)
    ratio = top1 / (top1 + top2 + 1e-6)
    confidence = 0.6 * ratio + 0.4 * min(1.0, gap / max(1.0, top1))
    return max(0.0, min(1.0, confidence))


def confidence_band(confidence: float) -> str:
    if confidence >= 0.70:
        return "high"
    if confidence >= 0.45:
        return "medium"
    return "low"


def score_site(url: str) -> Dict[str, Any]:
    html = fetch_text(url)
    title = extract_title(html)
    home_links, nav_texts, anchor_count = extract_links_and_nav(html, url)

    sitemap_urls = fetch_sitemap_urls(url)
    candidates = set(home_links)
    candidates.update(sitemap_urls)
    if not candidates:
        candidates.add(url)

    paths = pathset(candidates)

    scores: Dict[str, float] = {}
    title_hits: Dict[str, int] = {}
    url_hits: Dict[str, int] = {}
    nav_hits: Dict[str, int] = {}

    for t in TYPES:
        t_hits = count_keyword_hits(title, KEYWORDS["title"][t])
        u_hits = sum(1 for pat in KEYWORDS["url"][t] if any(pat in p for p in paths))
        n_hits = count_nav_hits(nav_texts, KEYWORDS["nav"][t])

        if t == "single_page" and len(paths) <= 3 and anchor_count >= 3:
            n_hits += 2

        title_hits[t] = t_hits
        url_hits[t] = u_hits
        nav_hits[t] = n_hits
        scores[t] = WEIGHTS["title"] * t_hits + WEIGHTS["url"] * u_hits + WEIGHTS["nav"] * n_hits

    ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    top1_type, top1_score = ranked[0]
    top2_type, top2_score = ranked[1]

    conf = confidence_from_scores(top1_score, top2_score)
    band = confidence_band(conf)

    if top1_score < 0.60 and conf < 0.45:
        predicted = "hybrid"
    else:
        predicted = top1_type

    confirmation = "none"
    if band in {"medium", "low"}:
        confirmation = "default_top1_no_response"

    article_hit, secondary_used, article_path = detect_article_path(paths)

    return {
        "url": url,
        "title": title,
        "predicted": predicted,
        "top1_type": top1_type,
        "top2_type": top2_type,
        "top1_score": round(top1_score, 3),
        "top2_score": round(top2_score, 3),
        "confidence": round(conf, 3),
        "confidence_band": band,
        "confirmation_action": confirmation,
        "title_hits": title_hits,
        "url_hits": url_hits,
        "nav_hits": nav_hits,
        "article_hit": article_hit,
        "article_secondary_used": secondary_used,
        "article_hit_source": article_path,
        "used_sitemap": bool(sitemap_urls),
        "candidate_paths": len(paths),
    }


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    samples_path = repo / "tests" / "site_classification_samples_v141.json"
    out_json = repo / "tests" / "v1.4.1-site-classification-results.json"
    out_md = repo / "tests" / "v1.4.1-site-classification-results.md"

    samples = json.loads(samples_path.read_text(encoding="utf-8"))

    total = 0
    correct = 0
    article_hits = 0
    article_secondary_hits = 0
    fallback_count = 0
    errors: List[Dict[str, str]] = []
    rows: List[Dict[str, Any]] = []

    per_type_total: Dict[str, int] = defaultdict(int)
    per_type_correct: Dict[str, int] = defaultdict(int)

    for sample in samples:
        entry = dict(sample)
        url = str(entry["url"])
        expected = str(entry["expected"])
        try:
            result = score_site(url)
            predicted = str(result["predicted"])
            ok = predicted == expected

            total += 1
            correct += int(ok)
            article_hits += int(bool(result["article_hit"]))
            article_secondary_hits += int(bool(result["article_secondary_used"]))
            fallback_count += int(result["confirmation_action"] != "none" or predicted == "hybrid")
            per_type_total[expected] += 1
            per_type_correct[expected] += int(ok)

            rows.append(
                {
                    "url": url,
                    "expected": expected,
                    "predicted": predicted,
                    "ok": ok,
                    "top1": result["top1_type"],
                    "top2": result["top2_type"],
                    "confidence": result["confidence"],
                    "band": result["confidence_band"],
                    "confirm": result["confirmation_action"],
                    "article_hit": result["article_hit"],
                    "article_src": result["article_hit_source"],
                    "paths": result["candidate_paths"],
                }
            )
        except Exception as exc:  # noqa: BLE001
            errors.append({"url": url, "expected": expected, "error": f"{type(exc).__name__}: {exc}"})

    accuracy = (correct / total) if total else 0.0
    article_hit_rate = (article_hits / total) if total else 0.0
    fallback_success_rate = (fallback_count / total) if total else 0.0

    summary = {
        "total_tested": total,
        "correct": correct,
        "accuracy": round(accuracy, 4),
        "article_hit_rate": round(article_hit_rate, 4),
        "article_secondary_hits": article_secondary_hits,
        "fallback_coverage_rate": round(fallback_success_rate, 4),
        "errors": errors,
        "rows": rows,
    }
    out_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines: List[str] = []
    lines.append("# v1.4.1 Site Classification Test Results")
    lines.append("")
    lines.append(f"- Tested: {total}")
    lines.append(f"- Correct: {correct}")
    lines.append(f"- Accuracy: {accuracy:.2%}")
    lines.append(f"- Article-page hit rate: {article_hit_rate:.2%}")
    lines.append(f"- Secondary article hits: {article_secondary_hits}")
    lines.append(f"- Fallback/confirmation coverage: {fallback_success_rate:.2%}")
    lines.append(f"- Unreachable/Errors: {len(errors)}")
    lines.append("")
    lines.append("## Case Results")
    lines.append("")
    lines.append("| URL | Expected | Predicted | Top-2 | Conf | Band | Confirm | Article | Result |")
    lines.append("|-----|----------|-----------|-------|------|------|---------|---------|--------|")
    for row in rows:
        mark = "PASS" if row["ok"] else "FAIL"
        lines.append(
            f"| {row['url']} | {row['expected']} | {row['predicted']} | "
            f"{row['top1']}/{row['top2']} | {row['confidence']} | {row['band']} | {row['confirm']} | "
            f"{row['article_hit']} ({row['article_src']}) | {mark} |"
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

    print(
        "Tested={tested} Correct={correct} Accuracy={acc:.2%} ArticleHit={article:.2%} Errors={errors}".format(
            tested=total,
            correct=correct,
            acc=accuracy,
            article=article_hit_rate,
            errors=len(errors),
        )
    )
    print(f"JSON: {out_json}")
    print(f"MD:   {out_md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
