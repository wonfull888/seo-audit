# SEO Audit Skill

> 基于 Google Content Warehouse 泄露信号设计的 73 项 SEO 诊断工具

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

传统 SEO 工具只关注技术指标，忽略了 Google 真正看重的 **E-E-A-T 信号**。

本 Skill 基于 2024 年 Google Content Warehouse 泄露文档，设计了完整的 73 项检查清单，覆盖：

- **技术 SEO**（25 项）- 可发现性、性能、安全性、结构化数据
- **页面元素**（20 项）- Title、Meta、H 标签、图片、社交标签
- **内容质量与 E-E-A-T**（28 项）- Trust、Experience、Expertise、Authoritativeness

## 快速开始

### 安装

将 `SKILL.md` 和 `references/` 目录复制到你的 Claude Code skills 目录：

```bash
# 克隆仓库
git clone https://github.com/yourusername/seo-audit.git

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

```
# 先设置环境变量
export PAGE_SPEED_API_KEY="your_api_key_here"

# 开始诊断
对 https://example.com 进行 SEO 诊断

# 结果：完整 73 项检查 + 性能数据
```

#### 方式 2：基础诊断（无 API Key）

```
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

## 文件结构

```
seo-audit/
├── SKILL.md                    # Skill 主入口
├── README.md                   # 本文件
├── USAGE.md                   # 📖 详细使用指南（推荐阅读）
├── API_KEY_SETUP.md            # API Key 配置文档
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

### API Key 安全

- ⚠️ 永远不要将 API Key 提交到 Git
- 使用环境变量存储 API Key
- `.gitignore` 已配置忽略敏感文件

## 贡献

欢迎提交 Issue 和 Pull Request！

### 改进方向

- [ ] 添加更多检查项
- [ ] 支持批量网址诊断
- [ ] 生成可视化雷达图
- [ ] 竞品对比分析

## 许可证

[MIT License](LICENSE)

## 致谢

- Google Content Warehouse 泄露文档分析社区
- [Hobo SEO Audit Framework](https://www.hobo-web.co.uk/)
- SCA (Specialty Coffee Association) - 示例报告参考

---

**Made with ☕ by SEO enthusiasts**
