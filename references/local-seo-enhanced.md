# 本地 SEO 增强检查项 (3 项)

本地 SEO 优化帮助实体店铺在本地搜索中获得更好的排名。

---

## 1. LocalBusiness Schema

### L1 LocalBusiness结构化数据

| 属性 | 值 |
|------|-----|
| 执行方式 | 解析 JSON-LD 中的 `@type: LocalBusiness` |
| 对应信号 | 本地搜索展示 |
| 评分标准 | 有完整LocalBusiness Schema🟢 / 部分🟡 / 无🔴 |

**原理**: LocalBusiness结构化数据帮助Google理解实体店信息,提高在Google Maps和本地搜索中的展示。

**必需字段:**
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "店铺名称",
  "image": "店铺图片URL",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "街道地址",
    "addressLocality": "城市",
    "addressRegion": "省份",
    "postalCode": "邮编",
    "addressCountry": "国家"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 40.75,
    "longitude": -73.98
  },
  "telephone": "+1-234-567-8900",
  "openingHours": "Mo,Tu,We,Th,Fr 09:00-17:00"
}
```

---

## 2. Google Maps嵌入

### L2 Google Maps地图嵌入

| 属性 | 值 |
|------|-----|
| 执行方式 | HTML 解析检查 `<iframe>` 中是否包含 google.com/maps |
| 对应信号 | 用户体验和本地相关性 |
| 评分标准 | 有地图嵌入🟢 / 无🟡 |

**原理**: 嵌入Google Maps提高用户体验,同时向Google发送本地相关性信号。

**实现方式:**
```html
<iframe 
  src="https://www.google.com/maps/embed?pb=..."
  width="600" 
  height="450" 
  style="border:0;" 
  allowfullscreen="" 
  loading="lazy">
</iframe>
```

---

## 3. NAP一致性

### L3 名称/地址/电话一致性检查

| 属性 | 值 |
|------|-----|
| 执行方式 | AI 提取页面中所有NAP信息并对比 |
| 对应信号 | 本地SEO信任度 |
| 评分标准 | 所有位置NAP一致🟢 / 有差异🔴 |

**原理**: Google对比网页、Schema、Google我的商家中的NAP信息,不一致会降低本地排名。

**检查点:**
- 页头/页脚联系信息
- Schema标记中的信息  
- 联系页面的信息
- 格式是否一致(如电话号码格式)

**一致性示例:**
```
✅ 正确:
网站: 北京市朝阳区建国路1号 | +86-10-1234-5678
Schema: 北京市朝阳区建国路1号 | +86-10-1234-5678

❌ 错误:
网站: 北京朝阳建国路1号 | 010-1234-5678
Schema: 北京市朝阳区建国路1号 | +86-10-1234-5678
```

---

## 检查项汇总

| ID | 检查项 | 评分标准 |
|----|--------|----------|
| L1 | LocalBusiness Schema | 完整🟢 |
| L2 | Google Maps嵌入 | 有🟢 |
| L3 | NAP一致性 | 一致🟢 |
