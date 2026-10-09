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

## 发布时的坑（2026-10-09 实测，本机 t14p）

`bash tools/deploy.sh` 在这台机器的 Hermes bash（MSYS）下有几处会咬人的地方，报错都不好认：

1. **`TMPDIR` 要给一个双方都认的 Windows 路径。** MSYS 的 `mktemp -d` 返回 `/tmp/...`，而 bash 的 `/tmp` 与原生 git 认的 `/tmp`（＝`D:\tmp`）不是同一个目录：脚本在子 shell 里 `cd` 进了一个非仓库目录，`git checkout --orphan` 静默失败（stderr 被脚本重定向掉了），**只剩一个 exit 128、什么错误都不打印**。写成
   `TMPDIR="C:/Users/wangc/AppData/Local/hermes/cache/scratch/tmpd" bash tools/deploy.sh` 即可。
2. **上一次死在 push 的残留会毒死下一次。** `deploy-tmp` 分支或 `D:/tmp/tmp.*` worktree 还在时，下一次一定在脚本开头 `git checkout --orphan` 撞名失败。跑之前先 `git worktree list` 与 `git branch -D deploy-tmp` 清一遍。
3. **GitHub 的 HTTPS 凭据会失效**，报 `remote: Invalid username or token. Password authentication is not supported`。本机 SSH 通的是 `neurusuv`、对该仓库有写权限，所以发布用
   `REMOTE=git@github.com:rushiuv/rushiuv.github.io.git bash tools/deploy.sh`；也可以重新登录一次 HTTPS 凭据，两种都行。
4. 发布后**核一遍线上**：文章地址里的 slug 是**小写**的（Hugo 会把网址转小写），
   `https://rushiuv.github.io/posts/<小写slug>/`；Actions 那次运行记录在仓库 Actions 页，
   推送 main 之后才会出现。

## 主题

`layouts/` 和 `static/css/site.css` 是自带的模板，只做亮色，没有外部依赖。
主图、头像、二维码在 `static/images/site/`；《金刚经》引句写在 `hugo.toml` 的 `params` 里。
