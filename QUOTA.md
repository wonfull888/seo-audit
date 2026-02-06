# PageSpeed API 免费额度说明

## 免费配额

Google PageSpeed Insights API 提供 **每天 25,000 次免费请求**。

来源：[Stack Overflow - PageSpeed Insights API limits](https://stackoverflow.com/questions/37122041/pagespeed-insights-api-limits)

> "I've logged into my Google Developers Console and I can see that I have a quota of **25,000 requests a day**."

---

## 请求计算

每次完整诊断需要调用 PageSpeed API 多次：

```
每个 URL 的 API 调用:
├─ 移动端: 1 次
└─ 桌面端: 1 次
小计: 2 次/URL

3 个页面的总调用:
├─ 首页: 2 次
├─ 分类页: 2 次
└─ 文章页: 2 次
总计: 6 次/网站
```

---

## 使用场景计算

### 场景 1：个人博客

```
频率: 每天诊断 1 个网站
每次调用: 6 次
每月调用: 6 × 30 = 180 次
可用时长: 25,000 / 180 ≈ 4,166 天 ≈ 11 年

✅ 结论：免费额度完全够用
```

### 场景 2：小型工作室

```
频率: 每天诊断 10 个客户网站
每次调用: 6 × 10 = 60 次
每月调用: 60 × 30 = 1,800 次
可用时长: 25,000 / 1,800 ≈ 416 天 ≈ 14 个月

✅ 结论：免费额度足够
```

### 场景 3：SEO 代理

```
频率: 每天诊断 100 个客户网站
每次调用: 6 × 100 = 600 次
每月调用: 600 × 30 = 18,000 次
可用时长: 25,000 / 18,000 ≈ 41 天 ≈ 1.5 个月

⚠️ 结论：需要监控配额或申请提升
```

---

## 配额监控

### 查看当前配额

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 进入 "APIs & Services" → "Credentials"
3. 选择你的 API Key
4. 查看 "Quotas" 标签页

### 配额提升

如果超出免费配额，可以：

1. 在 Google Cloud Console 中申请提升配额
2. 可能需要提供：
   - 使用场景说明
   - 预计日调用次数
   - 商业信息（如适用）

> 注意：提升配额可能产生费用，具体取决于 Google 的定价政策

---

## 优化建议

### 减少不必要请求

```bash
# ❌ 错误：重复诊断
对 https://example.com 进行 SEO 诊断
# 10 分钟后
对 https://example.com 进行 SEO 诊断  # 浪费 6 次调用

# ✅ 正确：缓存结果
# 保存报告，避免重复调用
```

### 批量诊断策略

```bash
# 如果需要诊断多个网站，可以批量操作
# 示例：诊断 10 个网站
for site in site1.com site2.com site3.com; do
  echo "诊断 $site..."
  # 调用 SEO Audit
done
# 总计: 10 × 6 = 60 次调用
```

---

## 常见问题

### Q: 超出配额会怎样？

A: API 会返回 429 (Too Many Requests) 错误，Skill 会提示配额已用完。

### Q: 配额会重置吗？

A: 是的，配额每天 UTC 00:00 重置。

### Q: 可以申请更高配额吗？

A: 可以，在 Google Cloud Console 的 "Quotas" 页面申请提升。

### Q: 有付费选项吗？

A: Google PageSpeed Insights API 主要提供免费配额，超出后可申请提升，具体费用需咨询 Google Cloud。

---

## 安全使用建议

1. **监控使用量** - 定期检查 Google Cloud Console 的配额使用情况
2. **缓存结果** - 避免对相同 URL 重复调用
3. **批量操作** - 一次性诊断多个网站，减少零散调用
4. **合理安排时间** - 将诊断安排在配额充足的时间段

---

## 链接

- [Google Cloud Console - Quotas](https://console.cloud.google.com/apis/api/pagespeedonline.googleapis.com/quotas)
- [PageSpeed Insights API 文档](https://developers.google.com/speed/docs/insights/v5/get-started)
- [Stack Overflow 讨论](https://stackoverflow.com/questions/37122041/pagespeed-insights-api-limits)
