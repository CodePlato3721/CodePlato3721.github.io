---
name: devto-publish
description: 将英文博客文章发布到 dev.to
trigger: "发布到 dev.to" 或 "发布英文文章"
---

## 目标

调用 `scripts/devto.py` 将英文文章发布到 dev.to。

## 前提

- `skills/.env` 中已设置 `DEVTO_API_KEY`

## 步骤

### 1. 确认文章路径

英文文章路径格式：
```
content/en/post/{en-slug}/index.md
```

### 2. 运行发布脚本

在项目根目录下执行：

```powershell
skills\.venv\Scripts\python.exe skills\devto\scripts\devto.py content\en\post\{en-slug}\index.md
```

### 3. 确认结果

脚本成功后会输出：
```
published: https://dev.to/...
```

如果报错，检查：
- `DEVTO_API_KEY` 是否正确设置
- 文章路径是否存在
- 文章 `draft` 是否为 `false`
