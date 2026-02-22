# API Key Setup Guide

**Languages**: [English](API_KEY_SETUP.md) | [简体中文](../zh-CN/API_KEY_SETUP.md)

## Why Configure API Key

With `PAGE_SPEED_API_KEY`, you unlock full mode (92 checks), including Core Web Vitals and PageSpeed scores.

## Quick Setup

### macOS / Linux

```bash
# Temporary (current shell)
export PAGE_SPEED_API_KEY="your_api_key_here"

# Persistent (zsh)
echo 'export PAGE_SPEED_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

### Windows PowerShell

```powershell
# Temporary
$env:PAGE_SPEED_API_KEY="your_api_key_here"

# Persistent (user level)
[System.Environment]::SetEnvironmentVariable('PAGE_SPEED_API_KEY', 'your_api_key_here', 'User')
```

## How to Get API Key

1. Open [Google Cloud Console](https://console.cloud.google.com/)
2. Create/select a project
3. Enable **PageSpeed Insights API**
4. Create API key (Credentials -> Create Credentials -> API Key)

## Verify Setup

```bash
echo $PAGE_SPEED_API_KEY
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&key=$PAGE_SPEED_API_KEY"
```

## Auto-load from `.env` (v1.4.0+)

If `PAGE_SPEED_API_KEY` is not found in environment variables, the skill will automatically try:

1. `./.env` (current working directory)
2. `~/.claude/skills/seo-audit/.env` (skill directory)

`.env` format example:

```dotenv
PAGE_SPEED_API_KEY="your_api_key_here"
```

## Security Best Practices

- Never commit real API keys
- Use env vars or local `.env`
- Keep `.gitignore` updated for `.env` variants

## FAQ

### Q: Can I run without API key?
Yes. The skill falls back to basic mode (84 checks).

### Q: What is the free quota?
25,000 requests/day. See [QUOTA.md](QUOTA.md).
