# 技术 SEO 增强检查项 (4 项)

技术 SEO 增强检查确保网站采用现代优化技术,提高性能和国际化支持。

---

## 1. Hreflang标签

### TE1 Hreflang多语言/多地区配置

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析 `<link rel="alternate" hreflang="...">` |
| 对应信号 | 国际SEO |
| 评分标准 | 多语言站点有hreflang🟢 / 单语言站点N/A / 多语言但无🔴 |

**原理**: Hreflang标签告诉Google不同语言/地区版本的关系,避免重复内容问题并提高国际用户体验。

**检查要点:**
- 是否检测到多个语言版本
- hreflang标签是否双向引用
- 是否包含 `x-default` 标签

**正确实现:**
```html
<!-- 中文页面 -->
<link rel="alternate" hreflang="zh-CN" href="https://example.com/cn/" />
<link rel="alternate" hreflang="en-US" href="https://example.com/us/" />
<link rel="alternate" hreflang="x-default" href="https://example.com/" />

<!-- 英文页面也需要相同的标签 -->
```

---

## 2. 服务器渲染检测

### TE2 SSR vs CSR检测

| 属性 | 值 |
|------|-----|
| 执行方式 | 对比初始HTML和完全加载后的DOM |
| 对应信号 | 爬虫友好度 |
| 评分标准 | 主要内容服务端渲染🟢 / 部分客户端🟡 / 完全客户端🔴 |

**原理**: 服务端渲染(SSR)让爬虫直接抓取到完整HTML,而客户端渲染(CSR)依赖JavaScript可能导致内容抓取不完整。

**检测方法:**
```bash
# 检查初始HTML源代码
curl -s https://example.com | grep -i "<h1>"

# 如果找不到主要内容,说明是客户端渲染
```

**评判标准:**
- 🟢 主要内容(标题、正文)在HTML源代码中可见
- 🟡 框架在源代码中,内容动态加载
- 🔴 源代码几乎是空的,完全依赖JS

---

## 3. 图片格式优化

### TE3 现代图片格式使用

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析图片src和source标签 |
| 对应信号 | 性能优化 |
| 评分标准 | 使用WebP/AVIF🟢 / 使用JPEG/PNG但有picture标签🟡 / 仅JPEG/PNG🔴 |

**原理**: WebP和AVIF等现代格式在相同质量下文件大小比JPEG/PNG小30-50%,显著提高加载速度。

**检查要点:**
- 是否直接使用 `.webp` 或 `.avif`
- 是否使用 `<picture>` 标签提供多格式回退

**最佳实践:**
```html
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="描述">
</picture>
```

---

## 4. 浏览器缓存配置

### TE4 Cache-Control和Expires检查

| 属性 | 值 |
|------|-----|
| 执行方式 | `curl -I` 检查HTTP响应头 |
| 对应信号 | 性能优化 |
| 评分标准 | 静态资源有缓存头🟢 / 部分有🟡 / 无🔴 |

**原理**: 正确配置缓存让浏览器存储静态资源,减少重复请求,提高回访用户的加载速度。

**检测方法:**
```bash
curl -I https://example.com/style.css | grep -i "cache-control"
```

**推荐配置:**
```
# 静态资源 (CSS, JS, 图片)
Cache-Control: public, max-age=31536000, immutable

# HTML 页面
Cache-Control: public, max-age=3600, must-revalidate
```

**评判标准:**
- 🟢 静态资源 max-age ≥ 1年, HTML max-age ≥ 1小时
- 🟡 有缓存头但时间较短
- 🔴 无缓存头或 `no-cache`

---

## 检查项汇总

| ID | 检查项 | 评分标准 |
|----|--------|----------|
| TE1 | Hreflang标签 | 多语言站有🟢 |
| TE2 | 服务器渲染 | 主要内容SSR🟢 |
| TE3 | 现代图片格式 | 使用WebP/AVIF🟢 |
| TE4 | 浏览器缓存 | 正确配置🟢 |
