# 快速确认机制说明

## 适用场景

当报告语言自动检测为低置信度（中文字符占比 10%-30%）时，给出快速确认提示。

## 设计原则

1. 不阻塞主流程
2. 提供显式覆盖能力（`--en` / `--zh`）
3. 低认知负担，默认值可直接继续

## 推荐实现

```python
lang_info = determine_report_language(user_input)

if lang_info["confidence"] in ("explicit", "high"):
    selected_lang = lang_info["language"]
else:
    # 低置信度：显示提示并使用默认值
    print("""
⚠️ Cannot auto-detect language with high confidence.
Select report language:
1. English (recommended)
2. 中文
Default: English
""")
    selected_lang = lang_info["language"]
```

## 可选交互增强

若运行环境支持交互选择，可使用 question 工具进行选项确认；若不支持，则按默认值继续并建议用户下次添加显式标志。

## 用户提示模板

```text
⚠️ Cannot auto-detect language with high confidence.
Select report language:
1. English (recommended)
2. 中文
Default: English
```
