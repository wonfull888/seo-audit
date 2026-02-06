---
name: seo-audit
version: 1.0.0
description: |
  SEO 诊断专家，基于 Google Content Warehouse 泄露信号设计的 73 项检查清单。
  触发词：SEO审计、SEO诊断、网站SEO检查、为什么排名不好、技术SEO检查、页面SEO、E-E-A-T检查、内容质量分析。
  输入一个网址，自动执行技术SEO（25项）、页面元素（20项）、内容质量与E-E-A-T（28项）三维度诊断，生成详细报告和优化建议。
---

# SEO Audit Skill

基于 Google Content Warehouse 泄露文档设计的证据驱动型 SEO 诊断工具。

## 快速开始

```
/seo-audit https://example.com           # 中文报告（默认）
/seo-audit https://example.com --en      # 英文报告
```

## 工作流程

```
用户输入网址
    ↓
1. 页面识别
   ├─ 尝试获取 /sitemap.xml
   ├─ 成功 → 解析 URL 结构
   └─ 失败 → 从首页链接启发式识别
    ↓
2. 选择 3 个代表页面
   ├─ 首页: /
   ├─ 分类页: 第一层路径（如 /blog, /products）
   └─ 文章页: 最深层路径
    ↓
3. 数据采集（并行）
   ├─ curl: robots.txt, HTTP headers
   ├─ WebFetch: 3 个页面 HTML
   └─ PageSpeed API: 3 个 URL（移动端 + 桌面端）
    ↓
4. 三维度分析
   ├─ 技术 SEO（25 项）→ references/technical-seo.md
   ├─ 页面元素（20 项）→ references/on-page-elements.md
   └─ 内容质量与 E-E-A-T（28 项）→ references/content-eeat.md
    ↓
5. 生成报告
   ├─ 综合评分（0-100）
   ├─ 各维度评分
   ├─ 问题清单（P0/P1/P2 优先级）
   └─ 优化建议
```

## 检查项概览

| 维度 | 检查项数 | 权重 | 详情 |
|------|----------|------|------|
| 技术 SEO | 25 项 | 30% | [technical-seo.md](references/technical-seo.md) |
| 页面元素 | 20 项 | 20% | [on-page-elements.md](references/on-page-elements.md) |
| 内容质量与 E-E-A-T | 28 项 | 50% | [content-eeat.md](references/content-eeat.md) |
| **总计** | **73 项** | **100%** | |

## 评分系统

→ 详见 [references/scoring-system.md](references/scoring-system.md)

### 快速参考

| 状态 | 含义 | 分数范围 |
|------|------|----------|
| 🟢 | 优秀 | ≥90 |
| 🟡 | 需改进 | 70-89 |
| 🔴 | 严重问题 | <70 |

## 报告模板

→ 详见 [references/report-template.md](references/report-template.md)

## 执行工具

| 工具 | 用途 | 示例 |
|------|------|------|
| `curl` | HTTP 请求 | `curl -I https://example.com` |
| `WebFetch` | 获取页面 HTML | AI 内置工具 |
| PageSpeed API | 性能分析 | 可选（推荐配置以获取完整报告） |

### API Key 配置（可选但推荐）

**为什么要配置 API Key？**
- ✅ 完整 73 项检查（包含 Core Web Vitals）
- ✅ 技术评分更准确（30% 权重）
- ✅ 性能优化建议更详细

**不配置也能用！**
- ⚠️ 65 项检查（跳过 Core Web Vitals）
- ⚠️ 技术评分降权（25% 权重）
- ⚠️ 报告会标注性能数据缺失

#### 配置方式

```bash
export PAGE_SPEED_API_KEY="your_api_key_here"
```

#### 获取免费 API Key

Google PageSpeed Insights API 提供 **每天 25,000 次免费请求**，个人使用完全够用！

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建项目或选择现有项目
3. 启用 PageSpeed Insights API
4. 创建 API Key

详细说明：[API_KEY_SETUP.md](API_KEY_SETUP.md)

### PageSpeed API 调用

⚠️ **重要**: PageSpeed API 需要有效的 API Key。请先设置环境变量：

```bash
export PAGE_SPEED_API_KEY="your_api_key_here"
```

详细配置说明：[API_KEY_SETUP.md](API_KEY_SETUP.md)

```bash
# 移动端
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${url}&strategy=mobile&key=${PAGE_SPEED_API_KEY}"

# 桌面端
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${url}&strategy=desktop&key=${PAGE_SPEED_API_KEY}"
```

## 检查标准

| 项目 | 标准 |
|------|------|
| Title 长度 | 50-60 字符 |
| Meta Description 长度 | 150-160 字符 |
| 首页最低字数 | 500 字 |
| 分类页最低字数 | 300 字 |
| 文章页最低字数 | 1000 字 |
| 内部链接 | ≥3 个/页 |
| URL 长度 | ≤100 字符 |

## 报告语言

- **默认**: 中文
- **可选**: 英文（用户在指令中说明即可，如 `--en` 或 "英文报告"）

## 参考资料

- [AI 写作特征检测](references/ai-writing-detection.md) - Em dash、高频词、AI 短语模式
- [示例报告](assets/example-report.md) - 完整报告示例

## 版本历史

- **v1.0.0** (2026-02-06): 首个完整版本，73 项检查
