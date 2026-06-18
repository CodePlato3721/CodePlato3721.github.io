---
name: linkedin-publish
description: 直接从草稿目录为文章生成 LinkedIn 发布所需的素材
trigger: "发布linkedin:<代号>"
---

## 触发格式

```
发布linkedin:<代号>
```

触发后，从触发短语中提取 `<代号>`，所有文件路径均以 `draft/<代号>/` 为根目录。

## 目标

直接从项目的 `draft/<代号>/` 目录读取文章，生成 LinkedIn 发布所需的素材，输出到 `~/.blog-workspace/<代号>/linkedin/` 目录：
- `metadata.md`：文章标题
- `short-version.md`：英文缩略版帖子
- `banner.png`：从 `draft/<代号>/` 复制而来

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/<代号>/cn-article.md`**：文章正文（中文）
- **`draft/<代号>/metadata.md`**：提取：
  - `英文标题` → `en-title`
  - `en-slug` = `en-title` 转 kebab-case（冒号及标点去掉或替换为 `-`）
  - `# 首发` 段落（可选）→ 提取 `website` 和 `url`

### 2. 确定原文链接（Canonical URL）

检查 `metadata.md` 中是否存在 `# 首发` 段落且 `website` 与 `url` 均有值：

- **首发路线**（有首发信息）：canonical URL = `url` 的值
- **博客路线**（无首发信息）：canonical URL = `https://CodePlato3721.github.io/en/post/{en-slug}/`

### 3. 撰写缩略版正文

阅读文章全文，撰写适合 LinkedIn 的英文缩略版：

- 长度：300～500 词
- 风格：直接、有观点，适合职业社交平台
- 结构：开门见山抛出核心观点 → 1～2 个关键论据或例子 → 简短结论
- 结尾固定附上：

```
Read the full article: {canonical URL}
```

> 注：如果英文版尚未发布到个人博客，可在发布后手动确认该链接可访问。

### 4. 准备输出目录

确保 `~/.blog-workspace/<代号>/linkedin/` 目录存在（不存在则新建）：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\<代号>\linkedin" | Out-Null
```

### 5. 写出 metadata.md

根据文章正文，生成 **Metadescription**：160 字符以内的英文描述，概括文章核心主题，适合作为 SEO meta description。

将以下内容写入 `~/.blog-workspace/<代号>/linkedin/metadata.md`：

```markdown
## Title
{en-title}

## Metadescription
{生成的 metadescription，160 字符以内}
```

### 6. 写出 short-version.md

将缩略版内容写入 `~/.blog-workspace/<代号>/linkedin/short-version.md`。

### 7. 复制封面图

将 `draft/<代号>/en-banner.png` 复制到输出目录并重命名为 `banner.png`：

```powershell
Copy-Item "draft\<代号>\en-banner.png" "$env:USERPROFILE\.blog-workspace\<代号>\linkedin\banner.png"
```

### 8. 确认输出

列出 `~/.blog-workspace/<代号>/linkedin/`，确认 `metadata.md`、`short-version.md`、`banner.png` 均已就绪。
