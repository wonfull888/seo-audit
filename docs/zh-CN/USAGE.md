# 使用指南

<!-- 术语翻译参考: /references/SEO_TERMINOLOGY_GLOSSARY.md -->

**语言**: [English](../en/USAGE.md) | [简体中文](USAGE.md)

## 概述

SEO Audit Skill 支持两种运行模式：

1. **完整模式（推荐）**：需要 `PAGE_SPEED_API_KEY`
2. **基础模式**：无需 API Key，跳过性能指标

## 模式对比

| 项目 | 完整模式 | 基础模式 |
|------|----------|----------|
| 检查项数 | 92 项 | 84 项 |
| Core Web Vitals | ✅ | ❌ |
| PageSpeed 评分（移动端/桌面端） | ✅ | ❌ |
| 适用场景 | 完整 SEO 诊断 | 快速审查 |

## 完整模式

### 配置步骤

```bash
# 1) 配置环境变量
export PAGE_SPEED_API_KEY="your_api_key_here"

# 2) 验证
echo $PAGE_SPEED_API_KEY

# 3) 开始诊断
/seo-audit https://example.com
```

### 优势

- 获取官方性能数据（CWV + PageSpeed）
- 技术 SEO 诊断更完整
- 报告建议更具体

## 基础模式

无需配置，直接执行：

```bash
/seo-audit https://example.com
```

基础模式会跳过 Core Web Vitals 和 PageSpeed 评分，其他维度照常执行。

## 报告语言选择

```bash
# 自动检测（推荐）
/seo-audit https://example.com

# 显式指定英文
/seo-audit https://example.com --en

# 显式指定中文
/seo-audit https://example.com --zh
```

优先级：
1. 显式标志（`--en` / `--zh`）
2. 输入语言自动检测
3. 默认英文

## 常见问题

### Q1: 不配置 API Key 能用吗？

可以。基础模式仍可完成 84 项检查。

### Q2: 免费额度够吗？

通常够用。PageSpeed API 免费额度为每天 25,000 次请求。

### Q3: API Key 会上传到仓库吗？

不会。请使用环境变量或本地 `.env`，并确认 `.gitignore` 已排除敏感文件。

## 相关文档

- [README](../../README.zh-CN.md)
- [API Key 配置](API_KEY_SETUP.md)
- [免费额度说明](QUOTA.md)
