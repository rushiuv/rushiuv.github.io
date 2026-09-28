# 如是有为博客

Hugo 静态博客，内容是公众号「如是有为」已发表文章的存档（264 篇，2025-09-22 ~ 2026-09-22）。
线上地址（发布后）：https://rushiuv.github.io/

## 日常操作

- 本地预览：`hugo server`，打开 http://localhost:1313/
- 重新导入文章：`python tools/import_wechat.py`
  - 来源：`D:\VerySync\VerySync_notes\2-Resources\2K-公众号-如是有为`
  - 会清空并重建 `content/posts/`；新出现的微信配图自动下载到 `static/images/wx/`，已下载的不重复下
- 压缩新下载的大图：`python tools/optimize_images.py`，然后再跑一次导入改好链接
- 发布：`bash tools/deploy.sh`（`main` 分支放构建产物给 GitHub Pages，`source` 分支放源码）

## 标签

`tools/tag_vocab.txt` 是词表，分三段：`[型号]` `[公司]` `[主题]`，每行「显示名|别名|别名」。
导入时在标题和正文里匹配。型号和公司出现 1 次就打标签，主题词要出现 2 次（标题里出现算 2 次）。
加标签就往词表里加一行，再重跑导入。

## 主题

`layouts/` 和 `static/css/site.css` 是自带的模板，只做亮色，没有外部依赖。
主图、头像、二维码在 `static/images/site/`；《金刚经》引句写在 `hugo.toml` 的 `params` 里。
