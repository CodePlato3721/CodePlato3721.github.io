---
name: juejin-publish
description: 为指定的中文博客文章生成掘金发布所需的元数据和简化版草稿
trigger: "发布到掘金"
---

## 目标

为一篇中文博客文章生成掘金发布所需的全部素材，输出到 `~/.blog-workspace/juejin/` 目录：元数据文件、简化版草稿、封面图。

## 步骤

### 1. 从草稿读取文章标题

读取 `~/.blog-workspace/draft/草稿.md` 的第一行，提取中文标题：

- 第一行格式为 `# 标题文字`，去掉 `# ` 前缀即为 `zh-title`

用 `zh-title` 推导 `zh-dir`（把 Windows 禁止字符 `: / \ * ? " < > |` 及全角等价字符替换为 `-`），定位文章文件：

```
content/zh/post/{zh-dir}/index.md
```

### 2. 读取 frontmatter

从文章文件中提取：
- `title`：中文标题
- `categories`：收录至专栏的值

### 3. 生成文章摘要

阅读文章正文，写一段 **100 字以内**的中文摘要，概括核心主题和主要观点。

### 4. 准备输出目录

确保 `~/.blog-workspace/juejin/` 目录存在（不存在则新建）。

### 5. 写出元数据文件

将以下内容写入 `~/.blog-workspace/juejin/元数据.md`：

```markdown
# 中文标题
{title 的值}

# 编辑摘要
{100 字以内的摘要}

# 收录至专栏
{categories 的值}
```

### 6. 生成简化版草稿

读取 `content/zh/post/{zh-dir}/index.md` 正文（去除 frontmatter），生成简化版文章，写入 `~/.blog-workspace/juejin/草稿.md`。

简化规则：
- **去除 frontmatter**：去掉文件开头两个 `---` 之间的全部内容
- **适度简化文字**：对篇幅较长的说明段落，精简表述，去掉冗余；但保留核心观点，不改变含义
- **保留不简化的内容**：代码块、示例、表格、列表条目——这类内容结构固定，原样保留
- **末尾加原文链接**：在文章最后追加一行：

```
完整版：https://codeplato3721.github.io/zh/post/{zh-dir}/
```

其中 `{zh-dir}` 需做 URL 编码。

### 7. 复制封面图

将 `~/.blog-workspace/draft/cn-banner.png` 复制到 `~/.blog-workspace/juejin/cn-banner.png`：

```powershell
Copy-Item "$env:USERPROFILE\.blog-workspace\draft\cn-banner.png" `
          "$env:USERPROFILE\.blog-workspace\juejin\cn-banner.png"
```

### 8. 确认输出

列出 `~/.blog-workspace/juejin/`，确认 `元数据.md`、`草稿.md`、`cn-banner.png` 均已就绪。
