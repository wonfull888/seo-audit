# 报告模板

## 报告结构

```markdown
# SEO 诊断报告 - {domain}

**生成时间**: {YYYY-MM-DD HH:MM:SS}
**分析页面**: 首页、关键业务页、文章页

---

## 🧭 诊断总览

{executive_summary_300_800_chars}

> 必须包含：网站类型、诊断页面范围、总分与总体判断、问题最严重维度、最急需修复事项（P0）。

**本次抓取页面（必须列出 URL）**

| 页面角色 | URL |
|----------|-----|
| 首页 | {homepage_url} |
| 关键业务页 | {business_page_url} |
| 文章页 | {article_page_url} |

---

## 📊 综合评分

### 总分：{score}/100 {status_emoji}

| 维度 | 得分 | 状态 |
|------|------|------|
| 技术 SEO | {tech_score}/100 | {tech_status} |
| 页面元素 | {onpage_score}/100 | {onpage_status} |
| 内容质量与 E-E-A-T | {eeat_score}/100 | {eeat_status} |

### E-E-A-T 细分

| 维度 | 得分 | 状态 |
|------|------|------|
| Trust（信任度） | {trust_score}/100 | {trust_status} |
| Experience（经验） | {exp_score}/100 | {exp_status} |
| Expertise（专业度） | {expertise_score}/100 | {expertise_status} |
| Authoritativeness（权威性） | {auth_score}/100 | {auth_status} |

---

## 🚨 优先级行动清单

### P0 - 必须立即修复

| 问题 | 页面 | 当前状态 | 建议 |
|------|------|----------|------|
| {issue} | {page} | {current} | {suggestion} |

### P1 - 尽快修复

| 问题 | 页面 | 当前状态 | 建议 |
|------|------|----------|------|
| {issue} | {page} | {current} | {suggestion} |

### P2 - 计划优化

| 问题 | 页面 | 当前状态 | 建议 |
|------|------|----------|------|
| {issue} | {page} | {current} | {suggestion} |

---

## 4. 优化建议

### 4.1 技术 SEO 优化建议

{tech_suggestions}

### 4.2 页面元素优化建议

{onpage_suggestions}

### 4.3 内容与 E-E-A-T 优化建议

{eeat_suggestions}

---

## 📝 详细检查清单 (全量 92 项)

### 1. 技术 SEO 检查结果 (29 项)

| ID | 检查项 | 首页 | 关键业务页 | 文章页 | 状态 |
|----|--------|------|--------|--------|------|
| T1.1 | robots.txt | {result} | - | - | {status} |
| T1.2 | sitemap.xml | {result} | - | - | {status} |
| T1.3 | HTTP 状态码 | {result} | {result} | {result} | {status} |
| T1.4 | noindex 检查 | {result} | {result} | {result} | {status} |
| T1.5 | Canonical 标签 | {result} | {result} | {result} | {status} |
| T1.6 | HTTPS 重定向 | {result} | - | - | {status} |
| T1.7 | www 一致性 | {result} | - | - | {status} |
| T1.8 | 重定向链 | {result} | {result} | {result} | {status} |
| T2.1 | PageSpeed 移动端 | {score} | {score} | {score} | {status} |
| T2.2 | PageSpeed 桌面端 | {score} | {score} | {score} | {status} |
| T2.3 | LCP (最大内容绘制) | {value} | {value} | {value} | {status} |
| T2.4 | FCP (首屏绘制) | {value} | {value} | {value} | {status} |
| T2.5 | CLS (布局偏移) | {value} | {value} | {value} | {status} |
| T2.6 | INP (交互延迟) | {value} | {value} | {value} | {status} |
| T2.7 | TBT (总阻塞时间) | {value} | {value} | {value} | {status} |
| T2.8 | TTFB (首字节时间) | {value} | {value} | {value} | {status} |
| T3.1 | HTTPS | {result} | {status} |
| T3.2 | SSL 证书 | {result} | {status} |
| T3.3 | 混合内容 | {result} | {status} |
| T3.4 | viewport | {result} | {status} |
| T4.1 | JSON-LD 存在 | {result} | {result} | {result} | {status} |
| T4.2 | Organization | {result} | - | - | {status} |
| T4.3 | Article Schema | - | - | {result} | {status} |
| T4.4 | Breadcrumb Schema | {result} | {result} | {result} | {status} |
| T4.5 | Author Schema | - | - | {result} | {status} |
| T... | ... | ... | ... | ... | ... |

### 2. 页面元素检查结果 (27 项)

#### 2.1 页面数据预览

**Title & Meta Description**

| 页面 | Title | 长度 | Meta Description | 长度 |
|------|-------|------|------------------|------|
| 首页 | {title} | {len} | {desc} | {len} |
| 关键业务页 | {title} | {len} | {desc} | {len} |
| 文章页 | {title} | {len} | {desc} | {len} |

**H 标签结构**

- **首页**: {h1}
- **关键业务页**: {h1}
- **文章页**: {h1}

**关键词分布**

- **首页**: {keywords}
- **关键业务页**: {keywords}
- **文章页**: {keywords}

#### 2.2 检查结果明细

| ID | 检查项 | 首页 | 关键业务页 | 文章页 | 状态 |
|----|--------|------|--------|--------|------|
| P1 | Title 标签存在 | {result} | {result} | {result} | {status} |
| P2 | Title 长度规范 | {result} | {result} | {result} | {status} |
| P3 | Title 包含关键词 | {result} | {result} | {result} | {status} |
| P4 | Meta Desc 存在 | {result} | {result} | {result} | {status} |
| P5 | Meta Desc 长度 | {result} | {result} | {result} | {status} |
| P6 | H1 标签唯一 | {result} | {result} | {result} | {status} |
| P7 | H2-H6 层级清晰 | {result} | {result} | {result} | {status} |
| P8 | 图片 Alt 完整率 | {result} | {result} | {result} | {status} |
| P9 | 图片尺寸定义 | {result} | {result} | {result} | {status} |
| P10 | Favicon | {result} | - | - | {status} |
| P11 | Open Graph 标签 | {result} | {result} | {result} | {status} |
| P12 | Twitter Card | {result} | {result} | {result} | {status} |
| P13 | 关键词自然分布 | {result} | {result} | {result} | {status} |
| P14 | 内部链接数量 | {result} | {result} | {result} | {status} |
| P15 | 外部链接引用 | - | - | {result} | {status} |
| P16 | 锚文本描述性 | {result} | {result} | {result} | {status} |
| P17 | 列表使用 (ul/ol) | {result} | {result} | {result} | {status} |
| P18 | 强调标签 (b/strong)| {result} | {result} | {result} | {status} |
| P19 | 引用标签 (blockq) | - | - | {result} | {status} |
| P20 | 表格数据展示 | - | - | {result} | {status} |
| P21 | 多媒体丰富度 | {result} | {result} | {result} | {status} |
| P22 | 无干扰广告 | {result} | {result} | {result} | {status} |
| P23 | 无弹窗打扰 | {result} | {result} | {result} | {status} |
| P24 | 内容阅读难度 | {result} | {result} | {result} | {status} |
| P25 | 字体可读性 | {result} | {result} | {result} | {status} |
| P26 | 颜色对比度 | {result} | {result} | {result} | {status} |
| P27 | 移动端点击目标 | {result} | {result} | {result} | {status} |

### 3. 内容质量与 E-E-A-T 检查结果 (33 项)

| ID | 检查项 | 首页 | 关键业务页 | 文章页 | 状态 |
|----|--------|------|--------|--------|------|
| E1 | 作者署名 | - | - | {result} | {status} |
| E2 | 作者简介链接 | - | - | {result} | {status} |
| E3 | 内容审核机制 | - | - | {result} | {status} |
| E4 | 发布日期 | - | - | {result} | {status} |
| E5 | 更新日期 | - | - | {result} | {status} |
| E6 | 品牌介绍 (About) | {result} | - | - | {status} |
| E7 | 联系方式 | {result} | - | - | {status} |
| E8 | 隐私政策 | {result} | - | - | {status} |
| E9 | 服务条款 | {result} | - | - | {status} |
| E10 | 404 页面自定义 | {result} | - | - | {status} |
| E11 | 内容原创性 | {result} | {result} | {result} | {status} |
| E12 | 内容深度 (字数) | {result} | {result} | {result} | {status} |
| E13 | 主题覆盖全面性 | {result} | {result} | {result} | {status} |
| E14 | 语法拼写 | {result} | {result} | {result} | {status} |
| E15 | 标题一致性 | {result} | {result} | {result} | {status} |
| E16 | 标题吸引力 | {result} | {result} | {result} | {status} |
| E17 | 摘要 (TL;DR) | - | - | {result} | {status} |
| E18 | 目录导航 (ToC) | - | - | {result} | {status} |
| E19 | 结论段落 | - | - | {result} | {status} |
| E20 | 评论互动 | - | - | {result} | {status} |
| E21 | 社交分享 | - | - | {result} | {status} |
| E22 | 相关推荐 | - | - | {result} | {status} |
| E23 | 引用来源 | - | - | {result} | {status} |
| E24 | 专家引用 | - | - | {result} | {status} |
| E25 | 案例研究 | - | - | {result} | {status} |
| E26 | 数据支撑 | - | - | {result} | {status} |
| E27 | 交互元素 | {result} | {result} | {result} | {status} |
| E28 | UGC 内容 | - | - | {result} | {status} |
| E29 | 奖项/认证展示 | {result} | - | - | {status} |
| E30 | HTTPS 安全标示 | {result} | {result} | {result} | {status} |
| E31 | 支付安全 | {result} | - | - | {status} |
| E32 | 退款政策 | {result} | - | - | {status} |
| E33 | 广告声明 | - | - | {result} | {status} |

---

## 附录

### A. 分析信息

| 页面类型 | URL | 爬取时间 |
|----------|-----|----------|
| 首页 | {url} | {timestamp} |
| 关键业务页 | {url} | {timestamp} |
| 文章页 | {url} | {timestamp} |

### B. 站点分类结果（v1.4.1）

| 项目 | 值 |
|------|----|
| Top-1 类型 | {site_type_top1} |
| Top-2 类型 | {site_type_top2} |
| Top-1 置信度 | {site_type_confidence} |
| 用户确认动作 | {type_confirmation_action} |
| 判定方式 | Title + URL + Nav |
| Title 命中 | {title_signals} |
| URL 命中 | {url_signals} |
| Nav 命中 | {nav_signals} |
| 页面来源 | {selection_source} |
| 回退路径 | {fallback_path} |

---

**SEO Audit Skill** | [GitHub](https://github.com/wonfull888/seo-audit) | Developer: [x.com/wonfull888](https://x.com/wonfull888)
```

## 状态符号说明

| 符号 | 含义 | 使用场景 |
|------|------|----------|
| 🟢 | 优秀/通过 | 得分 ≥90 或完全符合标准 |
| 🟡 | 需改进 | 得分 70-89 或部分符合 |
| 🔴 | 严重问题 | 得分 <70 或不符合标准 |
| ✓ | 检查通过 | 单项检查通过 |
| ✗ | 检查失败 | 单项检查失败 |
| - | 不适用 | 该检查项不适用于此页面 |
