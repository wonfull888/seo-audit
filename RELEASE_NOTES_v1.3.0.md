# v1.3.0 - Complete Internationalization

Release date: 2026-02-18

## Highlights

- English is now the default documentation language on GitHub (`README.md`).
- Added Chinese companion documentation (`README.zh-CN.md`, `docs/zh-CN/*`).
- Added bilingual report templates and examples.
- Added intelligent report language selection workflow (`--en`, `--zh`, and auto-detection).

## What Changed

### 1) Bilingual Documentation System

- Added language entry pages:
  - `USAGE.md`
  - `API_KEY_SETUP.md`
  - `QUOTA.md`
- Added full bilingual docs folders:
  - `docs/en/`
  - `docs/zh-CN/`

### 2) Intelligent Report Language Selection

- Explicit override flags: `--en` and `--zh`
- Auto-detection from user input language
- Low-confidence fallback prompt strategy
- Default language: English

Reference docs:
- `references/language-detection.md`
- `references/quick-confirm-mechanism.md`

### 3) Bilingual Report Templates and Examples

- Added `references/report-template.en.md`
- Added `references/report-template.zh-CN.md`
- Kept `references/report-template.md` as compatibility entry
- Added `assets/example-report.en.md`
- Added `assets/example-report.zh-CN.md`

### 4) Planning Visibility for Next Version

- Updated `PRODUCT.md` with v1.4.0 major feature plan (smart website type detection).

## v1.4.0 Preview

- Website type detection (SaaS, E-commerce, Content, Corporate, Tool)
- Type-based dynamic page selection
- Mandatory article page capture for every site
- Confidence-based confirmation and fallback heuristics

## Full Changelog

See `CHANGELOG.md` for details.
