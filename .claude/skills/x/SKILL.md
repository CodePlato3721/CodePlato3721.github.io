---
name: x
description: 从 draft/<代号>/ 生成一句话推文并自动发布到 X（Twitter）。用户输入 "/x <代号>"、"发布x:<代号>" 或类似表述时使用。
---

## 调用方式

```
/x <代号>
```

例：`/x 0606tokenmaxxing`

`<代号>` 从 slash 命令参数中获取（也可用 "发布x:<代号>" 等自然语言触发），所有文件路径均以 `draft/<代号>/` 为根目录。

## 前提

- 已运行 `/draft-to-en <代号>`，英文版文章已发布（本博客，或已首发到其他站点）
- `.claude/skills/x/.env` 中已设置以下变量（X Developer Portal → 项目 App → Keys and tokens）：
  - `X_API_KEY` / `X_API_SECRET`：App 的 API Key/Secret
  - `X_ACCESS_TOKEN` / `X_ACCESS_TOKEN_SECRET`：User authentication settings 中需先把权限设为 **Read and Write**，再生成/重新生成 Access Token & Secret（否则发推会 403）
  - `X_HANDLE`：账号 handle，默认 `codeplato2026`

## 目标

从 `draft/<代号>/` 读取已发布的英文文章，生成一句话（英文）推文，附上文章链接，通过 X API v2 自动发布。

## 步骤

### 1. 读取元数据

读取 `draft/<代号>/metadata.md`，提取：

- `英文标题` → `en-title`
- `en-slug` = `en-title` 转 kebab-case（冒号及标点去掉或替换为 `-`）
- `# 首发` 段落（可选）→ `website` / `url`
- `# Hackernoon` 段落（可选）→ `url`

### 2. 确定文章链接

按以下优先级选取一个链接：

1. `# 首发` 段落有 `url` → 使用该首发 URL
2. 没有首发 URL，但 `# Hackernoon` 段落有 `url` → 使用该 HackerNoon URL
3. 以上都没有 → 使用本博客英文版链接 `https://CodePlato3721.github.io/post/{en-slug}/`（`en` 是默认语言，**不带 `/en/` 子路径**，只有 `zh` 会带 `/zh/`）

### 3. 撰写推文正文

读取 `draft/<代号>/en-article.md`，提炼出**一句话钩子**（英文）：

- 不是摘要陈述句，而是能引发点击欲望的一句话——抛出文章最有反差感/最有观点的那个点
- 语气直接、不说教，符合 X 平台的表达习惯
- 长度控制在 200 字符以内（为链接和空行留出余量，链接在 X 上固定占用约 23 字符）
- 不加 hashtag（除非文章主题非常适合 1 个精准的 hashtag，最多用 1 个）

组装完整推文：

```
{一句话钩子}

{文章链接}
```

整体不超过 280 字符。

### 4. 准备输出目录并写入草稿

确保 `~/.blog-workspace/<代号>/x/` 目录存在：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\<代号>\x" | Out-Null
```

将组装好的推文全文（纯文本，无 frontmatter）写入：

```
~/.blog-workspace/<代号>/x/tweet.md
```

### 5. 运行发布脚本

在项目根目录下执行：

```powershell
skills\.venv\Scripts\python.exe .claude\skills\x\scripts\post_tweet.py "$env:USERPROFILE\.blog-workspace\<代号>\x\tweet.md"
```

### 6. 确认结果

脚本成功后会输出：
```
published: https://x.com/{handle}/status/{id}
```

如果报错，检查：
- `.claude/skills/x/.env` 中四个 X_* 凭证是否都已填写
- X Developer App 的 User authentication settings 权限是否为 **Read and Write**（改权限后需要重新生成 Access Token）
- 推文正文是否超过 280 字符
- `~/.blog-workspace/<代号>/x/tweet.md` 是否存在
