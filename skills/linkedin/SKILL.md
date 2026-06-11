---
name: linkedin-publish
description: 直接从草稿目录为文章生成 LinkedIn 发布所需的素材
trigger: "发布到 LinkedIn"
---

## 目标

直接从项目的 `draft/` 目录读取文章，生成 LinkedIn 发布所需的素材，输出到 `~/.blog-workspace/linkedin/` 目录：
- `short-version.md`：英文缩略版帖子
- `metadata.md`：文章元数据（英文标题）
- `banner.png`：从 `draft/en-banner.png` 复制后重命名而来

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/metadata.md`**：提取：
  - `英文标题` → `en-title`
  - `en-slug` = `en-title` 转 kebab-case（冒号及标点去掉或替换为 `-`）

### 2. 撰写缩略版正文

读取 `draft/en-article.md`，撰写适合 LinkedIn 的英文缩略版：

- 长度：300～500 词
- 风格：直接、有观点，适合职业社交平台
- 结构：开门见山抛出核心观点 → 1～2 个关键论据或例子 → 简短结论
- 结尾按以下优先级决定是否附上链接：
  1. 如果 `draft/metadata.md` 的「首发」中 `url` 有值，使用该首发 URL
  2. 如果英文版已发布到本博客（`en-slug` 对应页面存在），使用 `https://CodePlato3721.github.io/en/post/{en-slug}/`
  3. 以上都没有，则不附链接

  有链接时结尾附上：

  ```
  Read the full article: {URL}
  ```

### 3. 准备输出目录

确保 `~/.blog-workspace/linkedin/` 目录存在（不存在则新建）：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\linkedin"
```

### 4. 写出 short-version.md

将缩略版内容写入 `~/.blog-workspace/linkedin/short-version.md`。

### 5. 写出 metadata.md

基于 `draft/en-article.md` 生成一段 100 词以内的英文摘要（`short-summary`），概括文章核心观点，语言简洁直接。

将以下内容写入 `~/.blog-workspace/linkedin/metadata.md`：

```markdown
# 英文标题
{en-title}

# 短摘要
{short-summary}
```

### 6. 复制封面图

将 `draft/en-banner.png` 复制到 `~/.blog-workspace/linkedin/banner.png`：

```powershell
Copy-Item "draft\en-banner.png" "$env:USERPROFILE\.blog-workspace\linkedin\banner.png"
```

### 7. 确认输出

列出 `~/.blog-workspace/linkedin/`，确认 `short-version.md`、`metadata.md` 和 `banner.png` 均已就绪。
