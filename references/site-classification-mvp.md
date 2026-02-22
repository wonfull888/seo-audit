# Site Classification Rules (v1.4.0 MVP)

## Goal

Classify site type with a lightweight, explainable method, then select high-value pages for SEO diagnosis.

## Type System (7+1)

1. Corporate
2. E-commerce
3. Content
4. Tool/SaaS
5. Community
6. Portal
7. Single-Page Site
8. Hybrid/Unknown

## Signals and Weights

- `Title` (homepage title keywords): high priority
- `URL` (sitemap/homepage links): medium priority

```text
score(type) = 0.7 * TitleScore + 0.3 * URLScore
```

## MVP Decision Rules

- Return Top-1 type only.
- If the best score is below threshold, return `Hybrid/Unknown`.
- Never block audit flow due to classification uncertainty.

## Keyword Hints (Initial)

- Corporate: company, group, services, about, case studies
- E-commerce: shop, store, product, cart, checkout, buy
- Content: blog, article, news, insights, post
- Tool/SaaS: features, pricing, solutions, integrations, trial
- Community: forum, topic, thread, discussion, community
- Portal: channel, headline, special, hot news
- Single-Page: very few paths, anchor-heavy navigation, conversion-focused title

## Dynamic Page Selection (MVP)

Always collect exactly 3 pages:

1. Homepage
2. Key business page (by type)
3. Article page (**mandatory**)

If article page is not directly discoverable, record it as unresolved and continue audit via fallback (fail-safe).

> Note: `Nav`-based signal and Top-2 confidence output are deferred to v1.4.1.

## Fallback Path

1. Use sitemap when available.
2. If sitemap is unavailable, use homepage links and depth heuristic.
3. If classification fails, run `Hybrid/Unknown` strategy and proceed.
