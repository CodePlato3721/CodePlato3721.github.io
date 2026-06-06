---
name: juejin-publish
description: 为草稿目录中的文章生成掘金发布所需的元数据和简化版草稿
trigger: "发布到掘金"
---

## 目标

直接从项目的 `draft/` 目录读取文章，生成掘金发布所需的全部素材，输出到 `~/.blog-workspace/juejin/` 目录。

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/article.md`**：文章正文
- **`draft/metadata.md`**：提取：
  - `中文标题` → `zh-title`
  - `中文分类` → 收录至专栏

### 2. 生成文章摘要

阅读文章正文，写一段 **100 字以内**的中文摘要，概括核心主题和主要观点。

### 3. 准备输出目录

确保 `~/.blog-workspace/juejin/` 目录存在（不存在则新建）。

### 4. 写出元数据文件

将以下内容写入 `~/.blog-workspace/juejin/元数据.md`：

```markdown
# 中文标题
{zh-title}

# 编辑摘要
{100 字以内的摘要}

# 收录至专栏
{中文分类}
```

### 5. 生成简化版草稿

读取 `draft/article.md` 正文，生成简化版文章，写入 `~/.blog-workspace/juejin/草稿.md`。

简化规则：
- **适度简化文字**：对篇幅较长的说明段落，精简表述，去掉冗余；但保留核心观点，不改变含义
- **保留不简化的内容**：代码块、示例、表格、列表条目——这类内容结构固定，原样保留
- **图片占位符**：将 `<cn-image-XX>` 占位标签原样保留（掘金编辑器上传图片后再替换）

### 6. 复制封面图

将 `draft/cn-banner.png` 复制到 `~/.blog-workspace/juejin/cn-banner.png`：

```powershell
Copy-Item "draft\cn-banner.png" "$env:USERPROFILE\.blog-workspace\juejin\cn-banner.png"
```

### 7. 确认输出

列出 `~/.blog-workspace/juejin/`，确认 `元数据.md`、`草稿.md`、`cn-banner.png` 均已就绪。
