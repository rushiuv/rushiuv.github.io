# 如是有为博客

Hugo 静态博客，内容是公众号「如是有为」已发表文章的存档（264 篇，2025-09-22 ~ 2026-09-22）。

- 文章来源：`D:\VerySync\VerySync_notes\2-Resources\2K-公众号-如是有为`（后台整号下载的存档）
- 重新导入：`python tools/import_wechat.py`（会清空并重建 `content/posts/`，本地图从库的 `_source` 复制到 `static/images/`）
- 本地预览：`hugo server`，打开 http://localhost:1313/
- 构建：`hugo`，产物在 `public/`
- 主题是 `layouts/` 里自带的极简模板，没有外部依赖

## 图片
大部分配图仍是微信 CDN（mmbiz.qpic.cn）外链。微信按 Referer 防盗链，所以页面加了
`<meta name="referrer" content="no-referrer">`，图片渲染钩子也带 `referrerpolicy="no-referrer"`。
若以后要彻底脱离微信 CDN，需要把这些图下载进 `static/images/` 再改链接。

## 部署前
把 `hugo.toml` 里的 `baseURL` 改成真实域名。
