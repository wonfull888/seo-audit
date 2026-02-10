# 内容分发优化检查项 (2 项)

内容分发优化确保内容在社交媒体平台获得最佳展示效果。

---

## 1. 社交媒体元标签完整性

### CD1 多平台社交标签覆盖

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析社交平台特定标签 |
| 对应信号 | 跨平台分享展示 |
| 评分标准 | 覆盖主流平台🟢 / 仅OG+Twitter🟡 / 不完整🔴 |

**原理**: 不同社交平台有特定的元标签偏好,完整覆盖能确保内容在各平台都有良好展示。

**检查平台:**
- Facebook/LinkedIn: Open Graph
- Twitter/X: Twitter Cards  
- Pinterest: `pinterest:description`
- WhatsApp: 通常使用 OG 标签

**最佳实践:**
```html
<!-- Open Graph (Facebook, LinkedIn) -->
<meta property="og:title" content="...">
<meta property="og:image" content="...">
<meta property="og:description" content="...">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="...">

<!-- Pinterest -->
<meta name="pinterest:description" content="...">
```

---

## 2. 内容可分享性指标

### CD2 标题情感化和吸引力

| 属性 | 值 |
|------|-----|
| 执行方式 | AI 分析Title和H1的情感元素 |
| 对应信号 | 社交分享率预测 |
| 评分标准 | 包含数字/疑问/情感词🟢 / 平淡陈述🟡 |

**原理**: 包含数字、疑问句、情感词的标题在社交媒体上分享率更高。

**高分享率元素:**
1. **数字**: "7个方法"、"提高3倍"
2. **疑问句**: "为什么..."、"如何..."
3. **情感词**: "惊人"、"必知"、"秘密"
4. **时效性**: "2026年"、"最新"
5. **实用性**: "指南"、"清单"、"工具"

**好的标题示例:**
- "7个被忽视的SEO技巧(2026年更新)"
- "如何在30天内将自然流量提高200%"
- "揭秘Google排名算法的5个真相"

**差的标题示例:**
- "SEO优化方法"
- "关于网站排名"

---

## 检查项汇总

| ID | 检查项 | 评分标准 |
|----|--------|----------|
| CD1 | 多平台社交标签 | 覆盖主流🟢 |
| CD2 | 标题吸引力 | 包含吸引元素🟢 |
