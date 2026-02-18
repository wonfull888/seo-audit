# Usage Guide

<!-- Terminology reference: /references/SEO_TERMINOLOGY_GLOSSARY.md -->

**Languages**: [English](USAGE.md) | [简体中文](../zh-CN/USAGE.md)

## Overview

SEO Audit Skill supports two execution modes:

1. **Full Mode (Recommended)**: requires `PAGE_SPEED_API_KEY`
2. **Basic Mode**: no API key required, skips performance metrics

## Mode Comparison

| Item | Full Mode | Basic Mode |
|------|-----------|------------|
| Checklist size | 92 checks | 84 checks |
| Core Web Vitals | Yes | No |
| PageSpeed score (mobile/desktop) | Yes | No |
| Best use case | Complete SEO audit | Fast review |

## Full Mode

### Setup

```bash
# 1) Set env var
export PAGE_SPEED_API_KEY="your_api_key_here"

# 2) Verify
echo $PAGE_SPEED_API_KEY

# 3) Run
/seo-audit https://example.com
```

### Why use Full Mode

- Includes official performance metrics (CWV + PageSpeed)
- Stronger technical SEO diagnostics
- More actionable optimization guidance

## Basic Mode

Run directly without setup:

```bash
/seo-audit https://example.com
```

Basic mode skips Core Web Vitals and PageSpeed scoring, but keeps the rest of the audit.

## Report Language Selection

```bash
# Auto-detect language (recommended)
/seo-audit https://example.com

# Force English report
/seo-audit https://example.com --en

# Force Chinese report
/seo-audit https://example.com --zh
```

Priority:
1. Explicit flag (`--en` / `--zh`)
2. Input language auto-detection
3. Default fallback: English

## FAQ

### Q1: Can I run it without API key?

Yes. Basic mode still performs 84 checks.

### Q2: Is the free quota enough?

Usually yes. PageSpeed API offers 25,000 free requests per day.

### Q3: Will API key be committed to Git?

No, if you keep it in environment variables or local `.env` and maintain `.gitignore` correctly.

## Related Docs

- [README](../../README.md)
- [API Key Setup](API_KEY_SETUP.md)
- [Quota Guide](QUOTA.md)
