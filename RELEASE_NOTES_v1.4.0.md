# v1.4.0 - MVP Site Classification and Dynamic Page Selection

Release date: 2026-02-22

## Highlights

- Added MVP site classification with `Title + URL` signals (Top-1 output).
- Introduced 7+1 site type model:
  - Corporate
  - E-commerce
  - Content
  - Tool/SaaS
  - Community
  - Portal
  - Single-Page Site
  - Hybrid/Unknown (fallback)
- Added dynamic page selection flow:
  - Homepage
  - Key business page
  - Mandatory article page

## Reporting Improvements

- Added required **Executive Summary** at the start of each report.
- Executive Summary now must include:
  - Site type
  - Crawled page URLs
  - Total score and overall judgment
  - Weakest dimension and core risk
  - Top 1-2 urgent P0 fixes
- Standardized report storage path:
  - `~/.claude/skills/seo-audit/reports/`
  - Auto-create if the folder does not exist

## Runtime and Safety Enhancements

- Added `.env` auto-load fallback for `PAGE_SPEED_API_KEY`:
  1. `./.env`
  2. `~/.claude/skills/seo-audit/.env`
- Strengthened pre-release API key safety requirements in product docs.

## Validation and Acceptance

Added test artifacts for v1.4.0 MVP validation:

- `tests/evaluate_site_classification_v140.py`
- `tests/site_classification_samples_v140.json`
- `tests/v1.4.0-site-classification-results.md`
- `tests/v1.4.0-site-classification-results.json`
- `tests/v1.4.0-acceptance.md`

Current sample-run result:

- Reachable samples tested: 9
- Correct classifications: 9
- Hit rate (reachable set): 100.00%
- One sample was blocked by remote anti-bot behavior.

## Full Changelog

See `CHANGELOG.md` for full details.
