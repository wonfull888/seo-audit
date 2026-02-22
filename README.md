# SEO Audit Skill

> Evidence-based SEO diagnostic skill built from Google Search Central, Ahrefs SEO checklist, and Microsoft's AEO/GEO guidance.

[English](README.md) | [简体中文](README.zh-CN.md)

Reference sources:
- [Google Search Central](https://developers.google.com/search/docs)
- [Ahrefs SEO + AI Search Checklist](https://ahrefs.com/blog/seo-ai-search-checklist/)
- [Microsoft AEO & GEO Guide](https://about.ads.microsoft.com/content/dam/sites/msa-about/global/common/content-lib/pdf/from-discovery-to-influence-a-guide-to-aeo-and-geo.pdf)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.4.0-blue.svg)]()

## What's New in v1.4.0

- MVP site classification with `Title + URL` (7+1 types) for dynamic page selection
- Mandatory article-page capture in every audit
- Executive Summary section at report start (includes site type, crawled URLs, overall score, key risk, P0 fixes)
- Report output path standardized to `~/.claude/skills/seo-audit/reports/` (auto-create if missing)
- API key auto-load from `.env` when env var is not present

## Quick Mode Selector

The skill supports an intelligent interaction flow and can run in two modes:

| Capability | Full Mode (Recommended) | Basic Mode |
|------|--------------------------|------------|
| Setup complexity | Requires API key | Zero setup |
| Checklist size | 92 checks | 84 checks |
| Core Web Vitals | Yes (LCP, FCP, CLS, INP) | Skipped |
| PageSpeed score | Yes (Mobile + Desktop) | Skipped |
| Best use case | Complete SEO audit | Fast content and structure review |
| Free quota | 25,000 requests/day | N/A |

Detailed guide: [USAGE.md](USAGE.md)

## Why This Skill Exists

Traditional SEO tools often require account setup, paid subscriptions, and heavy workflows. This skill keeps the audit process lightweight and transparent.

### Value

1. No lock-in: run directly in Claude Code, no external dashboard required.
2. Practical: one command starts a full or basic audit.
3. Transparent: checklist logic is open and based on public guidance.
4. Evolving: includes report export, and continues to improve with each release.

## Quick Start

### Install

Copy `SKILL.md` and `references/` into your Claude Code skills directory:

```bash
git clone https://github.com/wonfull888/seo-audit.git
cp -r seo-audit ~/.claude/skills/
```

### Run

```bash
# Auto-detect report language (recommended)
/seo-audit https://example.com

# Force English report
/seo-audit https://example.com --en

# Force Chinese report
/seo-audit https://example.com --zh
```

Language selection priority:
1. Explicit flag: `--en` / `--zh`
2. Auto-detection from user input language
3. Default fallback: English

### Configure PageSpeed API Key (Recommended)

Google PageSpeed Insights API includes a free quota of 25,000 requests/day.

```bash
export PAGE_SPEED_API_KEY="your_api_key_here"
```

If environment variable is missing, the skill will auto-try:
1. `./.env`
2. `~/.claude/skills/seo-audit/.env`

More details:
- [API_KEY_SETUP.md](API_KEY_SETUP.md)
- [QUOTA.md](QUOTA.md)

## Audit Workflow

```text
User provides URL
    -> 1. Check environment (API key)
    -> 2. Detect report language
    -> 3. Classify site type (Title + URL)
    -> 4. Select representative pages (home + key business + article)
    -> 5. Collect data (curl + WebFetch + optional PageSpeed API)
    -> 6. Analyze 4 dimensions (92 checks)
    -> 7. Generate and save full Markdown report
```

## Checklist Overview

| Dimension | Checks | Weight | Notes |
|------|------|------|------|
| Technical SEO | 29 | 32% | Crawlability, indexing, security, CWV |
| On-Page SEO | 27 | 29% | Title, metadata, structure, AI-search readiness |
| Content Quality & E-E-A-T | 33 | 36% | Content depth, trust, expertise, authority |
| Local SEO | 3 | 3% | LocalBusiness schema, map signals, NAP |
| **Total** | **92** | **100%** | |

## Scoring Scale

| Grade | Score | Status |
|------|------|------|
| A | 90-100 | Excellent |
| B | 80-89 | Good |
| C | 70-79 | Average |
| D | 60-69 | Weak |
| F | <60 | Poor |

## Reports

- Default example report (English): [assets/example-report.en.md](assets/example-report.en.md)
- Chinese example report: [assets/example-report.md](assets/example-report.md)

Every report includes:
- Executive Summary at the beginning
- Site type and crawled URLs
- Overall and dimension scores
- P0/P1/P2 action items
- Full 92-row checklist table
- Actionable recommendations
- Standard brand footer

Default report save path:
- `~/.claude/skills/seo-audit/reports/seo-audit-report-{domain}-{timestamp}.md`

## File Structure

```text
seo-audit/
|-- SKILL.md
|-- README.md
|-- README.zh-CN.md
|-- USAGE.md
|-- API_KEY_SETUP.md
|-- QUOTA.md
|-- CHANGELOG.md
|-- docs/
|   |-- en/
|   |   |-- USAGE.md
|   |   |-- API_KEY_SETUP.md
|   |   `-- QUOTA.md
|   `-- zh-CN/
|       |-- USAGE.md
|       |-- API_KEY_SETUP.md
|       `-- QUOTA.md
|-- references/
|   |-- report-template.md
|   |-- report-template.en.md
|   |-- report-template.zh-CN.md
|   |-- language-detection.md
|   `-- SEO_TERMINOLOGY_GLOSSARY.md
`-- assets/
    |-- example-report.en.md
    |-- example-report.md
    `-- example-report.zh-CN.md
```

## License

[MIT License](LICENSE)

## Acknowledgements

- Google Search Central
- Ahrefs SEO team
- Microsoft Ads and Search guidance team

---

**SEO Audit Skill** | [GitHub](https://github.com/wonfull888/seo-audit) | Developer: [x.com/wonfull888](https://x.com/wonfull888)
