---
name: weibo
description: 从 draft/<代号>/cn-article.md 生成一条微博文案，输出到 ~/.blog-workspace/<代号>/weibo/ 供手动发布。用户输入 "/weibo <代号>"、"发布微博:<代号>" 或类似表述时使用。
---

## 调用方式

```
/weibo <代号>
```

例：`/weibo 0819memory`

`<代号>` 从 slash 命令参数中获取（也可用 "发布微博:<代号>" 等自然语言触发），所有文件路径均以 `draft/<代号>/` 为根目录。

## 前提

已运行 `/draft-to-zh <代号>`，中文版文章已发布到本博客（`content/zh/post/{zh-dir}/index.md` 存在）。

（微博开放平台创建应用需要身份证实名认证，暂不走 API 自动发布，本 skill 只准备文案和配图，由用户手动发布。）

## 目标

从 `draft/<代号>/` 读取已发布的中文文章，生成一句话（中文）微博文案（带本博客中文版链接），连同封面图一起输出到 `~/.blog-workspace/<代号>/weibo/`，供手动发布到微博。

## 步骤

### 1. 读取元数据

读取 `draft/<代号>/metadata.md`，提取 `中文标题` → `zh-title`。

### 2. 确定文章链接

1. 在 `content/zh/post/` 下找到与 `zh-title` 对应的文章目录（`draft-to-zh` 生成时用的目录名，可能保留原始大小写）
2. 把目录名转小写、URL 编码，拼成链接：
   ```powershell
   $slug = "{目录名}".ToLower()
   $encoded = [System.Uri]::EscapeDataString($slug)
   $link = "https://CodePlato3721.github.io/zh/post/$encoded/"
   ```
3. `curl -sI $link` 验证返回 200（Hugo 会把 URL 自动转小写，跟目录原始大小写不一定一致，必须实测，不能凭猜测拼）

### 3. 撰写微博正文

读取 `draft/<代号>/cn-article.md`，提炼出**一句话钩子**（中文）：

- 不是摘要陈述句，而是能引发点击欲望的一句话——抛出文章最有反差感/最有观点的那个点
- 语气直接、不说教，符合微博的表达习惯
- 不加话题标签（除非文章主题非常适合 1 个精准的 `#话题#`，最多用 1 个）

组装完整正文：

```
{一句话钩子}

{文章链接}
```

### 4. 准备输出目录并写入文案

确保 `~/.blog-workspace/<代号>/weibo/` 目录存在：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\<代号>\weibo" | Out-Null
```

将组装好的正文全文（纯文本，无 frontmatter）写入：

```
~/.blog-workspace/<代号>/weibo/weibo.md
```

### 5. 复制封面图

将 `draft/<代号>/cn-banner.png` 复制到输出目录并重命名为 `banner.png`：

```powershell
Copy-Item "draft\<代号>\cn-banner.png" "$env:USERPROFILE\.blog-workspace\<代号>\weibo\banner.png"
```

### 6. 确认输出

告知用户：
- `weibo.md` 里的文案全文
- `banner.png` 已就绪
- 提醒用户手动打开微博发布，把 `banner.png` 作为配图一起发出
