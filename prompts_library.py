# 提示词模板库
# 使用方式：在 Cursor 中输入 /prompts 触发 Skill，或在 Python 中导入使用

PROMpts = {
    # 翻译类
    "translate_japanese": "翻译为日语，保持原文风格",
    "translate_english": "翻译为英语，保持原文风格",
    "translate_korean": "翻译为韩语，保持原文风格",

    # 写作类
    "summarize": "简洁总结以下内容，提取关键信息",
    "expand": "详细展开以下内容，丰富论述",
    "polish": "润色以下文字，提升表达质量",

    # 代码类
    "explain_code": "解释以下代码的功能和工作原理",
    "review_code": "审查以下代码，指出潜在问题和改进建议",
    "generate_tests": "为以下代码生成单元测试",

    # 通用
    "analyze": "分析以下内容，给出优缺点总结",
    "brainstorm": "针对以下主题进行头脑风暴，提出创意想法",
}
