# SEO Audit Skill

> 基于 Google 搜索指南、Ahrefs SEO Checklist 及微软官方搜索指南设计的 73 项 SEO 诊断工具（持续更新中）

文档来源：
- [Google 搜索指南](https://developers.google.com/search/docs?hl=zh-cn)
- [Ahrefs SEO Checklist](https://ahrefs.com/blog/seo-ai-search-checklist/)
- [微软搜索指南](https://about.ads.microsoft.com/content/dam/sites/msa-about/global/common/content-lib/pdf/from-discovery-to-influence-a-guide-to-aeo-and-geo.pdf)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)]()

## 快速选择：你需要哪种模式？

| 功能 | 完整模式（推荐） | 基础模式 |
|------|----------------|----------|
| **配置复杂度** | 需要配置 API Key | 零配置，开箱即用 |
| **检查项数** | 73 项 | 65 项 |
| **Core Web Vitals** | ✅ LCP, FCP, CLS, INP | ❌ 跳过 |
| **PageSpeed 评分** | ✅ 移动端 + 桌面端 | ❌ 跳过 |
| **技术 SEO 权重** | 30% | 25% |
| **E-E-A-T 权重** | 50% | 55% |
| **适用场景** | 完整 SEO 诊断 | 快速内容检查 |
| **免费额度** | 每天 25,000 次请求 | N/A |

> 📖 详细说明：[USAGE.md](USAGE.md)

---

## 为什么需要这个 Skill？

### 💡 开发初衷

传统 SEO 工具往往需要**繁琐的登录**或**昂贵的付费订阅**，对于快速诊断来说门槛太高。

随着 AI 大模型的高速发展，我们迎来了 **Token 自由** 的时代。这意味着我们可以轻松构建属于自己的轻量级工具，不再受限于传统 SaaS 的限制。

### 🚀 对你的价值

1. **零门槛、零付费**：无需注册账号，无需绑定信用卡，甚至不需要安装复杂的 Python/Node.js 环境。
2. **轻量级、即用即走**：基于 AI Agent 的 Skill 形式，一行命令即可启动诊断。
3. **透明可控**：所有检查逻辑开源，基于权威文档（Google/微软/Ahrefs），而非黑盒算法。
4. **持续进化**：
   - 目前支持 Markdown 报告导出
   - 未来计划支持 **可视化图表**、**批量诊断** 和 **历史趋势对比**

本 Skill 旨在为你提供一个**快速、免费、且专业的网站体检报告**。

---

## 快速开始

### 安装

将 `SKILL.md` 和 `references/` 目录复制到你的 Claude Code skills 目录：

```bash
# 克隆仓库
git clone https://github.com/wonfull888/seo-audit.git

# 复制到 skills 目录
cp -r seo-audit ~/.claude/skills/
```

### 配置 API Key（推荐，非必需）

**⭐ 免费额度：每天 25,000 次请求！**

Google PageSpeed Insights API 提供免费配额，个人使用完全够用：

| 使用场景 | 每月请求 | 可用时长 |
|---------|-----------|---------|
| 每天诊断 1 个网站 | 180 次 | 约 11 年 |
| 每天诊断 10 个网站 | 1,800 次 | 约 14 个月 |
| 每天诊断 100 个网站 | 18,000 次 | 约 1.5 个月 |

#### 配置步骤

```bash
# 设置环境变量
export PAGE_SPEED_API_KEY="your_api_key_here"
```

#### 获取免费 API Key

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建项目或选择现有项目
3. 启用 **PageSpeed Insights API**
4. 创建 API Key（免费）

📊 **免费额度详情**：[QUOTA.md](QUOTA.md)

详细说明：[API_KEY_SETUP.md](API_KEY_SETUP.md)

### 使用

#### 方式 1：完整诊断（有 API Key）

```bash
# 先设置环境变量
export PAGE_SPEED_API_KEY="your_api_key_here"

# 开始诊断
对 https://example.com 进行 SEO 诊断

# 结果：完整 73 项检查 + 性能数据
```

#### 方式 2：基础诊断（无 API Key）

```bash
# 直接使用，无需配置
对 https://example.com 进行 SEO 诊断

# 结果：65 项检查（跳过 Core Web Vitals）+ 调整评分权重
```

**差异对比：**

| 功能 | 有 API Key | 无 API Key |
|------|-----------|-----------|
| 检查项数 | 73 项 | 65 项 |
| 技术 SEO 权重 | 30% | 25% |
| E-E-A-T 权重 | 50% | 55% |
| Core Web Vitals | ✅ LCP, FCP, CLS, INP | ❌ 跳过 |
| PageSpeed 评分 | ✅ 移动端 + 桌面端 | ❌ 跳过 |

## 诊断流程

```
用户输入网址
    ↓
1. 页面识别（sitemap.xml 或启发式）
    ↓
2. 选择 3 个代表页面（首页 + 分类页 + 文章页）
    ↓
3. 数据采集
   ├─ curl: robots.txt, HTTP headers
   ├─ WebFetch: 3 个页面 HTML
   └─ PageSpeed API: 6 次调用（3 URL × 2 策略）
    ↓
4. 三维度分析（73 项检查）
    ↓
5. 生成诊断报告
```

## 检查项概览

| 维度 | 检查项数 | 权重 | 说明 |
|------|----------|------|------|
| 技术 SEO | 25 项 | 30% | Core Web Vitals、索引、安全 |
| 页面元素 | 20 项 | 20% | Title、Meta、H 标签、图片 |
| 内容质量与 E-E-A-T | 28 项 | 50% | Google 核心排名信号 |
| **总计** | **73 项** | **100%** | |

### E-E-A-T 细分

| 子维度 | 检查项 | 占总权重 |
|--------|--------|----------|
| Trust（信任度） | 8 项 | 20% |
| Experience（经验） | 7 项 | 10% |
| Expertise（专业度） | 7 项 | 10% |
| Authoritativeness（权威性） | 6 项 | 10% |

## 评分标准

| 等级 | 分数 | 状态 |
|------|------|------|
| A | 90-100 | 🟢 优秀 |
| B | 80-89 | 🟢 良好 |
| C | 70-79 | 🟡 中等 |
| D | 60-69 | 🟡 较差 |
| F | <60 | 🔴 不及格 |

## 报告示例

查看完整的报告示例：[assets/example-report.md](assets/example-report.md)

报告包含：
- 综合评分与各维度得分
- P0/P1/P2 优先级行动清单
- 73 项逐条检查结果
- 针对性优化建议（附代码示例）

## 文件结构

```
seo-audit/
├── SKILL.md                    # Skill 主入口
├── README.md                   # 本文件
├── LICENSE                     # MIT 许可证
├── CHANGELOG.md                # 版本历史
├── references/
│   ├── technical-seo.md        # 技术 SEO 25 项详情
│   ├── on-page-elements.md     # 页面元素 20 项详情
│   ├── content-eeat.md         # E-E-A-T 28 项详情
│   ├── scoring-system.md       # 评分系统
│   ├── report-template.md      # 报告模板
│   └── ai-writing-detection.md # AI 写作特征检测
└── assets/
    └── example-report.md       # 示例报告
```

## 技术要求

本 Skill 不依赖 Python/Node.js，仅需：

- **curl** - HTTP 请求
- **WebFetch** - AI 内置工具
- **PageSpeed API** - 可选（推荐配置以获取完整报告，见 [USAGE.md](USAGE.md)）

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

[MIT License](LICENSE)

## 致谢

- Google Content Warehouse 泄露文档分析社区
- [Hobo SEO Audit Framework](https://www.hobo-web.co.uk/)
- SCA (Specialty Coffee Association) - 示例报告参考

### 参考指南

- **Google 搜索指南** (中文) - [https://developers.google.com/search/docs?hl=zh-cn](https://developers.google.com/search/docs?hl=zh-cn)
- **Ahrefs SEO AI Search Checklist** - [https://ahrefs.com/blog/seo-ai-search-checklist/](https://ahrefs.com/blog/seo-ai-search-checklist/)
- **微软 AEO & GEO 指导** - [https://about.ads.microsoft.com/content/dam/sites/msa-about/global/common/content-lib/pdf/from-discovery-to-influence-a-guide-to-aeo-and-geo.pdf](https://about.ads.microsoft.com/content/dam/sites/msa-about/global/common/content-lib/pdf/from-discovery-to-influence-a-guide-to-aeo-and-geo.pdf)

---

**Made with ☕ by SEO enthusiasts**
