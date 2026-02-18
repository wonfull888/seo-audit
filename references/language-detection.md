# 语言检测规则

## 目标

在 SEO 诊断开始前，确定报告语言，减少用户确认成本，并提供显式覆盖能力。

## 检测优先级

1. 显式标志（最高优先级）
   - `--en` / `--english` -> `en`
   - `--zh` / `--zh-CN` / `--中文` -> `zh-CN`
2. 自动检测（无显式标志时）
3. 默认语言（无法高置信度判断时）-> `en`

## 自动检测方法

### 方法 A：中文字符占比

```python
def detect_language_by_char_ratio(text: str) -> dict:
    chinese_chars = len([c for c in text if "\u4e00" <= c <= "\u9fff"])
    total_chars = len([c for c in text if c.strip()])

    if total_chars == 0:
        return {"language": "en", "confidence": "low", "method": "auto"}

    ratio = chinese_chars / total_chars

    if ratio > 0.30:
        return {"language": "zh-CN", "confidence": "high", "method": "auto"}
    if ratio < 0.10:
        return {"language": "en", "confidence": "high", "method": "auto"}
    return {"language": "en", "confidence": "low", "method": "auto"}
```

### 方法 B：关键词辅助（可选）

- 中文关键词：`诊断`、`审计`、`网站`、`优化`
- 英文关键词：`audit`、`diagnose`、`check`、`optimize`

## 置信度行为

| 置信度 | 条件 | 行为 |
|--------|------|------|
| high | 中文占比 >30% 或 <10% | 直接使用检测结果，展示提示 |
| low | 中文占比 10%-30% | 显示快速确认提示，按默认值继续 |

## 伪代码

```python
def determine_report_language(user_message: str) -> dict:
    text = user_message.lower()

    if "--en" in text or "--english" in text:
        return {"language": "en", "confidence": "explicit", "method": "flag"}
    if "--zh" in text or "--zh-cn" in text or "--中文" in user_message:
        return {"language": "zh-CN", "confidence": "explicit", "method": "flag"}

    return detect_language_by_char_ratio(user_message)
```

## 提示文案

高置信度：

```text
📝 Report language: English (auto-detected)
   To override: add --zh
```

低置信度：

```text
⚠️ Cannot auto-detect language with high confidence.
Select report language:
1. English (recommended)
2. 中文
Default: English
```
