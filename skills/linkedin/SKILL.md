---
name: linkedin-publish
description: 为指定的英文博客文章生成 LinkedIn 发布所需的素材
trigger: "发布到 LinkedIn"
---

## 目标

为一篇英文博客文章生成 LinkedIn 发布所需的素材，输出到 `~/.blog-workspace/linkedin/` 目录：
- `short-version.md`：文章的英文缩略版，结尾附完整版链接
- `en-banner.png`：从 `draft/` 复制而来

## 步骤

### 1. 找到英文文章文件

根据文章标题，定位英文文章文件：
```
content/en/post/{en-slug}/index.md
```

### 2. 读取 frontmatter

从文章文件中提取：
- `title`：英文标题
- `date`：发布日期

canonical URL 格式：`https://CodePlato3721.github.io/en/post/{en-slug}/`

### 3. 撰写缩略版正文

阅读英文文章全文，撰写适合 LinkedIn 的缩略版：

- 长度：300～500 词
- 风格：直接、有观点，适合职业社交平台
- 结构：开门见山抛出核心观点 → 1～2 个关键论据或例子 → 简短结论
- 结尾固定附上：

```
Read the full article: {canonical URL}
```

### 4. 准备输出目录

确保 `~/.blog-workspace/linkedin/` 目录存在（不存在则新建）：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\linkedin"
```

### 5. 写出 short-version.md

将缩略版内容写入 `~/.blog-workspace/linkedin/short-version.md`。

### 6. 复制封面图

将 `~/.blog-workspace/draft/en-banner.png` 复制到 `~/.blog-workspace/linkedin/en-banner.png`：

```powershell
Copy-Item "$env:USERPROFILE\.blog-workspace\draft\en-banner.png" `
          "$env:USERPROFILE\.blog-workspace\linkedin\en-banner.png"
```

### 7. 确认输出

列出 `~/.blog-workspace/linkedin/`，确认 `short-version.md` 和 `en-banner.png` 均已就绪。
