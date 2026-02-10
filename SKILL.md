---
name: seo-audit
version: 1.1.0
description: |
  SEO 诊断专家,基于 Google、Ahrefs、微软搜索指南设计的 92 项检查清单。
  触发词:SEO审计、SEO诊断、网站SEO检查、为什么排名不好、技术SEO检查、页面SEO、E-E-A-T检查、内容质量分析、AI搜索优化。
  输入一个网址,自动执行技术SEO(29项)、页面元素(22项)、内容质量与E-E-A-T(31项)、AI搜索(5项)、本地SEO(3项)、信任信号(2项)六维度诊断,生成详细报告和优化建议。
---

# SEO Audit Skill

基于 Google、Ahrefs、微软官方搜索指南设计的证据驱动型 SEO 诊断工具。

文档来源:
- [Google 搜索指南](https://developers.google.com/search/docs?hl=zh-cn)
- [Ahrefs 82项 SEO+AI 搜索清单](https://ahrefs.com/blog/seo-ai-search-checklist/)
- [微软 AEO & GEO 指南](https://about.ads.microsoft.com/content/dam/sites/msa-about/global/common/content-lib/pdf/from-discovery-to-influence-a-guide-to-aeo-and-geo.pdf)

## 快速开始

```
/seo-audit https://example.com           # 中文报告(默认)
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
   ├─ 分类页: 第一层路径(如 /blog, /products)
   └─ 文章页: 最深层路径
    ↓
3. 数据采集(并行)
   ├─ curl: robots.txt, HTTP headers
   ├─ WebFetch: 3 个页面 HTML
   └─ PageSpeed API: 3 个 URL(移动端 + 桌面端)
    ↓
4. 六维度分析
   ├─ 技术 SEO(29 项)→ technical-seo.md + technical-seo-enhanced.md
   ├─ 页面元素(22 项)→ on-page-elements.md + content-distribution.md
   ├─ 内容质量与 E-E-A-T(31 项)→ content-eeat.md + content-quality-enhanced.md
   ├─ AI 搜索优化(5 项)→ ai-search-optimization.md
   ├─ 本地 SEO(3 项)→ local-seo-enhanced.md
   └─ 信任信号(2 项)→ trust-signals-enhanced.md
    ↓
5. 生成报告
   ├─ 综合评分(0-100)
   ├─ 各维度评分
   ├─ 问题清单(P0/P1/P2 优先级)
   └─ 优化建议
```

## 检查项概览

| 维度 | 检查项数 | 权重 | 详情 |
|------|----------|------|------|
| 技术 SEO | 25+4 项 | 28% | [technical-seo.md](references/technical-seo.md) + [enhanced](references/technical-seo-enhanced.md) |
| 页面元素 | 20+2 项 | 18% | [on-page-elements.md](references/on-page-elements.md) + [enhanced](references/content-distribution.md) |
| 内容质量与 E-E-A-T | 28+3 项 | 42% | [content-eeat.md](references/content-eeat.md) + [enhanced](references/content-quality-enhanced.md) |
| AI 搜索优化 | 5 项 | 6% | [ai-search-optimization.md](references/ai-search-optimization.md) |
| 本地 SEO | 3 项 | 4% | [local-seo-enhanced.md](references/local-seo-enhanced.md) |
| 信任信号 | 2 项 | 2% | [trust-signals-enhanced.md](references/trust-signals-enhanced.md) |
| **总计** | **92 项** | **100%** | |

## 新增功能 (v1.1.0)

### 🎯 AI 搜索优化 (5项)
基于 Ahrefs 82项清单,新增 AI 搜索引擎优化检查:
- **TL;DR摘要检测** - AI搜索引擎偏好引用包含简洁摘要的页面
- **Answer-Oriented Writing** - 检测"先结论后支撑"的写作模式
- **可引用内容块** - 识别表格、步骤列表等AI易摘录的格式
- **FAQ Schema** - 检测FAQPage结构化数据
- **语音搜索优化** - 检测自然语言问答格式

### 🌍 本地 SEO 增强 (3项)
- **LocalBusiness Schema** - 检测本地商家结构化数据
- **Google Maps嵌入** - 检测地图嵌入提高本地相关性
- **NAP一致性** - 对比名称/地址/电话的一致性

### 🔧 技术 SEO 增强 (4项)
- **Hreflang标签** - 多语言/多地区配置检测
- **服务器渲染检测** - SSR vs CSR判断爬虫友好度
- **现代图片格式** - 检测WebP/AVIF使用提高性能
- **浏览器缓存配置** - HTTP headers缓存设置检查

### ✍️ 内容质量增强 (3项)
- **内容可扫描性** - 分析段落/句子长度和列表使用
- **术语定义** - 检测专业术语首次出现时的解释
- **多媒体丰富度** - 统计视频/音频/交互内容

### 📱 内容分发优化 (2项)
- **多平台社交标签** - 除OG/Twitter外的平台标签检测
- **标题吸引力** - 分析情感化元素提高分享率

### 🔒 信任信号增强 (2项)
- **退款保证** - 电商/SaaS网站保证政策检测
- **安全认证徽章** - 识别SSL/行业认证等信任标记

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
| PageSpeed API | 性能分析 | 可选(推荐配置以获取完整报告) |

### API Key 配置(可选但推荐)

**为什么要配置 API Key?**
- ✅ 完整 92 项检查(包含 Core Web Vitals)
- ✅ 技术评分更准确(28% 权重)
- ✅ 性能优化建议更详细

**不配置也能用!**
- ⚠️ 84 项检查(跳过 Core Web Vitals)
- ⚠️ 技术评分降权(23% 权重)
- ⚠️ 报告会标注性能数据缺失

#### 配置方式

```bash
export PAGE_SPEED_API_KEY="your_api_key_here"
```

#### 获取免费 API Key

Google PageSpeed Insights API 提供 **每天 25,000 次免费请求**,个人使用完全够用!

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建项目或选择现有项目
3. 启用 PageSpeed Insights API
4. 创建 API Key

详细说明:[API_KEY_SETUP.md](API_KEY_SETUP.md)

### PageSpeed API 调用

⚠️ **重要**: PageSpeed API 需要有效的 API Key。请先设置环境变量:

```bash
export PAGE_SPEED_API_KEY="your_api_key_here"
```

详细配置说明:[API_KEY_SETUP.md](API_KEY_SETUP.md)

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
- **可选**: 英文(用户在指令中说明即可,如 `--en` 或 "英文报告")

## 参考资料

- [AI 写作特征检测](references/ai-writing-detection.md) - Em dash、高频词、AI 短语模式
- [示例报告](assets/example-report.md) - 完整报告示例

## 版本历史

- **v1.1.0** (2026-02-10): 新增19项检查,从73项扩展到92项,增加AI搜索优化
- **v1.0.0** (2026-02-06): 首个完整版本,73 项检查
