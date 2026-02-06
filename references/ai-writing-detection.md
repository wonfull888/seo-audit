# AI 写作特征检测

用于检测内容是否具有 AI 生成的特征。这些特征会影响 E-E-A-T 评分中的 Experience 维度。

来源: Grammarly (2025), Microsoft 365 Life Hacks (2025), Wikipedia "Signs of AI writing"

---

## 最明显的 AI 特征：Em Dash（破折号）

**Em dash (—) 是最可靠的 AI 写作标志之一。**

### 为什么 Em Dash 暴露 AI 写作

- AI 模型训练数据中包含大量编辑过的书籍和学术论文，这些文本频繁使用 em dash
- AI 使用 em dash 作为句式变化的捷径，替代逗号、冒号或括号
- 大多数人类写作者很少使用 em dash，因为它不是标准键盘按键
- 过度使用 em dash 已成为 ChatGPT 写作的"签名"

### 检测标准

| 频率 | 判断 |
|------|------|
| 每页 0-1 个 | 🟢 正常 |
| 每页 2-3 个 | 🟡 可疑 |
| 每页 4+ 个 | 🔴 高度可疑 |

### 替换建议

| AI 写法 | 人类写法 |
|---------|----------|
| The results—which were surprising—showed... | The results, which were surprising, showed... |
| This approach—unlike traditional methods—allows... | This approach, unlike traditional methods, allows... |
| Communication skills—both written and verbal—are essential | Communication skills (both written and verbal) are essential |

---

## AI 高频动词

| 避免使用 | 替换为 |
|----------|--------|
| delve (into) | explore, examine, look at |
| leverage | use, apply |
| utilize | use |
| optimize | improve |
| facilitate | help, enable |
| foster | encourage, develop |
| bolster | strengthen, support |
| underscore | emphasize, highlight |
| unveil | reveal, show |
| navigate | manage, handle |
| streamline | simplify |
| enhance | improve |
| endeavor | try, attempt |
| ascertain | find out, determine |
| elucidate | explain, clarify |

---

## AI 高频形容词

| 避免使用 | 替换为 |
|----------|--------|
| robust | strong, reliable |
| comprehensive | complete, thorough |
| pivotal | key, important |
| crucial | important, critical |
| vital | important, essential |
| transformative | significant, major |
| cutting-edge | new, advanced |
| groundbreaking | new, original |
| innovative | new, creative |
| seamless | smooth, easy |
| intricate | complex, detailed |
| nuanced | subtle, complex |
| multifaceted | complex, varied |
| holistic | complete, whole |

---

## AI 开头短语

### 必须避免的开头

- "In today's fast-paced world..."
- "In today's digital age..."
- "In an era of..."
- "In the ever-evolving landscape of..."
- "In the realm of..."
- "It's important to note that..."
- "Let's delve into..."
- "Imagine a world where..."

### 必须避免的过渡短语

- "That being said..."
- "With that in mind..."
- "It's worth mentioning that..."
- "At its core..."
- "To put it simply..."
- "In essence..."
- "This begs the question..."

### 必须避免的结尾短语

- "In conclusion..."
- "To sum up..."
- "By [doing X], you can [achieve Y]..."
- "In the final analysis..."
- "All things considered..."
- "At the end of the day..."

---

## AI 结构模式

### 三元素列举

```
❌ "Whether you're a beginner, intermediate, or expert..."
❌ "It's not just about X, it's also about Y and Z..."
```

### By + 动名词结构

```
❌ "By understanding X, you can achieve Y..."
❌ "By leveraging these strategies, you'll see improvement..."
```

### Think of X as Y 类比

```
❌ "Think of SEO as a marathon, not a sprint..."
❌ "Think of your website as a digital storefront..."
```

---

## 空洞修饰词

这些词通常不增加实际意义，应删除或替换：

- absolutely
- actually
- basically
- certainly
- clearly
- definitely
- essentially
- extremely
- fundamentally
- incredibly
- interestingly
- naturally
- obviously
- quite
- really
- significantly
- simply
- surely
- truly
- ultimately
- undoubtedly
- very

---

## 学术风格 AI 特征

| 避免使用 | 替换为 |
|----------|--------|
| shed light on | clarify, explain |
| pave the way for | enable, allow |
| a myriad of | many, various |
| a plethora of | many, several |
| paramount | very important |
| pertaining to | about, regarding |
| prior to | before |
| subsequent to | after |
| in light of | because of, given |
| with respect to | about, for |
| in terms of | regarding, for |
| the fact that | that (或重写) |

---

## 检测清单

在分析文章时，检查以下内容：

### 1. 标点检查
- [ ] Em dash 使用频率是否正常（每页 ≤1）
- [ ] 是否过度使用分号

### 2. 词汇检查
- [ ] 是否包含 AI 高频动词（delve, leverage, utilize 等）
- [ ] 是否包含 AI 高频形容词（robust, comprehensive, pivotal 等）
- [ ] 是否包含空洞修饰词

### 3. 结构检查
- [ ] 开头是否使用 AI 典型短语
- [ ] 是否有 "By + 动名词" 模式
- [ ] 是否有三元素列举模式
- [ ] 结尾是否使用 "In conclusion" 等

### 4. 整体风格
- [ ] 句式是否过于统一
- [ ] 段落长度是否过于一致
- [ ] 是否缺乏口语化表达
- [ ] 是否缺乏具体案例/数据

---

## 评分标准

| 特征数量 | 判断 | 得分 |
|----------|------|------|
| 0-2 个 | 🟢 自然写作 | 100 |
| 3-5 个 | 🟡 轻微 AI 痕迹 | 50 |
| 6+ 个 | 🔴 明显 AI 生成 | 0 |

---

## 自检方法

1. **朗读测试**: 大声朗读，如果听起来不自然，就需要修改
2. **对话测试**: 问自己"我会在和同事对话时这样说吗？"
3. **句式检查**: 确保句子长度有变化
4. **修饰词审计**: 每个修饰词都应该增加实际意义
