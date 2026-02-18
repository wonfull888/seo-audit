# PageSpeed API Quota Guide

**Languages**: [English](QUOTA.md) | [简体中文](../zh-CN/QUOTA.md)

## Free Quota

Google PageSpeed Insights API provides **25,000 free requests per day**.

## Request Formula

Performance calls per full-site audit:

- 3 representative pages (home, category, article)
- 2 strategies per page (mobile + desktop)
- Total: `3 x 2 = 6 requests/site`

## Typical Usage Scenarios

| Scenario | Daily requests | Notes |
|----------|----------------|------|
| 1 site/day | 6 | More than enough |
| 10 sites/day | 60 | Comfortable |
| 100 sites/day | 600 | Monitor quota closely |

## Monitor Quota

1. Open [Google Cloud Console](https://console.cloud.google.com/)
2. Go to APIs & Services
3. Open PageSpeed Insights API Quotas

## Optimization Tips

- Cache completed reports to avoid duplicate calls
- Throttle large batch runs
- Use full mode on high-priority pages first

## References

- [Google Cloud Console Quotas](https://console.cloud.google.com/apis/api/pagespeedonline.googleapis.com/quotas)
- [PageSpeed API Docs](https://developers.google.com/speed/docs/insights/v5/get-started)
