# SEO Audit Skill - 产品说明

SEO Audit Skill 是一个基于 Google、Ahrefs、微软官方搜索指南设计的证据驱动型 SEO 诊断工具。

文档来源:
- [Google 搜索指南](https://developers.google.com/search/docs?hl=zh-cn)
- [Ahrefs 82项 SEO+AI 搜索清单](https://ahrefs.com/blog/seo-ai-search-checklist/)
- [微软 AEO & GEO 指南](https://about.ads.microsoft.com/content/dam/sites/msa-about/global/common/content-lib/pdf/from-discovery-to-influence-a-guide-to-aeo-and-geo.pdf)

**核心价值**:传统 SEO 工具只关注技术指标,忽略了 Google 真正看重的 E-E-A-T 信号。

---

## 产品功能

### 核心功能

| 功能 | 描述 | 状态 |
|------|------|------|
| **四维度诊断** | 技术 SEO(29项) + 页面元素(27项) + E-E-A-T(33项) + 本地SEO(3项) | ✅ 已实现 |
| **双模式支持** | 完整模式(92项) + 基础模式(84项,零配置) | ✅ 已实现 |
| **双语报告** | 默认中文,可选英文 | ✅ 已实现 |
| **优先级分类** | P0(必须立即修复)/P1(尽快修复)/P2(计划优化) | ✅ 已实现 |
| **优化建议** | 每个问题附带代码示例和最佳实践 | ✅ 已实现 |

### E-E-A-T 子维度

| 子维度 | 检查项 | 占E-E-A-T权重 | 状态 |
|--------|--------|--------------|------|
| Trust(信任度) | 10 项 | 40% | ✅ |
| Experience(经验) | 7 项 | 20% | ✅ |
| Expertise(专业度) | 10 项 | 20% | ✅ |
| Authoritativeness(权威性) | 6 项 | 20% | ✅ |

**v1.1.0更新**: Trust新增2项(退款保证、安全徽章),Expertise新增3项(可扫描性、术语定义、多媒体)

---

## 适用范围

### 目标用户

| 用户类型 | 使用场景 | 推荐模式 |
|----------|----------|----------|
| **个人站长** | 诊断自己的网站 SEO 问题 | 基础模式或完整模式 |
| **SEO 从业者** | 快速分析客户网站 | 完整模式(批量诊断) |
| **内容创作者** | 检查内容质量(E-E-A-T) | 基础模式即可 |
| **开发者** | 性能优化参考 | 完整模式(需要 Core Web Vitals) |

### 不适用场景

- ❌ **大规模 SEO 监控平台** - Skill 设计为单次诊断工具
- ❌ **竞品持续对比** - 需要专门的监控工具
- ❌ **关键词排名跟踪** - 需要 SERP 跟踪功能

---

## 技术依赖

### 必需依赖

| 依赖 | 用途 | 说明 |
|------|------|------|
| **curl** | HTTP 请求 | robots.txt, sitemap.xml, HTTP headers |
| **WebFetch** | 获取页面 HTML | AI 内置工具 |

### 可选依赖

| 依赖 | 用途 | 获取方式 |
|------|------|----------|
| **PageSpeed API** | Core Web Vitals 数据 | Google Cloud Console(免费 25,000 次/天) |
| **PAGE_SPEED_API_KEY** | 存储 API Key | 环境变量 |

---

## 使用限制

### 免费额度

| 模式 | PageSpeed 调用 | 每月使用量(10 个网站) | 免费额度 |
|------|---------------|------------------------|----------|
| 完整模式 | 6 次/网站 | 1,800 次 | 约 14 个月 |
| 基础模式 | 0 次 | 0 次 | 无限制 |

### API Key 要求

| 模式 | API Key | 说明 |
|------|----------|------|
| 完整模式 | **必需** | 需要配置环境变量 |
| 基础模式 | 可选 | 无需配置,开箱即用 |

---

## 版本信息

| 项目 | 版本 | 状态 |
|------|------|------|
| Skill 版本 | 1.3.0 | 当前版本 |
| 开源状态 | MIT License | 可开源 |
| API Key | 需自行申请 | 不包含密钥 |

---

## 后续规划

### v1.3.0 - 已开发完成（待发布）

✅ **国际化基础完成**
- 英文 README 默认展示（GitHub 首页）
- 中文 README 独立为 `README.zh-CN.md`
- 文档双语目录：`docs/en/` 与 `docs/zh-CN/`

✅ **报告语言智能选择**
- 支持显式标志：`--en` / `--zh`
- 支持自动语言检测（高置信度静默使用）
- 低置信度场景支持快速确认提示

✅ **双语报告模板与示例**
- `references/report-template.en.md`
- `references/report-template.zh-CN.md`
- `assets/example-report.en.md`

### v1.4.0 - 智能网站识别（规划中）

**核心目标**：按网站类型自动选择更有代表性的页面进行诊断。

**主要功能**:
- [ ] 网站类型识别：SaaS / E-commerce / Content / Corporate / Tool
- [ ] 动态页面选择：按类型优先抓取关键业务页面
  - SaaS：功能页、解决方案页
  - 电商：商品详情页、集合页
  - 企业站：服务页、案例页
- [ ] **文章页强制抓取（Mandatory）**：无论何种类型，都必须包含文章页用于内容质量与 E-E-A-T 评估
- [ ] 低置信度识别时的用户确认机制
- [ ] 回退策略：站点结构不清晰时自动使用 sitemap + 首页链接混合启发式

**预估周期**：5-7 天

### v1.5.0+（候选）

- [ ] 批量网址诊断
- [ ] 竞品对比分析
- [ ] 趋势对比与历史追踪
- [ ] 报告导出增强（PDF/JSON/HTML）

---

## 参考文档

| 文档 | 说明 |
|------|------|
| [README.md](./README.md) | GitHub 项目说明 |
| [USAGE.md](./USAGE.md) | 详细使用指南 |
| [TASKS_v1.3.0.md](./TASKS_v1.3.0.md) | v1.3.0 任务拆解 |
| [API_KEY_SETUP.md](./API_KEY_SETUP.md) | API Key 配置 |
| [QUOTA.md](./QUOTA.md) | 免费额度说明 |
| [CHANGELOG.md](./CHANGELOG.md) | 版本历史 |
| [SKILL.md](./SKILL.md) | Skill 主文件 |

---

## 开源信息

| 项目 | 信息 |
|------|------|
| 仓库名 | `seo-audit` |
| 许可证 | MIT License |
| API Key | 用户自行配置(不包含在仓库中) |
| 安全 | `.gitignore` 已配置忽略敏感文件 |

---

**产品完成时间**: 2026-02-10  
**当前版本**: 1.3.0  
**最新更新**: 完成国际化改造（默认英文文档 + 智能语言检测 + 双语模板）
