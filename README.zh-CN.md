# SEO Audit Skill

> 基于 Google 搜索指南、Ahrefs SEO Checklist 及微软官方搜索指南设计的 92 项 SEO 诊断工具。

[English](README.md) | [简体中文](README.zh-CN.md)

文档来源：
- [Google 搜索指南](https://developers.google.com/search/docs?hl=zh-cn)
- [Ahrefs SEO Checklist](https://ahrefs.com/blog/seo-ai-search-checklist/)
- [微软 AEO & GEO 指南](https://about.ads.microsoft.com/content/dam/sites/msa-about/global/common/content-lib/pdf/from-discovery-to-influence-a-guide-to-aeo-and-geo.pdf)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.4.1-blue.svg)]()

## v1.4.1 新增能力

- 分类能力升级为 `Title + URL + Nav`
- 输出 Top-2 候选类型 + 置信度
- 低置信度场景支持快速确认，且无响应默认继续（不阻断）
- 在主内容路径基础上新增文章页二次发现（`/insights`、`/docs`）
- 报告附录新增可解释字段（Top-1/Top-2、置信度、命中信号、回退路径）

## 快速选择：运行模式

| 功能 | 完整模式（推荐） | 基础模式 |
|------|----------------|----------|
| 配置复杂度 | 需要 API Key | 零配置 |
| 检查项数 | 92 项 | 84 项 |
| Core Web Vitals | ✅ | ❌ 跳过 |
| PageSpeed 评分 | ✅ 移动端 + 桌面端 | ❌ 跳过 |
| 适用场景 | 完整 SEO 诊断 | 快速内容与结构检查 |
| 免费额度 | 每天 25,000 次请求 | N/A |

详细说明：[`USAGE.md`](USAGE.md)

## 快速开始

### 安装

```bash
git clone https://github.com/wonfull888/seo-audit.git
cp -r seo-audit ~/.claude/skills/
```

### 使用

```bash
# 自动检测报告语言（推荐）
/seo-audit https://example.com

# 强制英文报告
/seo-audit https://example.com --en

# 强制中文报告
/seo-audit https://example.com --zh
```

语言选择优先级：
1. 显式标志（`--en` / `--zh`）
2. 基于用户输入自动检测
3. 默认英文

### 配置 API Key（推荐）

```bash
export PAGE_SPEED_API_KEY="your_api_key_here"
```

若环境变量不存在，Skill 会自动按顺序读取：
1. `./.env`
2. `~/.claude/skills/seo-audit/.env`

详细文档：
- [`API_KEY_SETUP.md`](API_KEY_SETUP.md)
- [`QUOTA.md`](QUOTA.md)

## 诊断流程

```text
用户输入网址
    -> 1. 环境检查（API Key）
    -> 2. 报告语言检测
    -> 3. 网站分类识别（Title + URL）
    -> 4. 选择代表页面（首页 + 关键业务页 + 文章页）
    -> 5. 数据采集（curl + WebFetch + 可选 PageSpeed API）
    -> 6. 四维度分析（92 项）
    -> 7. 生成并保存完整 Markdown 报告
```

## 检查项概览

| 维度 | 检查项数 | 权重 |
|------|----------|------|
| 技术 SEO | 29 项 | 32% |
| 页面元素（On-Page SEO） | 27 项 | 29% |
| 内容质量与 E-E-A-T | 33 项 | 36% |
| 本地 SEO | 3 项 | 3% |
| **总计** | **92 项** | **100%** |

## 报告示例

- 英文示例（默认）：[`assets/example-report.en.md`](assets/example-report.en.md)
- 中文示例：[`assets/example-report.md`](assets/example-report.md)

报告默认保存路径：

- `~/.claude/skills/seo-audit/reports/seo-audit-report-{domain}-{timestamp}.md`

## 许可证

[MIT License](LICENSE)

---

**SEO Audit Skill** | [GitHub](https://github.com/wonfull888/seo-audit) | Developer: [x.com/wonfull888](https://x.com/wonfull888)
