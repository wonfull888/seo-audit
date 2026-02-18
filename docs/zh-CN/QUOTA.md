# PageSpeed API 免费额度说明

**语言**: [English](../en/QUOTA.md) | [简体中文](QUOTA.md)

## 免费配额

Google PageSpeed Insights API 提供 **每天 25,000 次免费请求**。

## 调用计算

单个网站完整诊断的性能调用量：

- 3 个页面（首页、分类页、文章页）
- 每个页面 2 次（移动端 + 桌面端）
- 合计：`3 x 2 = 6 次/网站`

## 常见场景估算

| 场景 | 日调用量 | 说明 |
|------|----------|------|
| 每天 1 个网站 | 6 次 | 额度非常充足 |
| 每天 10 个网站 | 60 次 | 额度充足 |
| 每天 100 个网站 | 600 次 | 需监控配额 |

## 配额监控

1. 打开 [Google Cloud Console](https://console.cloud.google.com/)
2. 进入 APIs & Services
3. 查看 PageSpeed Insights API 的 Quotas 页面

## 优化建议

- 缓存已完成报告，减少重复请求
- 批量执行时控制频率
- 优先对高价值页面执行完整模式

## 参考链接

- [Google Cloud Console Quotas](https://console.cloud.google.com/apis/api/pagespeedonline.googleapis.com/quotas)
- [PageSpeed API 文档](https://developers.google.com/speed/docs/insights/v5/get-started)
