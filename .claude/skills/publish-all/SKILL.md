---
name: publish-all
description: 按固定顺序依次执行完整发布流程（prepare → draft-to-en → draft-to-zh → devto → x → hackernoon → linkedin → juejin → csdn → weibo），一次性把一篇稿子发布到全部平台。用户输入 "/publish-all <代号>"、"全部发布:<代号>" 或类似表述时使用。
---

## 调用方式

```
/publish-all <代号>
```

例：`/publish-all 0819memory`

`<代号>` 从 slash 命令参数中获取（也可用 "全部发布:<代号>" 等自然语言触发），所有文件路径均以 `draft/<代号>/` 为根目录。

## 前提

`draft/<代号>/` 下已完成写稿，至少包含：
- `cn-article.md`
- `metadata.md`（含 `中文标题`、`英文标题`、`中文分类`、`英文分类` 字段）
- `cn-banner.png`

## 分类说明

| 阶段 | Skill | 性质 |
|------|-------|------|
| 1 | `prepare` | 翻译 + 上传图片，为后续所有步骤做准备 |
| 2 | `draft-to-en` | 自动发布——写入本博客英文版 |
| 3 | `draft-to-zh` | 自动发布——写入本博客中文版 |
| 4 | `devto` | 自动发布——调用 API 发到 dev.to |
| 5 | `x` | 自动发布——调用 API 发到 X |
| 6 | `hackernoon` | 仅生成素材——需手动去 HackerNoon 编辑器粘贴发布 |
| 7 | `linkedin` | 仅生成素材——需手动去 LinkedIn 发布 |
| 8 | `juejin` | 仅生成素材——需手动去掘金发布 |
| 9 | `csdn` | 仅生成素材——需手动去 CSDN 发布 |
| 10 | `weibo` | 仅生成素材——需手动去微博发布 |

## 执行顺序（严格按此顺序，不可打乱或跳过）

依次用 `Skill` 工具调用下列每个 skill，`<代号>` 作为 `args` 传入：

1. `prepare`
2. `draft-to-en`
3. `draft-to-zh`
4. `devto`
5. `x`
6. `hackernoon`
7. `linkedin`
8. `juejin`
9. `csdn`
10. `weibo`

## 执行时的注意事项

- **严格串行**：每一步必须等上一步真正完成（文件确实写入、API 确实返回成功）才能开始下一步，不要并行或提前开始
- **失败即停**：任何一步报错（凭证缺失/过期、额度不足、链接 404、文件缺失等），立刻停下，把错误原因和目前完成到哪一步告诉用户；不要自动重试、不要跳过该步骤继续后面的步骤——等用户处理好问题后，从失败的那一步（而不是从头）继续
- **各 skill 自身的强制检查照常执行**，不因为是被串联调用就简化，比如 `weibo`/`x` 里对链接的验证步骤，仍要按各自 SKILL.md 的要求执行
- `draft-to-en`、`draft-to-zh` 会修改本仓库 `content/` 下的文件，但不会自动 commit/push，串联执行完之后仍由用户决定何时提交
- `devto`、`x` 是对外发布操作，发布后不易撤回（`x` 可删除重发，`devto` 需登录后台改），这两步照常执行，不需要额外向用户二次确认——用户调用 `/publish-all` 本身就是对整条链路的授权

## 全部完成后

汇总一份清单告知用户：

- **已自动发布上线**：本博客中/英文版链接、dev.to 链接、X 链接
- **待手动发布**：HackerNoon / LinkedIn / 掘金 / CSDN / 微博，各自素材目录路径（`~/.blog-workspace/<代号>/{平台}/`），提醒用户逐一去对应平台手动粘贴发布
