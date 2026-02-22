# API Key 配置指南

**语言**: [English](../en/API_KEY_SETUP.md) | [简体中文](API_KEY_SETUP.md)

## 为什么建议配置 API Key

配置 `PAGE_SPEED_API_KEY` 后，可启用完整模式（92 项检查），包含 Core Web Vitals 和 PageSpeed 评分。

## 快速配置

### macOS / Linux

```bash
# 临时配置（当前终端会话）
export PAGE_SPEED_API_KEY="your_api_key_here"

# 永久配置（zsh）
echo 'export PAGE_SPEED_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

### Windows PowerShell

```powershell
# 临时
$env:PAGE_SPEED_API_KEY="your_api_key_here"

# 永久（用户级）
[System.Environment]::SetEnvironmentVariable('PAGE_SPEED_API_KEY', 'your_api_key_here', 'User')
```

## 获取 API Key

1. 打开 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建/选择项目
3. 启用 **PageSpeed Insights API**
4. 创建 API Key（Credentials -> Create Credentials -> API Key）

## 验证配置

```bash
echo $PAGE_SPEED_API_KEY
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&key=$PAGE_SPEED_API_KEY"
```

## `.env` 自动加载（v1.4.0+）

当环境变量中没有 `PAGE_SPEED_API_KEY` 时，Skill 会自动按顺序尝试：

1. `./.env`（当前工作目录）
2. `~/.claude/skills/seo-audit/.env`（Skill 目录）

`.env` 示例：

```dotenv
PAGE_SPEED_API_KEY="your_api_key_here"
```

## 安全建议

- 不要把真实 API Key 写入仓库文件
- 使用环境变量或本地 `.env`
- 确保 `.gitignore` 排除 `.env` 及变体

## 常见问题

### Q: 没有 API Key 还能跑吗？
可以，会自动降级到基础模式（84 项）。

### Q: 免费额度是多少？
每天 25,000 次请求，详见 [QUOTA.md](QUOTA.md)。
