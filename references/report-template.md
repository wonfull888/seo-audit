# 报告模板

## 报告结构

```markdown
# SEO 诊断报告 - {domain}

**生成时间**: {YYYY-MM-DD HH:MM:SS}
**分析页面**: 首页、分类页、文章页

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

## 1. 技术 SEO 检查结果

### 1.1 可发现性与索引

| ID | 检查项 | 首页 | 分类页 | 文章页 | 状态 |
|----|--------|------|--------|--------|------|
| T1.1 | robots.txt | {result} | - | - | {status} |
| T1.2 | sitemap.xml | {result} | - | - | {status} |
| T1.3 | HTTP 状态码 | {result} | {result} | {result} | {status} |
| T1.4 | noindex 检查 | {result} | {result} | {result} | {status} |
| T1.5 | Canonical 标签 | {result} | {result} | {result} | {status} |
| T1.6 | HTTPS 重定向 | {result} | - | - | {status} |
| T1.7 | www 一致性 | {result} | - | - | {status} |
| T1.8 | 重定向链 | {result} | {result} | {result} | {status} |

### 1.2 技术性能 Core Web Vitals

| ID | 指标 | 首页 | 分类页 | 文章页 | 标准 | 状态 |
|----|------|------|--------|--------|------|------|
| T2.1 | PageSpeed 移动端 | {score} | {score} | {score} | ≥90 | {status} |
| T2.2 | PageSpeed 桌面端 | {score} | {score} | {score} | ≥90 | {status} |
| T2.3 | LCP | {value} | {value} | {value} | <2.5s | {status} |
| T2.4 | FCP | {value} | {value} | {value} | <1.8s | {status} |
| T2.5 | CLS | {value} | {value} | {value} | <0.1 | {status} |
| T2.6 | INP | {value} | {value} | {value} | <200ms | {status} |
| T2.7 | TBT | {value} | {value} | {value} | <200ms | {status} |
| T2.8 | TTFB | {value} | {value} | {value} | <800ms | {status} |

### 1.3 安全性

| ID | 检查项 | 结果 | 状态 |
|----|--------|------|------|
| T3.1 | HTTPS | {result} | {status} |
| T3.2 | SSL 证书 | {result} | {status} |
| T3.3 | 混合内容 | {result} | {status} |
| T3.4 | viewport | {result} | {status} |

### 1.4 结构化数据

| ID | 检查项 | 首页 | 分类页 | 文章页 | 状态 |
|----|--------|------|--------|--------|------|
| T4.1 | JSON-LD 存在 | {result} | {result} | {result} | {status} |
| T4.2 | Organization | {result} | - | - | {status} |
| T4.3 | Article | - | - | {result} | {status} |
| T4.4 | Breadcrumb | {result} | {result} | {result} | {status} |
| T4.5 | Author | - | - | {result} | {status} |

---

## 2. 页面元素检查结果

### 2.1 Title 标签

| 页面 | Title 内容 | 长度 | 关键词 | 状态 |
|------|-----------|------|--------|------|
| 首页 | {title} | {len} | {has_kw} | {status} |
| 分类页 | {title} | {len} | {has_kw} | {status} |
| 文章页 | {title} | {len} | {has_kw} | {status} |

### 2.2 Meta Description

| 页面 | 描述内容 | 长度 | 状态 |
|------|----------|------|------|
| 首页 | {desc} | {len} | {status} |
| 分类页 | {desc} | {len} | {status} |
| 文章页 | {desc} | {len} | {status} |

### 2.3 H 标签结构

#### 首页
```
{h_structure}
```

#### 分类页
```
{h_structure}
```

#### 文章页
```
{h_structure}
```

### 2.4 图片优化

| 页面 | 图片总数 | 有 Alt | 缺失 Alt | Alt 完整率 | 状态 |
|------|----------|--------|----------|------------|------|
| 首页 | {total} | {with_alt} | {without_alt} | {rate}% | {status} |
| 分类页 | {total} | {with_alt} | {without_alt} | {rate}% | {status} |
| 文章页 | {total} | {with_alt} | {without_alt} | {rate}% | {status} |

### 2.5 社交标签

| 页面 | Open Graph | Twitter Card | 状态 |
|------|------------|--------------|------|
| 首页 | {og_status} | {tw_status} | {status} |
| 分类页 | {og_status} | {tw_status} | {status} |
| 文章页 | {og_status} | {tw_status} | {status} |

---

## 3. 内容质量与 E-E-A-T 检查结果

### 3.1 Trust（信任度）

| ID | 检查项 | 结果 | 状态 |
|----|--------|------|------|
| E1.1 | 品牌信息完整性 | {result} | {status} |
| E1.2 | 联系方式可见 | {result} | {status} |
| E1.3 | 隐私政策 | {result} | {status} |
| E1.4 | 内容准确性 | {result} | {status} |
| E1.5 | 权威来源引用 | {result} | {status} |
| E1.6 | YMYL 免责声明 | {result} | {status} |
| E1.7 | 广告干扰 | {result} | {status} |
| E1.8 | 弹窗干扰 | {result} | {status} |

### 3.2 Experience（经验）

| ID | 检查项 | 首页 | 分类页 | 文章页 | 状态 |
|----|--------|------|--------|--------|------|
| E2.1 | 原创媒体 | {result} | {result} | {result} | {status} |
| E2.2 | 第一人称经验 | - | - | {result} | {status} |
| E2.3 | 独家数据 | - | - | {result} | {status} |
| E2.4 | 信息增益 | - | - | {result} | {status} |
| E2.5 | 努力程度 | {result} | {result} | {result} | {status} |
| E2.6 | 更新日期 | {result} | {result} | {result} | {status} |
| E2.7 | AI 写作检测 | - | - | {result} | {status} |

### 3.3 Expertise（专业度）

| ID | 检查项 | 结果 | 状态 |
|----|--------|------|------|
| E3.1 | 作者署名 | {result} | {status} |
| E3.2 | 作者简介 | {result} | {status} |
| E3.3 | Author Schema | {result} | {status} |
| E3.4 | 领域匹配 | {result} | {status} |
| E3.5 | 主题垂直度 | {result} | {status} |
| E3.6 | 语义全面性 | {result} | {status} |
| E3.7 | 术语准确 | {result} | {status} |

### 3.4 Authoritativeness（权威性）

| ID | 检查项 | 结果 | 状态 |
|----|--------|------|------|
| E4.1 | 导航清晰 | {result} | {status} |
| E4.2 | 内链结构 | {result} | {status} |
| E4.3 | 外部引用 | {result} | {status} |
| E4.4 | 社交证明 | {result} | {status} |
| E4.5 | 品牌一致 | {result} | {status} |
| E4.6 | About 页面 | {result} | {status} |

---

## 4. 优化建议

### 4.1 技术 SEO 优化

{tech_suggestions}

### 4.2 页面元素优化

{onpage_suggestions}

### 4.3 内容与 E-E-A-T 优化

{eeat_suggestions}

---

## 附录

### A. 分析页面信息

| 页面类型 | URL | 爬取时间 |
|----------|-----|----------|
| 首页 | {url} | {timestamp} |
| 分类页 | {url} | {timestamp} |
| 文章页 | {url} | {timestamp} |

### B. 数据来源

- PageSpeed API 调用: 6 次（3 个 URL × 移动端/桌面端）
- HTML 页面: 3 个
- robots.txt: 1 个
- sitemap.xml: 1 个

### C. 报告信息

- 报告版本: v1.0.0
- 生成工具: SEO Audit Skill
- 生成时间: {timestamp}

---

**报告结束**
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
