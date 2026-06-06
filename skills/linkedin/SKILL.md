---
name: linkedin-publish
description: 直接从草稿目录为文章生成 LinkedIn 发布所需的素材
trigger: "发布到 LinkedIn"
---

## 目标

直接从项目的 `draft/` 目录读取文章，生成 LinkedIn 发布所需的素材，输出到 `~/.blog-workspace/linkedin/` 目录：
- `short-version.md`：英文缩略版帖子
- `en-banner.png`：从 `draft/` 复制而来

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/article.md`**：文章正文（中文）
- **`draft/metadata.md`**：提取：
  - `英文标题` → `en-title`
  - `en-slug` = `en-title` 转 kebab-case（冒号及标点去掉或替换为 `-`）

canonical URL 格式：`https://CodePlato3721.github.io/en/post/{en-slug}/`

### 2. 撰写缩略版正文

阅读文章全文，撰写适合 LinkedIn 的英文缩略版：

- 长度：300～500 词
- 风格：直接、有观点，适合职业社交平台
- 结构：开门见山抛出核心观点 → 1～2 个关键论据或例子 → 简短结论
- 结尾固定附上：

```
Read the full article: {canonical URL}
```

> 注：如果英文版尚未发布到个人博客，可在发布后手动确认该链接可访问。

### 3. 准备输出目录

确保 `~/.blog-workspace/linkedin/` 目录存在（不存在则新建）：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\linkedin"
```

### 4. 写出 short-version.md

将缩略版内容写入 `~/.blog-workspace/linkedin/short-version.md`。

### 5. 复制封面图

将 `draft/en-banner.png` 复制到 `~/.blog-workspace/linkedin/en-banner.png`：

```powershell
Copy-Item "draft\en-banner.png" "$env:USERPROFILE\.blog-workspace\linkedin\en-banner.png"
```

### 6. 确认输出

列出 `~/.blog-workspace/linkedin/`，确认 `short-version.md` 和 `en-banner.png` 均已就绪。
