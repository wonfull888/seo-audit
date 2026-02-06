# 页面元素检查项（20 项）

页面元素优化确保搜索引擎正确理解页面内容，并在 SERP 中获得最佳展示。

## 目录

1. [Title 标签](#1-title-标签4-项)
2. [Meta 标签](#2-meta-标签4-项)
3. [H 标签](#3-h-标签3-项)
4. [URL 结构](#4-url-结构3-项)
5. [图片优化](#5-图片优化3-项)
6. [社交分享标签](#6-社交分享标签2-项)
7. [链接结构](#7-链接结构1-项)

---

## 1. Title 标签（4 项）

### O1 Title 标签存在性

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `<title>` |
| 对应信号 | Goldmine 系统 |
| 评分标准 | 存在🟢 / 不存在🔴 |

---

### O2 Title 长度

| 属性 | 值 |
|------|-----|
| 执行方式 | 统计 `<title>` 字符数 |
| 对应信号 | SERP 展示 |
| 评分标准 | 50-60 字符🟢 / 30-50 或 60-70🟡 / <30 或 >70🔴 |

**说明：**
- 过短：浪费展示机会
- 过长：会被截断，关键信息可能丢失
- 中文按字符计算（约 25-30 个汉字）

---

### O3 Title 关键词位置

| 属性 | 值 |
|------|-----|
| 执行方式 | AI 分析 Title 内容 |
| 对应信号 | 关键词权重 |
| 评分标准 | 关键词在前半部分🟢 / 在后半部分🟡 / 无关键词🔴 |

**最佳实践：**
```html
<!-- 好 -->
<title>SEO 审计工具 - 73 项检查清单 | 品牌名</title>

<!-- 不好 -->
<title>品牌名 | 我们提供各种服务包括 SEO 审计</title>
```

---

### O4 Title 唯一性（跨页面）

| 属性 | 值 |
|------|-----|
| 执行方式 | 对比 3 个分析页面的 Title |
| 对应信号 | 避免重复 |
| 评分标准 | 每页唯一🟢 / 有重复🔴 |

---

## 2. Meta 标签（4 项）

### O5 Meta Description 存在性

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `<meta name="description">` |
| 对应信号 | SERP 展示 |
| 评分标准 | 存在🟢 / 不存在🟡 |

**注意：** Google 可能自动生成描述，但自定义描述可控性更好。

---

### O6 Meta Description 长度

| 属性 | 值 |
|------|-----|
| 执行方式 | 统计 description 字符数 |
| 对应信号 | CTR 影响 |
| 评分标准 | 150-160 字符🟢 / 120-150 或 160-200🟡 / <120 或 >200🔴 |

---

### O7 Meta Description 号召力

| 属性 | 值 |
|------|-----|
| 执行方式 | AI 分析描述内容 |
| 对应信号 | CTR |
| 评分标准 | 有明确 CTA 或价值主张🟢 / 仅描述性🟡 / 空洞无力🔴 |

**好的描述应包含：**
- 核心关键词
- 价值主张（用户能获得什么）
- 行动号召（了解更多、立即查看等）

---

### O8 Meta Robots 配置

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `<meta name="robots">` |
| 对应信号 | 索引控制 |
| 评分标准 | index,follow 或无标签🟢 / noindex 或 nofollow🔴（除非有意） |

---

## 3. H 标签（3 项）

### O9 H1 标签存在与唯一性

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `<h1>` 标签数量 |
| 对应信号 | `goldmineHeaderIsH1` |
| 评分标准 | 唯一 1 个🟢 / 0 个或多个🔴 |

**规则：**
- 每个页面应有且仅有 1 个 H1
- H1 应包含页面主关键词

---

### O10 H1 与 Title 一致性

| 属性 | 值 |
|------|-----|
| 执行方式 | AI 分析 H1 和 Title 语义 |
| 对应信号 | Goldmine 信号协调 |
| 评分标准 | 语义一致🟢 / 部分相关🟡 / 完全不一致🔴 |

**说明：** H1 和 Title 不需要完全相同，但应该传达相同的主题。

---

### O11 H 标签层级结构

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析所有 H 标签 |
| 对应信号 | 语义结构 |
| 评分标准 | H1>H2>H3 正确层级🟢 / 有跳级（如 H1 直接到 H3）🔴 |

**正确结构：**
```html
<h1>主标题</h1>
  <h2>章节 1</h2>
    <h3>子节 1.1</h3>
    <h3>子节 1.2</h3>
  <h2>章节 2</h2>
```

---

## 4. URL 结构（3 项）

### O12 URL 可读性（语义化）

| 属性 | 值 |
|------|-----|
| 执行方式 | AI 分析 URL 结构 |
| 对应信号 | `goldmineUrlMatchFactor` |
| 评分标准 | 语义清晰🟢 / 有参数但可理解🟡 / 参数混乱🔴 |

**好的 URL：**
```
/blog/seo-audit-guide
/products/running-shoes
```

**差的 URL：**
```
/page?id=12345&ref=abc
/p/x/y/z/item-999
```

---

### O13 URL 长度

| 属性 | 值 |
|------|-----|
| 执行方式 | 统计 URL 路径字符数 |
| 对应信号 | 可用性 |
| 评分标准 | ≤75 字符🟢 / 76-100🟡 / >100🔴 |

---

### O14 URL 关键词包含

| 属性 | 值 |
|------|-----|
| 执行方式 | AI 分析 URL 是否包含页面关键词 |
| 对应信号 | 相关性 |
| 评分标准 | 包含主关键词🟢 / 无关键词🟡 |

---

## 5. 图片优化（3 项）

### O15 图片 Alt 属性完整度

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析所有 `<img>` 标签 |
| 对应信号 | 图片 SEO |
| 评分标准 | 100% 有 Alt🟢 / 80-99%🟡 / <80%🔴 |

**检查要点：**
- 每张图片应有描述性 alt 文本
- 装饰性图片可用 `alt=""`

---

### O16 图片尺寸属性（width/height）

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `<img>` 的 width/height 属性 |
| 对应信号 | CLS 优化 |
| 评分标准 | 主要图片有尺寸🟢 / 部分有🟡 / 都没有🔴 |

**重要性：** 设置尺寸可防止布局偏移（CLS）。

---

### O17 图片 Lazy Loading

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `loading="lazy"` 属性 |
| 对应信号 | 性能优化 |
| 评分标准 | 非首屏图片有 lazy🟢 / 无🟡 |

**正确用法：**
```html
<!-- 首屏图片：不用 lazy -->
<img src="hero.jpg" loading="eager">

<!-- 非首屏图片：用 lazy -->
<img src="below-fold.jpg" loading="lazy">
```

---

## 6. 社交分享标签（2 项）

### O18 Open Graph 标签完整度

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `og:` 标签 |
| 对应信号 | 社交分享展示 |
| 评分标准 | og:title + og:description + og:image🟢 / 部分有🟡 / 都没有🔴 |

**必需标签：**
```html
<meta property="og:title" content="页面标题">
<meta property="og:description" content="页面描述">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com/page">
<meta property="og:type" content="website">
```

---

### O19 Twitter Card 标签

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `twitter:` 标签 |
| 对应信号 | Twitter 分享展示 |
| 评分标准 | 有完整 Twitter Card🟢 / 无🟡 |

**推荐标签：**
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="页面标题">
<meta name="twitter:description" content="页面描述">
<meta name="twitter:image" content="https://example.com/image.jpg">
```

---

## 7. 链接结构（1 项）

### O20 内部链接数量与锚文本质量

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析页面内所有 `<a>` 标签 |
| 对应信号 | `onsiteProminence` |
| 评分标准 | ≥3 个描述性内链🟢 / 1-2 个🟡 / 0 个或全是"点击这里"🔴 |

**检查要点：**
- 每页至少 3 个内部链接
- 锚文本应描述目标页面内容
- 避免"点击这里"、"了解更多"等空洞锚文本

**好的内链：**
```html
<a href="/seo-guide">SEO 优化完整指南</a>
```

**差的内链：**
```html
<a href="/seo-guide">点击这里</a>
```

---

## 检查项汇总

| ID | 检查项 | 类别 | 评分标准 |
|----|--------|------|----------|
| O1 | Title 存在 | Title | 有🟢 |
| O2 | Title 长度 | Title | 50-60 字符🟢 |
| O3 | Title 关键词位置 | Title | 前半部分🟢 |
| O4 | Title 唯一性 | Title | 唯一🟢 |
| O5 | Meta Description 存在 | Meta | 有🟢 |
| O6 | Meta Description 长度 | Meta | 150-160🟢 |
| O7 | Meta Description 号召力 | Meta | 有 CTA🟢 |
| O8 | Meta Robots | Meta | index,follow🟢 |
| O9 | H1 存在与唯一 | H 标签 | 唯一 1 个🟢 |
| O10 | H1 与 Title 一致性 | H 标签 | 一致🟢 |
| O11 | H 标签层级 | H 标签 | 正确🟢 |
| O12 | URL 可读性 | URL | 语义清晰🟢 |
| O13 | URL 长度 | URL | ≤100🟢 |
| O14 | URL 关键词 | URL | 有🟢 |
| O15 | 图片 Alt | 图片 | 100%🟢 |
| O16 | 图片尺寸 | 图片 | 有🟢 |
| O17 | Lazy Loading | 图片 | 有🟢 |
| O18 | Open Graph | 社交 | 完整🟢 |
| O19 | Twitter Card | 社交 | 有🟢 |
| O20 | 内部链接 | 链接 | ≥3 个🟢 |
