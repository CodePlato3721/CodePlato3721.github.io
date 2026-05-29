---
name: csdn-publish
description: 为指定的中文博客文章生成 CSDN 发布所需的元数据、简化版草稿和封面图
trigger: "发布到 CSDN"
---

## 目标

为一篇中文博客文章生成 CSDN 发布所需的全部素材，输出到 `~/.blog-workspace/csdn/` 目录：元数据文件、简化版草稿、封面图和插图。

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
- `categories`：分类专栏值

### 3. 生成文章摘要

阅读文章正文，写一段 200 字以内的中文摘要，概括：
- 文章核心主题
- 主要内容/结构
- 核心观点或结论

### 4. 准备输出目录

确保 `~/.blog-workspace/csdn/` 目录存在（不存在则新建）。

### 5. 写出元数据文件

将以下内容写入 `~/.blog-workspace/csdn/元数据.md`：

```markdown
# 中文标题
{title 的值}

# 文章摘要
{生成的摘要}

# 分类专栏
{categories 的值}
```

### 6. 生成简化版草稿

读取 `content/zh/post/{zh-dir}/index.md` 正文（去除 frontmatter），生成简化版文章，写入 `~/.blog-workspace/csdn/草稿.md`。

简化规则：
- **去除 frontmatter**：去掉文件开头两个 `---` 之间的全部内容
- **适度简化文字**：对篇幅较长的说明段落，精简表述，去掉冗余；但保留核心观点，不改变含义
- **保留不简化的内容**：代码块、示例、表格、列表条目——这类内容结构固定，原样保留
- **末尾加原文链接**：在文章最后追加一行：

```
完整版：https://codeplato3721.github.io/zh/post/{zh-dir}/
```

其中 `{zh-dir}` 需做 URL 编码（中文字符转为 `%XX` 格式），或直接使用浏览器可识别的中文路径均可。

### 7. 复制封面图

将 `~/.blog-workspace/draft/cn-banner.png` 复制到 `~/.blog-workspace/csdn/cn-banner.png`：

```powershell
Copy-Item "$env:USERPROFILE\.blog-workspace\draft\cn-banner.png" `
          "$env:USERPROFILE\.blog-workspace\csdn\cn-banner.png"
```

### 8. 复制插图

将 `~/.blog-workspace/draft/` 下所有 `cn-image-*.png` 复制到 `~/.blog-workspace/csdn/`：

```powershell
Copy-Item "$env:USERPROFILE\.blog-workspace\draft\cn-image-*.png" `
          "$env:USERPROFILE\.blog-workspace\csdn\"
```

如果没有 `cn-image-*.png`，跳过此步骤。

### 9. 确认输出

列出 `~/.blog-workspace/csdn/`，确认 `元数据.md`、`草稿.md`、`cn-banner.png`、所有插图均已就绪。
