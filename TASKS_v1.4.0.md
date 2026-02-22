# v1.4.0 任务清单（MVP）- 方案 B（精简落地）

## 版本目标

使用轻量、可解释的 `Title + URL` 双引擎识别逻辑，实现网站动态分类与动态选页。

> 强制规则：无论分类结果如何，必须抓取文章页（Article Page）。

---

## 一、分类体系（7+1）

1. 企业官网（Corporate）
2. 电商（E-commerce）
3. 内容站（Content）
4. 工具/SaaS（Tool/SaaS）
5. 社区（Community）
6. 门户（Portal）
7. 单页站（Single-Page Site）
8. 混合/未确定（Hybrid/Unknown）

---

## 二、MVP 识别逻辑（精简）

### 2.1 信号来源（仅 2 类）

1. **Title 信号（主信号，高权重）**
   - 读取首页 `<title>`
   - 识别类别关键词（中英）

2. **URL 信号（校验信号）**
   - 解析 sitemap URL（优先）
   - 若无 sitemap，则解析首页链接 URL

### 2.2 固定权重打分

```text
score(type) = 0.7 * TitleScore + 0.3 * URLScore
```

### 2.3 决策规则

- 输出单一主分类（Top-1）
- 若最高分低于阈值（如 0.45） -> `Hybrid/Unknown`
- MVP 不输出 Top-2，不做置信度交互确认

---

## 三、分类关键词（初版词典）

### 企业官网

- Title: 官网, 企业, 集团, 公司, 服务, 方案
- URL: `/about`, `/services`, `/case`, `/contact`

### 电商

- Title: 商城, 购买, 购物车, 下单, shop, store
- URL: `/product`, `/shop`, `/cart`, `/checkout`, `/category`

### 内容站

- Title: 博客, 资讯, 新闻, 专栏, blog, news
- URL: `/blog`, `/news`, `/article`, `/post`

### 工具/SaaS

- Title: 工具, 平台, software, saas, pricing, features, trial
- URL: `/features`, `/solutions`, `/pricing`, `/integrations`

### 社区

- Title: 社区, 论坛, 讨论, 帖子, forum, topic
- URL: `/forum`, `/thread`, `/topic`, `/community`, `/u/`

### 门户

- Title: 门户, 频道, 热点, 快讯, 头条
- URL: `/channel`, `/hot`, `/headline`, `/special`

### 单页站

- 特征：路径数量极少 + 标题营销导向 + 大量锚点链接

---

## 四、动态选页矩阵（MVP）

| 类型 | 关键业务页（仅1页） | 强制页 |
|------|----------------------|--------|
| 企业官网 | 服务页/解决方案页 | 文章页 |
| 电商 | 商品详情页 | 文章页 |
| 内容站 | 栏目页 | 文章页 |
| 工具/SaaS | 功能页 | 文章页 |
| 社区 | 话题页 | 文章页 |
| 门户 | 频道页 | 文章页 |
| 单页站 | 主落地页 | 文章页 |
| Hybrid | 首页高权重链接页 | 文章页 |

---

## 五、回退与强制规则

1. sitemap 可用：优先 sitemap 选页
2. sitemap 不可用：首页链接启发式 + 深度优先
3. 文章页未命中：记录未命中并标记为后续增强项，不阻断流程
4. 分类失败：进入 Hybrid，不阻断审计流程（Fail-safe）

---

## 六、开发任务拆分（MVP）

### Phase 1：识别器

- [x] 实现首页 Title 解析与关键词匹配
- [x] 实现 URL 路径匹配
- [x] 实现固定权重打分与 Top-1 决策

### Phase 2：动态选页

- [x] 实现“类型 -> 选页优先级”映射
- [x] 注入文章页强制抓取逻辑
- [x] 实现 Hybrid 兜底选页

### Phase 3：回退机制

- [x] sitemap 优先策略
- [x] 首页链接启发式回退

### Phase 4：报告集成

- [x] 报告附录输出类型结果
- [x] 输出判定依据（Title/URL）
- [x] 输出页面来源（sitemap/heuristic）
- [x] 报告开头增加“诊断总览”（中文 300-800 字 / 英文 300-800 words）
- [x] 在“诊断总览”中显式列出本次抓取页面 URL（首页/关键业务页/文章页）
- [x] 报告统一输出到 Skill 目录下 `reports/`，不存在则自动创建

### Phase 5：测试验收

- [x] 每类至少 1-2 个样站跑通（测试样本 10，成功执行 9）
- [x] 验证文章页强制抓取（规则与模板已集成）
- [x] 验证分类失败不阻断主流程（Hybrid 兜底）

测试结果文件：
- `tests/v1.4.0-site-classification-results.md`
- `tests/v1.4.0-site-classification-results.json`
- `tests/v1.4.0-acceptance.md`

---

## 七、验收标准

1. 7+1 分类体系可用，且输出单一主分类。
2. 动态选页按分类生效。
3. 文章页强制抓取有效。
4. sitemap 失败可回退且不中断。
5. 报告附录可解释分类依据。
