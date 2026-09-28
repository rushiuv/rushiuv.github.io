#!/usr/bin/env bash
# 构建并发布到 GitHub Pages（https://rushiuv.github.io）
# 分支约定：source = Hugo 源码；main = 构建产物（Pages 从 main 根目录发布）
# 用法：在博客根目录执行  bash tools/deploy.sh
set -euo pipefail
cd "$(dirname "$0")/.."

REMOTE=${REMOTE:-origin}
HUGO=${HUGO:-hugo}
command -v "$HUGO" >/dev/null 2>&1 || HUGO="$LOCALAPPDATA/Microsoft/WinGet/Packages/Hugo.Hugo.Extended_Microsoft.Winget.Source_8wekyb3d8bbwe/hugo.exe"

rm -rf public
"$HUGO" --gc --minify
touch public/.nojekyll

SRC_REV=$(git rev-parse --short HEAD)
TMP=$(mktemp -d)
git worktree add --detach "$TMP" >/dev/null
(
  cd "$TMP"
  git checkout --orphan deploy-tmp >/dev/null 2>&1
  git rm -rfq . >/dev/null 2>&1 || true
  cp -r "$OLDPWD/public/." .
  git add -A
  git commit -qm "deploy: 由 source@$SRC_REV 构建"
  git push -f "$REMOTE" HEAD:main
)
git worktree remove --force "$TMP"
git branch -D deploy-tmp >/dev/null 2>&1 || true
git push "$REMOTE" HEAD:source
echo "已发布：https://rushiuv.github.io/"
