"""压缩 static/images/wx 下的大图：宽度限到 1600 像素、转 WebP（质量 82），删掉原文件。

文件名的主干（URL 的 md5）不变，import_wechat.py 按主干找图，所以压缩后重跑导入即可改好链接。
GIF（可能是动图）和 SVG 不动；已经小于 200 KB 的也不动。
"""
import sys
from pathlib import Path

from PIL import Image

WX = Path(__file__).resolve().parent.parent / "static" / "images" / "wx"
MAX_W = 1600
MIN_BYTES = 200 * 1024


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    before = after = n = 0
    for f in sorted(WX.iterdir()):
        if f.suffix.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
            continue
        size = f.stat().st_size
        if size < MIN_BYTES:
            continue
        try:
            im = Image.open(f)
            im.load()
        except Exception as e:
            print("跳过（打不开）：", f.name, e)
            continue
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGBA" if "A" in im.getbands() or im.mode == "P" else "RGB")
        if im.width > MAX_W:
            im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
        out = f.with_suffix(".webp")
        tmp = f.with_suffix(".tmp.webp")
        im.save(tmp, "WEBP", quality=82, method=5)
        new = tmp.stat().st_size
        if new >= size:
            tmp.unlink()
            continue
        if out != f and out.exists():
            out.unlink()
        f.unlink()
        tmp.rename(out)
        before += size
        after += new
        n += 1
    print(f"压缩 {n} 张：{before / 2**20:.0f} MB → {after / 2**20:.0f} MB")


if __name__ == "__main__":
    main()
