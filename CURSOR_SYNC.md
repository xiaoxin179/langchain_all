# Cursor Skills 同步说明

## 当前状态
提示词模板已存储在 `cursor-skills/prompts/SKILL.md`

## 如何同步到其他电脑

### 步骤 1：Clone 项目
```bash
git clone <你的仓库地址>
cd langchain
```

### 步骤 2：复制 Skills 到 Cursor 目录
```powershell
# Windows PowerShell
Copy-Item -Recurse "cursor-skills\*" "$env:USERPROFILE\.cursor\skills-cursor\"

# 或者 CMD
xcopy /E /I cursor-skills\* %USERPROFILE%\.cursor\skills-cursor\
```

```bash
# macOS/Linux
cp -r cursor-skills/* ~/.cursor/skills-cursor/
```

### 步骤 3：重启 Cursor

---

## 可用提示词模板

### 翻译类
- `translate_japanese` → 翻译为日语
- `translate_english` → 翻译为英语
- `translate_korean` → 翻译为韩语

### 写作类
- `summarize` → 简洁总结
- `expand` → 详细展开
- `polish` → 润色文字

### 代码类
- `explain_code` → 解释代码
- `review_code` → 审查代码
- `generate_tests` → 生成测试

### 通用类
- `analyze` → 分析内容
- `brainstorm` → 头脑风暴

## 触发方式
在 Cursor 对话中输入 `/prompts` 即可调用
