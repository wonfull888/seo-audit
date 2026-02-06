# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 待发布

### 计划中的功能
- [ ] 添加更多检查项（国际 SEO、本地 SEO 等）
- [ ] 支持批量网址诊断
- [ ] 生成可视化雷达图
- [ ] 竞品对比分析

### 计划中的改进
- [ ] 优化报告生成速度
- [ ] 增加更多示例报告
- [ ] 改进错误提示信息

---

## [1.0.0] - 2026-02-06

### Added

#### 核心功能
- ✅ 73 项 SEO 检查清单
  - ✅ 技术 SEO（25 项，30% 权重）
  - ✅ 页面元素（20 项，20% 权重）
  - ✅ 内容质量与 E-E-A-T（28 项，50% 权重）
- ✅ E-E-A-T 子维度分析
  - ✅ Trust（信任度，8 项，40% of E-E-A-T）
  - ✅ Experience（经验，7 项，20% of E-E-A-T）
  - ✅ Expertise（专业度，7 项，20% of E-E-A-T）
  - ✅ Authoritativeness（权威性，6 项，20% of E-E-A-T）
- ✅ 双模式支持
  - ✅ 完整模式（73 项，需 API Key）
  - ✅ 基础模式（65 项，零配置，跳过 Core Web Vitals）
- ✅ 动态评分权重调整
  - ✅ 有 API Key：技术 30%，E-E-A-T 50%
  - ✅ 无 API Key：技术 25%，E-E-A-T 55%
- ✅ 优先级分类系统
  - ✅ P0（必须立即修复）
  - ✅ P1（尽快修复）
  - ✅ P2（计划优化）
- ✅ 双语支持
  - ✅ 默认中文报告
  - ✅ 可选英文报告（--en 或 "英文报告"）
- ✅ AI 写作检测模块
  - ✅ Em dash 使用检测
  - ✅ 高频 AI 词汇识别
  - ✅ 三元组句式模式检测
- ✅ 模糊归因检测

#### 修正与优化（v1.0.0 发布后）
- ✅ 移除误导的"关键词密度"检查标准（Google 已不再关注密度，改为关注关键词位置）
- ✅ PageSpeed API 调用保持环境变量方式，不暴露 API Key

#### 文档
- ✅ PRODUCT.md（产品说明，功能全貌）
- ✅ README.md（GitHub 首页，用户指南）
- ✅ USAGE.md（详细使用指南，双模式说明）
- ✅ API_KEY_SETUP.md（API Key 配置文档）
- ✅ QUOTA.md（免费额度计算和说明）
- ✅ CHANGELOG.md（版本历史）
- ✅ LICENSE（MIT 许可证）
- ✅ references/（详细参考文档）
  - ✅ technical-seo.md（技术 SEO 25 项详情）
  - ✅ on-page-elements.md（页面元素 20 项详情）
  - ✅ content-eeat.md（E-E-A-T 28 项详情）
  - ✅ scoring-system.md（评分系统，含降级模式）
  - ✅ report-template.md（报告模板）
  - ✅ ai-writing-detection.md（AI 写作特征检测）
- ✅ assets/example-report.md（完整示例报告）

#### 安全与配置
- ✅ .gitignore（敏感文件过滤）
- ✅ .env.example（配置模板）
- ✅ 环境变量支持（PAGE_SPEED_API_KEY）
- ✅ API Key 保护（无硬编码）

#### SDLC 符合
- ✅ 创建 PRODUCT.md（产品说明，适合 Skill 工具）
- ✅ 不创建 CURRENT.md（Skill 无迭代概念）
- ✅ 不创建 TASKS.md（Skill 无开发任务）
- ✅ 维护 CHANGELOG.md（版本历史）

### 技术栈

- ✅ 无依赖 Python/Node.js
- ✅ 仅使用 curl（HTTP 请求）
- ✅ WebFetch（AI 内置工具）
- ✅ PageSpeed API（可选）

### API 集成

- ✅ Google PageSpeed Insights API v5
- ✅ 移动端 + 桌面端双策略
- ✅ 免费额度说明（每天 25,000 次请求）
- ✅ 环境变量支持

### 评分标准

| 等级 | 分数 | 状态 |
|------|------|------|
| A | 90-100 | 🟢 优秀 |
| B | 80-89 | 🟢 良好 |
| C | 70-79 | 🟡 中等 |
| D | 60-69 | 🟡 较差 |
| F | <60 | 🔴 不及格 |

### E-E-A-T 评分

| 子维度 | 检查项 | 占 E-E-A-T 权重 | 占总权重 |
|--------|--------|-----------------|----------|
| Trust（信任度） | 8 项 | 40% | 20% |
| Experience（经验） | 7 项 | 20% | 10% |
| Expertise（专业度） | 7 项 | 20% | 10% |
| Authoritativeness（权威性） | 6 项 | 20% | 10% |

### 检查标准

| 项目 | 标准 |
|------|------|
| Title 长度 | 50-60 字符 |
| Meta Description 长度 | 150-160 字符 |
| 首页最低字数 | 500 字 |
| 分类页最低字数 | 300 字 |
| 文章页最低字数 | 1000 字 |
| 关键词密度 | 1-2% |
| 内部链接 | ≥3 个/页 |
| URL 长度 | ≤100 字符 |

### Core Web Vitals

| 指标 | 良好 | 需改进 | 严重 |
|------|------|--------|------|
| LCP | <2.5s | 2.5-4s | >4s |
| FCP | <1.8s | 1.8-3s | >3s |
| CLS | <0.1 | 0.1-0.25 | >0.25 |
| INP | <200ms | 200-500ms | >500ms |
| TBT | <200ms | 200-600ms | >600ms |
| TTFB | <800ms | 800-1800ms | >1800ms |

### 报告语言

- 默认: 中文
- 可选: 英文（--en 或 "英文报告"）

### 文件结构

```
seo-audit/
├── .env.example                  # 配置模板
├── .gitignore                   # Git 忽略规则
├── API_KEY_SETUP.md            # API Key 配置文档
├── CHANGELOG.md                # 版本历史（本文件）
├── LICENSE                     # MIT 许可证
├── PRODUCT.md                  # 产品说明
├── QUOTA.md                   # 免费额度说明
├── README.md                   # GitHub 首页
├── SKILL.md                   # Skill 主文件
├── USAGE.md                   # 详细使用指南
├── assets/
│   └── example-report.md       # 示例报告
└── references/
    ├── ai-writing-detection.md  # AI 写作检测
    ├── content-eeat.md        # E-E-A-T 详情
    ├── on-page-elements.md     # 页面元素详情
    ├── report-template.md      # 报告模板
    ├── scoring-system.md       # 评分系统
    └── technical-seo.md        # 技术 SEO 详情
```

### 开源信息

- 仓库名: `seo-audit`
- 许可证: MIT License
- API Key: 用户自行配置（不包含在仓库中）
- Google PageSpeed API: 每天 25,000 次免费请求

### 致谢

- Google Content Warehouse 泄露文档分析社区
- [Hobo SEO Audit Framework](https://www.hobo-web.co.uk/)
- SCA (Specialty Coffee Association) - 示例报告参考
- Stack Overflow - PageSpeed API 免费额度确认

---

## [Unreleased]

### 计划中

详见 [1.1.0 版本计划](#110---待发布)
