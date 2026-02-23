# Report Template

## Report Structure

```markdown
# SEO Audit Report - {domain}

**Generated**: {YYYY-MM-DD HH:MM:SS}
**Pages Analyzed**: Homepage, Key Business Page, Article Page

---

## 🧭 Executive Summary

{executive_summary_300_800_words}

> Must include: site type, analyzed page scope, total score with overall judgment, weakest dimension, and the top 1-2 urgent fixes (P0).

**Crawled Pages (URLs required)**

| Page Role | URL |
|-----------|-----|
| Homepage | {homepage_url} |
| Key Business Page | {business_page_url} |
| Article Page | {article_page_url} |

---

## 📊 Overall Score

### Total Score: {score}/100 {status_emoji}

| Dimension | Score | Status |
|-----------|-------|--------|
| Technical SEO | {tech_score}/100 | {tech_status} |
| On-Page SEO | {onpage_score}/100 | {onpage_status} |
| Content Quality & E-E-A-T | {eeat_score}/100 | {eeat_status} |

### E-E-A-T Breakdown

| Dimension | Score | Status |
|-----------|-------|--------|
| Trust | {trust_score}/100 | {trust_status} |
| Experience | {exp_score}/100 | {exp_status} |
| Expertise | {expertise_score}/100 | {expertise_status} |
| Authoritativeness | {auth_score}/100 | {auth_status} |

---

## 🚨 Priority Action Items

### P0 - Must Fix Immediately

| Issue | Page | Current State | Recommendation |
|-------|------|---------------|----------------|
| {issue} | {page} | {current} | {suggestion} |

### P1 - Fix Soon

| Issue | Page | Current State | Recommendation |
|-------|------|---------------|----------------|
| {issue} | {page} | {current} | {suggestion} |

### P2 - Planned Optimization

| Issue | Page | Current State | Recommendation |
|-------|------|---------------|----------------|
| {issue} | {page} | {current} | {suggestion} |

---

## 4. Optimization Recommendations

### 4.1 Technical SEO Recommendations

{tech_suggestions}

### 4.2 On-Page SEO Recommendations

{onpage_suggestions}

### 4.3 Content & E-E-A-T Recommendations

{eeat_suggestions}

---

## 📝 Detailed Checklist (All 92 Checks)

### 1. Technical SEO Results (29)

| ID | Check Item | Home | Business | Article | Status |
|----|------------|------|----------|---------|--------|
| T1.1 | robots.txt | {result} | - | - | {status} |
| T1.2 | sitemap.xml | {result} | - | - | {status} |
| T1.3 | HTTP status code | {result} | {result} | {result} | {status} |
| T1.4 | noindex usage | {result} | {result} | {result} | {status} |
| T1.5 | Canonical tag | {result} | {result} | {result} | {status} |
| T1.6 | HTTPS redirect | {result} | - | - | {status} |
| T1.7 | www consistency | {result} | - | - | {status} |
| T1.8 | Redirect chain | {result} | {result} | {result} | {status} |
| T2.1 | PageSpeed mobile | {score} | {score} | {score} | {status} |
| T2.2 | PageSpeed desktop | {score} | {score} | {score} | {status} |
| T2.3 | LCP (Largest Contentful Paint) | {value} | {value} | {value} | {status} |
| T2.4 | FCP (First Contentful Paint) | {value} | {value} | {value} | {status} |
| T2.5 | CLS (Cumulative Layout Shift) | {value} | {value} | {value} | {status} |
| T2.6 | INP (Interaction to Next Paint) | {value} | {value} | {value} | {status} |
| T2.7 | TBT (Total Blocking Time) | {value} | {value} | {value} | {status} |
| T2.8 | TTFB (Time to First Byte) | {value} | {value} | {value} | {status} |
| T3.1 | HTTPS | {result} | {status} |
| T3.2 | SSL certificate | {result} | {status} |
| T3.3 | Mixed content | {result} | {status} |
| T3.4 | viewport | {result} | {status} |
| T4.1 | JSON-LD exists | {result} | {result} | {result} | {status} |
| T4.2 | Organization schema | {result} | - | - | {status} |
| T4.3 | Article schema | - | - | {result} | {status} |
| T4.4 | Breadcrumb schema | {result} | {result} | {result} | {status} |
| T4.5 | Author schema | - | - | {result} | {status} |
| T... | ... | ... | ... | ... | ... |

### 2. On-Page SEO Results (27)

#### 2.1 Page Data Preview

**Title & Meta Description**

| Page | Title | Length | Meta Description | Length |
|------|-------|--------|------------------|--------|
| Home | {title} | {len} | {desc} | {len} |
| Business | {title} | {len} | {desc} | {len} |
| Article | {title} | {len} | {desc} | {len} |

**Heading Structure**

- **Home**: {h1}
- **Business**: {h1}
- **Article**: {h1}

**Keyword Distribution**

- **Home**: {keywords}
- **Business**: {keywords}
- **Article**: {keywords}

#### 2.2 Detailed Check Results

| ID | Check Item | Home | Business | Article | Status |
|----|------------|------|----------|---------|--------|
| P1 | Title tag exists | {result} | {result} | {result} | {status} |
| P2 | Title length | {result} | {result} | {result} | {status} |
| P3 | Title includes keyword | {result} | {result} | {result} | {status} |
| P4 | Meta description exists | {result} | {result} | {result} | {status} |
| P5 | Meta description length | {result} | {result} | {result} | {status} |
| P6 | Single H1 tag | {result} | {result} | {result} | {status} |
| P7 | Heading hierarchy (H2-H6) | {result} | {result} | {result} | {status} |
| P8 | Image alt coverage | {result} | {result} | {result} | {status} |
| P9 | Image dimensions defined | {result} | {result} | {result} | {status} |
| P10 | Favicon | {result} | - | - | {status} |
| P11 | Open Graph tags | {result} | {result} | {result} | {status} |
| P12 | Twitter card | {result} | {result} | {result} | {status} |
| P13 | Natural keyword distribution | {result} | {result} | {result} | {status} |
| P14 | Internal link count | {result} | {result} | {result} | {status} |
| P15 | Outbound references | - | - | {result} | {status} |
| P16 | Descriptive anchor text | {result} | {result} | {result} | {status} |
| P17 | List usage (ul/ol) | {result} | {result} | {result} | {status} |
| P18 | Emphasis tags (b/strong) | {result} | {result} | {result} | {status} |
| P19 | Blockquote usage | - | - | {result} | {status} |
| P20 | Table data presentation | - | - | {result} | {status} |
| P21 | Multimedia richness | {result} | {result} | {result} | {status} |
| P22 | Non-intrusive ads | {result} | {result} | {result} | {status} |
| P23 | Non-intrusive popups | {result} | {result} | {result} | {status} |
| P24 | Reading difficulty | {result} | {result} | {result} | {status} |
| P25 | Font readability | {result} | {result} | {result} | {status} |
| P26 | Color contrast | {result} | {result} | {result} | {status} |
| P27 | Mobile tap targets | {result} | {result} | {result} | {status} |

### 3. Content Quality & E-E-A-T Results (33)

| ID | Check Item | Home | Business | Article | Status |
|----|------------|------|----------|---------|--------|
| E1 | Author byline | - | - | {result} | {status} |
| E2 | Author bio link | - | - | {result} | {status} |
| E3 | Editorial process | - | - | {result} | {status} |
| E4 | Published date | - | - | {result} | {status} |
| E5 | Last updated date | - | - | {result} | {status} |
| E6 | About page | {result} | - | - | {status} |
| E7 | Contact info | {result} | - | - | {status} |
| E8 | Privacy policy | {result} | - | - | {status} |
| E9 | Terms of service | {result} | - | - | {status} |
| E10 | Custom 404 page | {result} | - | - | {status} |
| E11 | Originality | {result} | {result} | {result} | {status} |
| E12 | Content depth | {result} | {result} | {result} | {status} |
| E13 | Topic coverage | {result} | {result} | {result} | {status} |
| E14 | Grammar and spelling | {result} | {result} | {result} | {status} |
| E15 | Headline consistency | {result} | {result} | {result} | {status} |
| E16 | Headline attractiveness | {result} | {result} | {result} | {status} |
| E17 | TL;DR summary | - | - | {result} | {status} |
| E18 | Table of contents | - | - | {result} | {status} |
| E19 | Conclusion section | - | - | {result} | {status} |
| E20 | Comments/engagement | - | - | {result} | {status} |
| E21 | Social sharing | - | - | {result} | {status} |
| E22 | Related content | - | - | {result} | {status} |
| E23 | Citations | - | - | {result} | {status} |
| E24 | Expert references | - | - | {result} | {status} |
| E25 | Case studies | - | - | {result} | {status} |
| E26 | Data-backed claims | - | - | {result} | {status} |
| E27 | Interactive elements | {result} | {result} | {result} | {status} |
| E28 | UGC content | - | - | {result} | {status} |
| E29 | Awards/certifications | {result} | - | - | {status} |
| E30 | HTTPS trust signal | {result} | {result} | {result} | {status} |
| E31 | Payment security | {result} | - | - | {status} |
| E32 | Refund policy | {result} | - | - | {status} |
| E33 | Ad disclosure | - | - | {result} | {status} |

---

## Appendix

### A. Analysis Metadata

| Page Type | URL | Crawl Time |
|-----------|-----|------------|
| Homepage | {url} | {timestamp} |
| Key Business Page | {url} | {timestamp} |
| Article Page | {url} | {timestamp} |

### B. Site Classification Result (v1.4.1)

| Item | Value |
|------|-------|
| Top-1 Type | {site_type_top1} |
| Top-2 Type | {site_type_top2} |
| Confidence (Top-1) | {site_type_confidence} |
| Confirmation Action | {type_confirmation_action} |
| Method | Title + URL + Nav |
| Title Signals | {title_signals} |
| URL Signals | {url_signals} |
| Nav Signals | {nav_signals} |
| Page Selection Source | {selection_source} |
| Fallback Path | {fallback_path} |

---

**SEO Audit Skill** | [GitHub](https://github.com/wonfull888/seo-audit) | Developer: [x.com/wonfull888](https://x.com/wonfull888)
```

## Status Legend

| Symbol | Meaning | Usage |
|--------|---------|-------|
| 🟢 | Excellent / Pass | Score >= 90 or fully compliant |
| 🟡 | Needs Improvement | Score 70-89 or partially compliant |
| 🔴 | Critical Issue | Score < 70 or non-compliant |
| ✓ | Check passed | Single check passed |
| ✗ | Check failed | Single check failed |
| - | Not applicable | Check not applicable to this page |
