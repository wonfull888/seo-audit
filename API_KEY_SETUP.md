# API Key 配置

## 为什么要配置 API Key？

Google PageSpeed Insights API 提供 **每天 25,000 次免费请求**，个人使用完全够用！

| 使用频率 | 每月请求次数 | 免费额度 |
|----------|---------------|----------|
| 每天诊断 1 个网站 | 1 × 6 = 6 次 | 25,000 / 6 = 4,166 天 ≈ **11 年** |
| 每天诊断 10 个网站 | 10 × 6 = 60 次 | 25,000 / 60 = 416 天 ≈ **14 个月** |
| 每天诊断 100 个网站 | 100 × 6 = 600 次 | 25,000 / 600 = 41 天 ≈ **1.5 个月** |

> **重要**: 每个 URL 诊断需要调用 PageSpeed API 2 次（移动端 + 桌面端），3 个页面 = 6 次

### 配置 vs 不配置

| 功能 | 配置 API Key | 不配置 |
|------|-------------|--------|
| 检查项数 | 73 项 | 65 项（跳过 Core Web Vitals） |
| 技术 SEO 权重 | 30% | 25% |
| E-E-A-T 权重 | 50% | 55% |
| 性能数据 | ✅ LCP, FCP, CLS, INP | ❌ 跳过 |
| PageSpeed 评分 | ✅ 移动端 + 桌面端 | ❌ 跳过 |
| 生成报告 | **完整** | **降级模式** |

**建议**：
- ✅ 如果需要完整的 SEO 诊断，**配置 API Key**
- ⚠️ 如果只是快速检查内容质量，**不配置也能用**

## 安全注意事项

如果硬编码 API Key 在代码中并开源，会导致：

- API Key 被滥用
- 配额耗尽
- 产生不必要的费用

## 解决方案

使用环境变量，确保 API Key 不会被提交到 Git。

### 步骤 1：获取 API Key

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建新项目或选择现有项目
3. 启用 PageSpeed Insights API
4. 创建 API Key（Credentials → Create Credentials → API Key）

### 步骤 2：设置环境变量

#### macOS/Linux

```bash
# 临时设置（当前会话有效）
export PAGE_SPEED_API_KEY="your_api_key_here"

# 永久设置（添加到 ~/.zshrc 或 ~/.bashrc）
echo 'export PAGE_SPEED_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

#### Windows PowerShell

```powershell
# 临时设置
$env:PAGE_SPEED_API_KEY="your_api_key_here"

# 永久设置（添加到系统环境变量）
[System.Environment]::SetEnvironmentVariable('PAGE_SPEED_API_KEY', 'your_api_key_here', 'User')
```

### 步骤 3：验证配置

```bash
# 检查环境变量是否设置
echo $PAGE_SPEED_API_KEY  # macOS/Linux
echo $env:PAGE_SPEED_API_KEY  # Windows PowerShell

# 测试 API 调用
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&key=$PAGE_SPEED_API_KEY"
```

### 步骤 4：.gitignore 确保安全

确保 `.gitignore` 包含以下内容：

```gitignore
# 敏感配置
.env
*.env
.env.local
.env.*.local
```

## 使用方式

### 在 Skill 中读取环境变量

```bash
# 如果环境变量存在，使用环境变量
# 否则，提示用户设置
if [ -n "$PAGE_SPEED_API_KEY" ]; then
  API_KEY="$PAGE_SPEED_API_KEY"
else
  echo "⚠️  PAGE_SPEED_API_KEY 环境变量未设置"
  echo "请参考 API_KEY_SETUP.md 设置您的 API Key"
  exit 1
fi

# 调用 PageSpeed API
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${url}&key=${API_KEY}"
```

### 临时覆盖（测试用）

```bash
# 临时设置环境变量进行测试
PAGE_SPEED_API_KEY="your_key_here" /seo-audit https://example.com
```

## 替代方案

如果不想设置环境变量，也可以：

### 方案 A：直接在提示中提供 API Key

```
对 https://example.com 进行 SEO 诊断，PageSpeed API Key: your_key_here
```

### 方案 B：使用本地配置文件

创建 `config.local.json`（不提交到 Git）：

```json
{
  "PAGE_SPEED_API_KEY": "your_api_key_here"
}
```

## FAQ

**Q: 我没有 Google Cloud 账号怎么办？**
A: 可以使用 Google 账号注册 [Google Cloud](https://console.cloud.google.com/)，免费额度通常足够个人使用。

**Q: API Key 会泄露吗？**
A: 只要不提交到 Git，就不会泄露。确保 `.gitignore` 正确配置。

**Q: 免费额度够用吗？**
A: Google PageSpeed Insights API 免费额度通常为每天 25,000 次请求，个人使用完全足够。

**Q: 超出配额怎么办？**
A: 可以：
1. 提升配额（付费）
2. 减少测试频率
3. 使用缓存（相同 URL 不重复请求）

## 安全检查清单

- [ ] API Key 未硬编码在任何 `.md` 文件中
- [ ] `.gitignore` 包含 `.env` 和相关文件
- [ ] `git status` 检查，确保没有敏感文件被跟踪
- [ ] 使用 `git grep -i "api_key"` 搜索，确保没有泄露

---

**重要**: 永远不要将包含真实 API Key 的文件提交到 Git 仓库！
