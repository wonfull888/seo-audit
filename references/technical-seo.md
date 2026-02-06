# 技术 SEO 检查项（25 项）

技术 SEO 确保搜索引擎能够正确抓取、索引和理解网站。

## 目录

1. [可发现性与索引](#1-可发现性与索引8-项)
2. [技术性能 Core Web Vitals](#2-技术性能-core-web-vitals8-项)
3. [安全性与基础设施](#3-安全性与基础设施4-项)
4. [结构化数据](#4-结构化数据5-项)

---

## 1. 可发现性与索引（8 项）

### T1.1 robots.txt 存在性与配置

| 属性 | 值 |
|------|-----|
| 执行方式 | `curl {domain}/robots.txt` |
| 对应信号 | 基础可抓取性 |
| 评分标准 | 存在且配置合理🟢 / 存在但有问题🟡 / 不存在🔴 |

**检查要点：**
- 文件是否存在且可访问
- 是否意外阻止了重要页面
- 是否引用了 sitemap.xml

**正确示例：**
```
User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /

Sitemap: https://example.com/sitemap.xml
```

---

### T1.2 sitemap.xml 存在性与格式

| 属性 | 值 |
|------|-----|
| 执行方式 | `curl {domain}/sitemap.xml` |
| 对应信号 | 索引发现 |
| 评分标准 | 存在且格式正确🟢 / 存在但有问题🟡 / 不存在🔴 |

**检查要点：**
- 文件是否存在
- XML 格式是否正确
- 是否包含主要页面

---

### T1.3 页面可访问性（HTTP 状态码）

| 属性 | 值 |
|------|-----|
| 执行方式 | `curl -I {url}` |
| 对应信号 | `isErrorPage` |
| 评分标准 | 200 OK🟢 / 301/302🟡 / 4xx/5xx🔴 |

**检查要点：**
- 所有分析页面返回 200 状态码
- 无软 404 错误

---

### T1.4 noindex 标签检查

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `<meta name="robots">` |
| 对应信号 | 索引控制 |
| 评分标准 | 无 noindex🟢 / 有 noindex🔴（除非有意） |

**检查要点：**
- 主要页面不应有 noindex
- 检查 HTTP 头中的 X-Robots-Tag

---

### T1.5 Canonical 标签正确性

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `<link rel="canonical">` |
| 对应信号 | `CompositeDoc` 信号整合 |
| 评分标准 | 存在且正确🟢 / 存在但指向错误🔴 / 不存在🟡 |

**检查要点：**
- 每个页面应有 canonical 标签
- 自引用或指向正确的规范版本
- 避免 canonical 链

---

### T1.6 HTTP → HTTPS 重定向

| 属性 | 值 |
|------|-----|
| 执行方式 | `curl -I http://{domain}` |
| 对应信号 | `badSslCertificate` |
| 评分标准 | 301 重定向到 HTTPS🟢 / 无重定向🔴 |

**检查要点：**
- HTTP 版本应 301 重定向到 HTTPS
- 不应是 302 临时重定向

---

### T1.7 www/non-www 一致性

| 属性 | 值 |
|------|-----|
| 执行方式 | `curl -I http://www.{domain}` 和 `curl -I http://{domain}` |
| 对应信号 | 规范化 |
| 评分标准 | 统一重定向🟢 / 两个版本都可访问🔴 |

**检查要点：**
- 选择一个版本作为规范
- 另一个版本 301 重定向

---

### T1.8 重定向链检测（301/302）

| 属性 | 值 |
|------|-----|
| 执行方式 | `curl -IL {url}` 跟踪跳转 |
| 对应信号 | 信号稀释 |
| 评分标准 | 无重定向链🟢 / 2 跳🟡 / 3+ 跳🔴 |

**检查要点：**
- 重定向不应超过 2 次
- 避免重定向循环

---

## 2. 技术性能 Core Web Vitals（8 项）

### T2.1 PageSpeed 移动端评分

| 属性 | 值 |
|------|-----|
| 执行方式 | PageSpeed API (`strategy=mobile`) |
| 对应信号 | `mobileCwv` |
| 评分标准 | ≥90🟢 / 70-89🟡 / <70🔴 |

---

### T2.2 PageSpeed 桌面端评分

| 属性 | 值 |
|------|-----|
| 执行方式 | PageSpeed API (`strategy=desktop`) |
| 对应信号 | `desktopCwv` |
| 评分标准 | ≥90🟢 / 70-89🟡 / <70🔴 |

---

### T2.3 LCP（最大内容绘制）

| 属性 | 值 |
|------|-----|
| 执行方式 | PageSpeed API |
| 对应信号 | `lcp` |
| 评分标准 | <2.5s🟢 / 2.5-4s🟡 / >4s🔴 |

**优化方向：**
- 优化图片大小和格式
- 使用 CDN
- 预加载关键资源

---

### T2.4 FCP（首次内容绘制）

| 属性 | 值 |
|------|-----|
| 执行方式 | PageSpeed API |
| 对应信号 | FCP |
| 评分标准 | <1.8s🟢 / 1.8-3s🟡 / >3s🔴 |

---

### T2.5 CLS（累积布局偏移）

| 属性 | 值 |
|------|-----|
| 执行方式 | PageSpeed API |
| 对应信号 | `cls` |
| 评分标准 | <0.1🟢 / 0.1-0.25🟡 / >0.25🔴 |

**优化方向：**
- 为图片设置 width/height
- 避免动态插入内容
- 预留广告位空间

---

### T2.6 INP（交互延迟）

| 属性 | 值 |
|------|-----|
| 执行方式 | PageSpeed API |
| 对应信号 | `inp` |
| 评分标准 | <200ms🟢 / 200-500ms🟡 / >500ms🔴 |

---

### T2.7 TBT（总阻塞时间）

| 属性 | 值 |
|------|-----|
| 执行方式 | PageSpeed API |
| 对应信号 | TBT |
| 评分标准 | <200ms🟢 / 200-600ms🟡 / >600ms🔴 |

---

### T2.8 TTFB（首字节时间）

| 属性 | 值 |
|------|-----|
| 执行方式 | PageSpeed API |
| 对应信号 | `time-to-first-byte` |
| 评分标准 | <800ms🟢 / 800-1800ms🟡 / >1800ms🔴 |

---

## 3. 安全性与基础设施（4 项）

### T3.1 HTTPS 强制使用

| 属性 | 值 |
|------|-----|
| 执行方式 | `curl -I {url}` |
| 对应信号 | Trust 基础 |
| 评分标准 | HTTPS🟢 / HTTP🔴 |

---

### T3.2 SSL 证书有效性

| 属性 | 值 |
|------|-----|
| 执行方式 | `curl -I https://{domain}` |
| 对应信号 | `badSslCertificate` |
| 评分标准 | 有效🟢 / 过期或无效🔴 |

---

### T3.3 混合内容检测

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析，检查 `http://` 资源引用 |
| 对应信号 | 安全警告 |
| 评分标准 | 无混合内容🟢 / 有 http:// 资源🔴 |

**检查要点：**
- 图片、脚本、样式表等资源应使用 HTTPS
- 检查 `<img src="http://...">` 等模式

---

### T3.4 viewport 移动端配置

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `<meta name="viewport">` |
| 对应信号 | `isSmartphoneOptimized` |
| 评分标准 | 正确配置🟢 / 缺失🔴 |

**正确配置：**
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

---

## 4. 结构化数据（5 项）

### T4.1 JSON-LD 结构化数据存在

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `<script type="application/ld+json">` |
| 对应信号 | `richsnippet` |
| 评分标准 | 有🟢 / 无🟡 |

---

### T4.2 Organization Schema

| 属性 | 值 |
|------|-----|
| 执行方式 | 解析 JSON-LD 中的 `@type: Organization` |
| 对应信号 | 品牌实体信号 |
| 评分标准 | 有🟢 / 无🟡 |

**示例：**
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "公司名称",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png"
}
```

---

### T4.3 Article Schema（文章页）

| 属性 | 值 |
|------|-----|
| 执行方式 | 解析 JSON-LD 中的 `@type: Article` |
| 对应信号 | 内容类型识别 |
| 评分标准 | 文章页有🟢 / 文章页无🟡 |

---

### T4.4 Breadcrumb Schema

| 属性 | 值 |
|------|-----|
| 执行方式 | 解析 JSON-LD 中的 `@type: BreadcrumbList` |
| 对应信号 | 导航结构 |
| 评分标准 | 有🟢 / 无🟡 |

---

### T4.5 Author Schema (Person)

| 属性 | 值 |
|------|-----|
| 执行方式 | 解析 JSON-LD 中的 `@type: Person` |
| 对应信号 | `isAuthor` |
| 评分标准 | 文章页有🟢 / 文章页无🟡 |

**示例：**
```json
{
  "@type": "Article",
  "author": {
    "@type": "Person",
    "name": "作者姓名",
    "url": "https://example.com/author/name"
  }
}
```

---

## 检查项汇总

| ID | 检查项 | 类别 | 评分标准 |
|----|--------|------|----------|
| T1.1 | robots.txt | 可发现性 | 存在且合理🟢 |
| T1.2 | sitemap.xml | 可发现性 | 存在且正确🟢 |
| T1.3 | HTTP 状态码 | 可发现性 | 200🟢 |
| T1.4 | noindex 检查 | 可发现性 | 无🟢 |
| T1.5 | Canonical 标签 | 可发现性 | 正确🟢 |
| T1.6 | HTTPS 重定向 | 可发现性 | 301🟢 |
| T1.7 | www 一致性 | 可发现性 | 统一🟢 |
| T1.8 | 重定向链 | 可发现性 | ≤2跳🟢 |
| T2.1 | PageSpeed 移动端 | 性能 | ≥90🟢 |
| T2.2 | PageSpeed 桌面端 | 性能 | ≥90🟢 |
| T2.3 | LCP | 性能 | <2.5s🟢 |
| T2.4 | FCP | 性能 | <1.8s🟢 |
| T2.5 | CLS | 性能 | <0.1🟢 |
| T2.6 | INP | 性能 | <200ms🟢 |
| T2.7 | TBT | 性能 | <200ms🟢 |
| T2.8 | TTFB | 性能 | <800ms🟢 |
| T3.1 | HTTPS | 安全 | 是🟢 |
| T3.2 | SSL 证书 | 安全 | 有效🟢 |
| T3.3 | 混合内容 | 安全 | 无🟢 |
| T3.4 | viewport | 安全 | 正确🟢 |
| T4.1 | JSON-LD 存在 | 结构化 | 有🟢 |
| T4.2 | Organization | 结构化 | 有🟢 |
| T4.3 | Article | 结构化 | 有🟢 |
| T4.4 | Breadcrumb | 结构化 | 有🟢 |
| T4.5 | Author | 结构化 | 有🟢 |
