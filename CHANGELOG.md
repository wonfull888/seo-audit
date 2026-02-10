# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-02-10

### Added

#### 新增19项检查,从73项扩展到92项

基于 [Ahrefs 82项 SEO+AI搜索清单](https://ahrefs.com/blog/seo-ai-search-checklist/) 分析,新增以下检查项:

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
- ✅ 检查维度: 3维 → 6维
  - 技术 SEO: 25 → 29项 (权重 30% → 28%)
  - 页面元素: 20 → 22项 (权重 20% → 18%)
  - 内容质量与E-E-A-T: 28 → 31项 (权重 50% → 42%)
  - 新增 AI 搜索优化: 5项 (权重 6%)
  - 新增 本地 SEO: 3项 (权重 4%)
  - 新增 信任信号: 2项 (权重 2%)
- ✅ 文档来源更新: 新增 Ahrefs 82项 SEO+AI搜索清单
- ✅ 版本号: 1.0.0 → 1.1.0

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

## [Unreleased]

### 计划中

详见 [VERSION_1.1.0.md](VERSION_1.1.0.md) 及 [PRODUCT.md](PRODUCT.md)
