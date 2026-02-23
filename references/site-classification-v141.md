# Site Classification Rules (v1.4.1)

## Goal

Improve classification accuracy and explainability over v1.4.0 by adding Nav signals, Top-2 output, and confidence-aware interaction.

## Type System (7+1)

1. Corporate
2. E-commerce
3. Content
4. Tool/SaaS
5. Community
6. Portal
7. Single-Page Site
8. Hybrid/Unknown

## Signals

- `Title`: homepage title keywords
- `URL`: sitemap/homepage discovered paths
- `Nav`: navigation labels and primary CTA anchors

## Scoring Formula

```text
score(type) = w_title * TitleScore + w_url * URLScore + w_nav * NavScore
default weights: w_title=0.5, w_url=0.3, w_nav=0.2
```

Weights must be configurable and not hardcoded in business logic.

## Output Requirements

- Return Top-2 candidates (`top1`, `top2`)
- Return confidence of Top-1 (`0.0-1.0`)
- Return evidence bundle:
  - Title hits
  - URL pattern hits
  - Nav keyword hits

## Confidence Thresholds

- High: `>= 0.70`
- Medium: `0.45-0.69`
- Low: `< 0.45`

## Confirmation Strategy

- High confidence: use Top-1 directly
- Medium/Low confidence: show quick confirmation with Top-2 options
- No response: default to Top-1 and continue (non-blocking)

## Dynamic Page Selection

Always audit exactly 3 pages:

1. Homepage
2. Key business page (by selected type)
3. Article page (**mandatory**)

## Article Page Secondary Search (v1.4.1)

If article page is not discovered in first pass, search content-like paths:

- `/blog`
- `/news`
- `/article`
- `/post`
- `/insights`
- `/docs`

If still not found, mark unresolved and continue via fail-safe.

## Fallback Path

1. Use sitemap if available
2. If unavailable, use homepage links + depth heuristic
3. If classification remains ambiguous, use `Hybrid/Unknown`

## Report Appendix Fields (Required)

- Top-1 type
- Top-2 type
- Top-1 confidence
- Confirmation action
- Method (`Title + URL + Nav`)
- Title/URL/Nav signals
- Selection source
- Fallback path
