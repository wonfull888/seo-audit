# 使用指南

## 概述

SEO Audit Skill 支持两种运行模式：

1. **完整模式**（推荐）- 需要 PageSpeed API Key
2. **基础模式** - 无需 API Key，功能受限

---

## 模式 1：完整模式（推荐）

### 优势

- ✅ 完整 73 项检查
- ✅ 包含 Core Web Vitals（LCP, FCP, CLS, INP, TBT, TTFB）
- ✅ 技术评分更准确（30% 权重）
- ✅ 详细的性能优化建议

### 配置步骤

```bash
# 1. 设置环境变量
export PAGE_SPEED_API_KEY="your_api_key_here"

# 2. 验证配置
echo $PAGE_SPEED_API_KEY

# 3. 开始使用
# 在 Claude Code 中输入：
对 https://example.com 进行 SEO 诊断
```

### 获取 API Key

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建项目或选择现有项目
3. 搜索并启用 **PageSpeed Insights API**
4. 点击 "Credentials" → "Create Credentials" → "API Key"
5. 复制生成的 API Key

> **免费额度**: 每天 25,000 次请求，个人使用完全够用
>
> 📊 详细计算：[QUOTA.md](QUOTA.md)

---

## 模式 2：基础模式（无需配置）

### 特点

- ✅ 无需任何配置，直接使用
- ✅ 65 项检查（跳过 Core Web Vitals）
- ⚠️ 技术 SEO 权重降为 25%
- ⚠️ E-E-A-T 权重提升至 55%
- ⚠️ 报告会标注性能数据缺失

### 使用方法

```bash
# 直接在 Claude Code 中输入，无需任何配置：
对 https://example.com 进行 SEO 诊断
```

### 输出示例

```
⚠️  检测到未配置 PageSpeed API Key
运行模式：基础模式（65 项检查）
- Core Web Vitals 检查已跳过
- 技术权重：25%，E-E-A-T 权重：55%
- 性能数据：不可用

如需完整诊断，请配置 API Key：
export PAGE_SPEED_API_KEY="your_key_here"
详见：API_KEY_SETUP.md

=========================================

# SEO 诊断报告 - example.com

📊 综合评分：68/100 🟡（基础模式）

| 维度 | 得分 | 状态 | 检查项数 |
|------|------|------|----------|
| 技术 SEO | 78/100 | 🟢 | 17 项 |
| 页面元素 | 72/100 | 🟡 | 20 项 |
| 内容质量与 E-E-A-T | 62/100 | 🟡 | 28 项 |

⚠️  注意：Core Web Vitals 数据缺失，技术 SEO 权重已调整
...
```

---

## 检查项对比

| 类别 | 完整模式 | 基础模式 |
|------|----------|----------|
| **可发现性与索引** | 8 项 | 8 项 ✓ |
| **Core Web Vitals** | 8 项 | 0 项 ❌ |
| **安全性与基础设施** | 4 项 | 4 项 ✓ |
| **结构化数据** | 5 项 | 5 项 ✓ |
| **页面元素** | 20 项 | 20 项 ✓ |
| **内容质量与 E-E-A-T** | 28 项 | 28 项 ✓ |
| **总计** | **73 项** | **65 项** |

### Core Web Vitals 详细对比

| 指标 | 完整模式 | 基础模式 |
|------|----------|----------|
| PageSpeed 移动端评分 | ✅ | ❌ |
| PageSpeed 桌面端评分 | ✅ | ❌ |
| LCP (最大内容绘制) | ✅ | ❌ |
| FCP (首次内容绘制) | ✅ | ❌ |
| CLS (累积布局偏移) | ✅ | ❌ |
| INP (交互延迟) | ✅ | ❌ |
| TBT (总阻塞时间) | ✅ | ❌ |
| TTFB (首字节时间) | ✅ | ❌ |

---

## 触发词

以下任一关键词都会触发 SEO Audit Skill：

```
SEO审计
SEO诊断
网站SEO检查
为什么排名不好
技术SEO检查
页面SEO
E-E-A-T检查
内容质量分析
```

### 使用示例

```
# 中文报告（默认）
对 https://example.com 进行 SEO 诊断

# 英文报告
对 https://example.com 进行 SEO 诊断，生成英文报告

# 或者直接用触发词
SEO审计 https://example.com
```

---

## 输出格式

### 报告结构

```
# SEO 诊断报告 - {domain}

📊 综合评分：{score}/100 {status}

| 维度 | 得分 | 状态 |
|------|------|------|
| 技术 SEO | {tech_score}/100 | {status} |
| 页面元素 | {onpage_score}/100 | {status} |
| 内容质量与 E-E-A-T | {eeat_score}/100 | {status} |

🚨 优先级行动清单
├─ P0 - 必须立即修复
├─ P1 - 尽快修复
└─ P2 - 计划优化

1. 技术 SEO 检查结果
2. 页面元素检查结果
3. 内容质量与 E-E-A-T 检查结果

4. 优化建议
```

---

## 常见问题

### Q: 不配置 API Key 会有什么影响？

A: 会跳过 8 项 Core Web Vitals 检查，技术 SEO 权重从 30% 降至 25%。但其他 65 项检查仍可正常进行。

### Q: 免费额度够用吗？

A: 完全够用！每天 25,000 次请求：
- 每天诊断 1 个网站 ≈ 可用 11 年
- 每天诊断 10 个网站 ≈ 可用 14 个月

### Q: 如何从基础模式升级到完整模式？

A: 只需设置环境变量，重新诊断即可：
```bash
export PAGE_SPEED_API_KEY="your_key_here"
# 然后重新运行诊断
```

### Q: 临时测试可以用别人的 API Key 吗？

A: 可以，但不建议。临时设置：
```bash
PAGE_SPEED_API_KEY="temporary_key" 对 https://example.com 进行 SEO 诊断
```

### Q: API Key 会被提交到 Git 吗？

A: 不会！`.gitignore` 已配置忽略 `.env` 文件，请确保使用环境变量存储 Key。

---

## 技术细节

### 评分权重调整算法

```python
# 完整模式
tech_weight = 0.30
onpage_weight = 0.20
eeat_weight = 0.50

# 基础模式（无 API Key）
tech_weight = 0.25  # 因为缺少 8 项 Core Web Vitals
onpage_weight = 0.20
eeat_weight = 0.55  # 提升权重以保持总分平衡
```

### 数据源对比

| 数据源 | 完整模式 | 基础模式 |
|--------|----------|----------|
| robots.txt | ✅ | ✅ |
| sitemap.xml | ✅ | ✅ |
| HTTP headers | ✅ | ✅ |
| PageSpeed API | ✅ (6 次调用) | ❌ |
| HTML 页面 | ✅ (3 个) | ✅ (3 个) |

---

## 支持

如遇问题，请查看：
- [API_KEY_SETUP.md](API_KEY_SETUP.md) - API Key 配置
- [README.md](README.md) - 项目介绍
- [CHANGELOG.md](CHANGELOG.md) - 版本历史
