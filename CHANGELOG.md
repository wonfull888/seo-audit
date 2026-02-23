# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

#### v1.4.1 - Classification enhancement and explainability
- Added enhanced classification strategy with `Title + URL + Nav` signals.
- Added Top-2 type output and confidence score/band output.
- Added low-confidence quick confirmation strategy with non-blocking default behavior.
- Added article secondary-path discovery (`/insights`, `/docs`) on top of primary content paths.
- Added new reference doc: `references/site-classification-v141.md`.
- Added v1.4.1 evaluator and artifacts:
  - `tests/evaluate_site_classification_v141.py`
  - `tests/site_classification_samples_v141.json`
  - `tests/v1.4.1-site-classification-results.md`
  - `tests/v1.4.1-site-classification-results.json`
  - `tests/v1.4.1-acceptance.md`

### Changed

- Updated `SKILL.md` classification workflow from v1.4.0 MVP to v1.4.1 enhanced flow.
- Updated bilingual report templates to include Top-2, confidence, Nav signals, and confirmation action fields.
- Updated `TASKS_v1.4.1.md` to atomic tasks and marked implementation/testing completion with evidence links.

## [1.4.0] - 2026-02-22

### Added

#### v1.4.0 MVP - Site classification and dynamic page selection
- Added lightweight site classification strategy based on `Title + URL` signals (Top-1 output).
- Added 7+1 site type framework: Corporate, E-commerce, Content, Tool/SaaS, Community, Portal, Single-Page, Hybrid/Unknown.
- Added dynamic page selection rule: homepage + key business page + mandatory article page.
- Added fail-safe fallback flow: sitemap-first, then homepage-link heuristic, then Hybrid mode without blocking audit.
- Added site classification rule reference: `references/site-classification-mvp.md`.
- Added report intro requirement: Executive Summary at the beginning with mandatory coverage fields.
- Added mandatory report save path to skill directory `reports/` with auto-create behavior.
- Added `.env` auto-load fallback for `PAGE_SPEED_API_KEY`.

#### Test and validation artifacts
- Added evaluator script: `tests/evaluate_site_classification_v140.py`.
- Added sample dataset: `tests/site_classification_samples_v140.json`.
- Added result outputs:
  - `tests/v1.4.0-site-classification-results.md`
  - `tests/v1.4.0-site-classification-results.json`

### Changed

- Updated `SKILL.md` to include v1.4.0 classification workflow and appendix output requirements.
- Updated bilingual report templates to use "Key Business Page" instead of fixed "Category Page".
- Split planning scope into:
  - `TASKS_v1.4.0.md` (MVP)
  - `TASKS_v1.4.1.md` (enhancements)

## [1.3.0] - 2026-02-18

### Added

#### Complete internationalization baseline
- ✅ English-first documentation experience (`README.md` default in English)
- ✅ Chinese companion README (`README.zh-CN.md`)
- ✅ Bilingual docs structure under `docs/en/` and `docs/zh-CN/`
- ✅ Language entry pages for `USAGE.md`, `API_KEY_SETUP.md`, `QUOTA.md`

#### Intelligent report language selection
- ✅ Explicit report flags: `--en`, `--zh`
- ✅ Auto language detection workflow documented in `references/language-detection.md`
- ✅ Low-confidence fallback strategy documented in `references/quick-confirm-mechanism.md`

#### Bilingual report artifacts
- ✅ Added `references/report-template.en.md`
- ✅ Added `references/report-template.zh-CN.md`
- ✅ Added English example report `assets/example-report.en.md`
- ✅ Added Chinese mapping file `assets/example-report.zh-CN.md`

### Changed

- ✅ `SKILL.md`
  - version bumped to `1.3.0`
  - added report-language detection section
  - updated template selection rules for bilingual output
- ✅ `references/report-template.md` changed to compatibility entry
- ✅ README and usage docs updated with language-switch links and language-priority behavior

### Notes

- v1.4.0 is planned for smart website-type detection and dynamic page selection.

## [1.2.2] - 2026-02-10

### Changed

#### 报告结构优化
- ✅ **页面数据预览前置** - 将 Title、Meta Description、H1 等实际内容从附录移至"页面元素"部分开头
- ✅ **提升阅读连贯性** - 用户先看实际数据（Title 写的是什么），再看检查结果（Title 是否合规），无需跳转
- ✅ **附录精简化** - 附录仅保留分析信息（URL、时间戳、数据来源），不再承载核心数据展示

#### 文档更新
- ✅ `references/report-template.md` - 重构页面元素部分结构：
  - 新增 `2.1 页面数据预览`（Title & Meta Description 表格、H 标签结构、关键词分布）
  - 新增 `2.2 检查结果明细`（原 P1-P27 检查表格）
  - 移除附录中的页面数据详情（已前置）

### Technical Details

**新模板结构：**
```
## 📝 详细检查清单
### 1. 技术 SEO (29项)
[统一6列表格]

### 2. 页面元素 (27项)
#### 2.1 页面数据预览
  - Title & Meta Description 表格
  - H 标签结构
  - 关键词分布
#### 2.2 检查结果明细
[统一6列表格]

### 3. E-E-A-T (33项)
[统一6列表格]

## 附录
### A. 分析信息
  - URL、爬取时间、数据来源
```

---

## [1.2.1] - 2026-02-10

### Added

### Added

#### 智能交互模式
- ✅ **环境自检** - 自动检测 `PAGE_SPEED_API_KEY` 环境变量状态。
- ✅ **智能引导** - 当未配置 API Key 时，主动询问用户选择"完整诊断"（引导配置）或"基础诊断"（跳过性能分析）。
- ✅ **交互式流程** - 优化用户体验，避免因环境问题导致诊断失败或结果不完整。

#### 报告规范化
- ✅ **完整展示** - 诊断结束后，Markdown 报告直接在对话框中完整渲染。
- ✅ **自动保存** - 报告自动保存为 `seo-audit-report-{domain}-{timestamp}.md`。
- ✅ **品牌页脚** - 所有报告底部统一添加 GitHub 仓库和开发者 X 账号链接，增强品牌传播。

### Changed
- ✅ `SKILL.md` - 新增"交互与执行规范"章节，明确 API Key 检查和报告输出要求。
- ✅ `references/report-template.md` - 更新模板，添加标准化的品牌页脚。
- ✅ `README.md` - 更新快速开始和诊断流程，说明新的交互模式。

---

## [1.1.0] - 2026-02-10

### Added

#### 新增19项检查,从73项扩展到92项,优化为4维度结构

基于 [Ahrefs 82项 SEO+AI搜索清单](https://ahrefs.com/blog/seo-ai-search-checklist/) 分析,新增19项检查并优化维度结构:
- **AI搜索优化** 归入 **页面元素** (因为将单独开发GEO监测skill)
- **信任信号** 归入 **E-E-A-T** (Trust本就是E-E-A-T核心维度)

##### AI 搜索优化 (5项)
- ✅ **A1 TL;DR摘要检测** - AI搜索引擎偏好引用包含简洁摘要的页面,检测页面开头是否有摘要
- ✅ **A2 Answer-Oriented Writing** - 检测"先结论后支撑"的写作模式,提高AI直接引用适配度
- ✅ **A3 可引用内容块** - 识别表格、步骤列表、代码示例等AI易摘录的独立内容单元
- ✅ **A4 FAQ Schema** - 检测FAQPage结构化数据,提高在AI问答中被引用的概率
- ✅ **A5 语音搜索优化** - 检测自然语言问答格式,适配语音助手朗读需求

##### 本地 SEO 增强 (3项)
- ✅ **L1 LocalBusiness Schema** - 检测本地商家结构化数据,提高Google Maps展示
- ✅ **L2 Google Maps嵌入** - 检测地图嵌入,向Google发送本地相关性信号
- ✅ **L3 NAP一致性** - 对比名称/地址/电话在页面、Schema中的一致性

##### 技术 SEO 增强 (4项)
- ✅ **TE1 Hreflang标签** - 多语言/多地区配置检测,避免国际SEO重复内容问题
- ✅ **TE2 服务器渲染检测** - SSR vs CSR判断,确保爬虫能抓取完整内容
- ✅ **TE3 现代图片格式** - 检测WebP/AVIF使用,相同质量下文件小30-50%
- ✅ **TE4 浏览器缓存配置** - HTTP headers缓存设置检查,提高回访速度

##### 内容质量增强 (3项)
- ✅ **CQ1 内容可扫描性** - 分析段落/句子长度和列表使用,提高快速浏览体验
- ✅ **CQ2 术语定义** - 检测专业术语首次出现时是否有解释,提高可理解性
- ✅ **CQ3 多媒体丰富度** - 统计视频/音频/交互内容,提高用户停留时间

##### 内容分发优化 (2项)
- ✅ **CD1 多平台社交标签** - 检测Pinterest等平台特定标签,确保跨平台分享展示
- ✅ **CD2 标题吸引力** - 分析情感化元素(数字/疑问/情感词),预测社交分享率

##### 信任信号增强 (2项)
- ✅ **TS1 退款保证** - 电商/SaaS网站保证政策检测,降低用户购买风险
- ✅ **TS2 安全认证徽章** - 识别SSL/ISO/行业认证等信任标记

#### 新增参考文档
- ✅ [ai-search-optimization.md](references/ai-search-optimization.md) - AI搜索优化5项详情
- ✅ [local-seo-enhanced.md](references/local-seo-enhanced.md) - 本地SEO 3项详情
- ✅ [technical-seo-enhanced.md](references/technical-seo-enhanced.md) - 技术SEO增强4项详情
- ✅ [content-quality-enhanced.md](references/content-quality-enhanced.md) - 内容质量增强3项详情
- ✅ [content-distribution.md](references/content-distribution.md) - 内容分发2项详情
- ✅ [trust-signals-enhanced.md](references/trust-signals-enhanced.md) - 信任信号2项详情

### Changed
- ✅ 检查项总数: 73 → 92 (+19项)
- ✅ 检查维度: 3维 → 4维 (优化结构,合并相关维度)
  - 技术 SEO: 25 → 29项 (权重 30% → 32%)
  - 页面元素: 20 → 27项 (权重 20% → 29%) - **包含AI搜索优化5项+内容分发2项**
  - 内容质量与E-E-A-T: 28 → 33项 (权重 50% → 36%) - **包含内容质量3项+信任信号2项**
  - 本地 SEO: 0 → 3项 (权重 0% → 3%)
- ✅ 文档来源更新: 新增 Ahrefs 82项 SEO+AI搜索清单
- ✅ 版本号: 1.0.0 → 1.1.0

### 维度优化说明

**为什么是4维度而非6维度?**
1. **AI搜索归入页面元素** - TL;DR摘要、FAQ Schema等本质是页面结构优化,且将单独开发GEO监测skill
2. **信任信号归入E-E-A-T** - 退款保证、安全徽章本就是E-E-A-T中Trust(信任度)的具体体现

### 技术实现

所有新增检查项均基于:
- ✅ 命令行工具 (`curl`)
- ✅ AI 分析能力
- ✅ PageSpeed API (可选)
- ✅ **无需安装任何脚本、程序环境**

### 原理说明 (每项一句话)

| ID | 检查项 | 原理 |
|----|--------|------|
| A1 | TL;DR摘要 | AI搜索引擎偏好引用包含简洁摘要的页面,因为摘要能直接回答用户问题 |
| A2 | Answer-Oriented Writing | AI偏好引用直接给出答案的内容块,而非需要阅读全文才能找到结论的内容 |
| A3 | 可引用内容块 | AI搜索引擎更容易摘录格式清晰、能独立理解的内容块(如表格、代码示例) |
| A4 | FAQ Schema | FAQPage结构化数据让AI搜索引擎直接提取问答对,提高被引用概率 |
| A5 | 语音搜索优化 | 语音助手倾向朗读完整句子而非关键词,内容应使用自然语言 |
| L1 | LocalBusiness Schema | 结构化数据帮助Google理解实体店信息,提高Google Maps展示 |
| L2 | Google Maps嵌入 | 嵌入地图提高用户体验,同时向Google发送本地相关性信号 |
| L3 | NAP一致性 | Google对比网页/Schema/GMB中的NAP,不一致会降低本地排名 |
| TE1 | Hreflang标签 | 告诉Google不同语言/地区版本关系,避免重复内容问题 |
| TE2 | 服务器渲染检测 | SSR让爬虫直接抓取完整HTML,CSR依赖JS可能导致抓取不完整 |
| TE3 | 现代图片格式 | WebP/AVIF在相同质量下比JPEG/PNG小30-50%,提高加载速度 |
| TE4 | 浏览器缓存配置 | 正确配置缓存让浏览器存储静态资源,减少重复请求 |
| CQ1 | 内容可扫描性 | 短段落、短句子和列表提高内容可扫描性,用户能快速找到信息 |
| CQ2 | 术语定义 | 定义术语让不同背景读者都能理解,向搜索引擎明确概念 |
| CQ3 | 多媒体丰富度 | 多样化媒体提高用户参与度和停留时间,这是重要排名信号 |
| CD1 | 多平台社交标签 | 不同平台有特定标签偏好,完整覆盖确保各平台良好展示 |
| CD2 | 标题吸引力 | 包含数字/疑问/情感词的标题在社交媒体分享率更高 |
| TS1 | 退款保证 | 明确保证降低购买风险,提高转化率,也是E-E-A-T中Trust体现 |
| TS2 | 安全认证徽章 | 第三方认证通过权威背书增强信任,对YMYL内容尤其重要 |

---

## [1.0.0] - 2026-02-06

### Added

#### 核心功能
- ✅ 73 项 SEO 检查清单
  - ✅ 三维度诊断:技术 SEO(25 项) + 页面元素(20 项) + E-E-A-T(28 项)
- ✅ E-E-A-T 子维度分析
  - ✅ Trust(信任度,8 项,40% of E-E-A-T)
  - ✅ Experience(经验,7 项,20% of E-E-A-T)
  - ✅ Expertise(专业度,7 项,20% of E-E-A-T)
  - ✅ Authoritativeness(权威性,6 项,20% of E-E-A-T)
- ✅ **文档来源更新**:基于微软官方搜索指南([AEO & GEO](https://about.ads.microsoft.com/content/dam/sites/msa-about/global/common/content-lib/pdf/from-discovery-to-influence-a-guide-to-aeo-and-geo.pdf))
- ✅ 双模式支持
  - ✅ 完整模式(73 项,需 API Key)
  - ✅ 基础模式(65 项,零配置,跳过 Core Web Vitals)
- ✅ 动态评分权重调整
  - ✅ 有 API Key:技术 30%,E-E-A-T 50%
  - ✅ 无 API Key:技术 25%,E-E-A-T 55%
- ✅ 优先级分类系统
  - ✅ P0(必须立即修复)
  - ✅ P1(尽快修复)
  - ✅ P2(计划优化)
- ✅ 双语支持
  - ✅ 默认中文报告
  - ✅ 可选英文报告(--en 或 "英文报告")
- ✅ AI 写作检测模块
  - ✅ Em dash 使用检测
  - ✅ 高频 AI 词汇识别
  - ✅ 三元组句式模式检测
- ✅ 模糊归因检测

#### 修正与优化(v1.0.0 发布后)
- ✅ 移除误导的"关键词密度"检查标准(Google 已不再关注密度,改为关注关键词位置)
- ✅ PageSpeed API 调用保持环境变量方式,不暴露 API Key

#### 文档
- ✅ PRODUCT.md(产品说明,功能全貌)
- ✅ README.md(GitHub 首页,用户指南)
- ✅ USAGE.md(详细使用指南,双模式说明)
- ✅ API_KEY_SETUP.md(API Key 配置文档)
- ✅ QUOTA.md(免费额度计算和说明)
- ✅ CHANGELOG.md(版本历史)
- ✅ LICENSE(MIT 许可证)
- ✅ references/(详细参考文档)
  - ✅ technical-seo.md(技术 SEO 25 项详情)
  - ✅ on-page-elements.md(页面元素 20 项详情)
  - ✅ content-eeat.md(E-E-A-T 28 项详情)
  - ✅ scoring-system.md(评分系统,含降级模式)
  - ✅ report-template.md(报告模板)
  - ✅ ai-writing-detection.md(AI 写作特征检测)
- ✅ assets/example-report.md(完整示例报告)

#### 安全与配置
- ✅ .gitignore(敏感文件过滤)
- ✅ .env.example(配置模板)
- ✅ 环境变量支持(PAGE_SPEED_API_KEY)
- ✅ API Key 保护(无硬编码)

#### SDLC 符合
- ✅ 创建 PRODUCT.md(产品说明,适合 Skill 工具)
- ✅ 不创建 CURRENT.md(Skill 无迭代概念)
- ✅ 不创建 TASKS.md(Skill 无开发任务)
- ✅ 维护 CHANGELOG.md(版本历史)

### 技术栈

- ✅ 无依赖 Python/Node.js
- ✅ 仅使用 curl(HTTP 请求)
- ✅ WebFetch(AI 内置工具)
- ✅ PageSpeed API(可选)

### API 集成

- ✅ Google PageSpeed Insights API v5
- ✅ 移动端 + 桌面端双策略
- ✅ 免费额度说明(每天 25,000 次请求)
- ✅ 环境变量支持

---
