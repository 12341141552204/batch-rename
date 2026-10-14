#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量文件重命名工具
支持：添加前缀/后缀、替换文本、序号重命名、扩展名修改
"""

import os
import argparse
from pathlib import Path


def batch_rename(folder, prefix="", suffix="", replace_from="", replace_to="",
                 start_num=1, num_pad=3, ext="", dry_run=False):
    """批量重命名文件"""
    folder = Path(folder)
    if not folder.is_dir():
        print(f"[错误] 目录不存在: {folder}")
        return

    files = sorted([f for f in folder.iterdir() if f.is_file()])
    if not files:
        print("[提示] 目录中没有文件")
        return

    count = 0
    for idx, f in enumerate(files, start=start_num):
        stem = f.stem
        original_name = f.name

        # 替换文本
        if replace_from:
            stem = stem.replace(replace_from, replace_to)

        # 前缀
        if prefix:
            stem = f"{prefix}{stem}"

        # 后缀
        if suffix:
            stem = f"{stem}{suffix}"

        # 序号
        stem = f"{stem}_{str(idx).zfill(num_pad)}"

        # 扩展名
        extension = ext if ext else f.suffix

        new_name = f"{stem}{extension}"
        new_path = folder / new_name

        if new_path == f:
            continue

        # 避免重名
        n = 1
        while new_path.exists() and new_path != f:
            new_name = f"{stem}_{n}{extension}"
            new_path = folder / new_name
            n += 1

        if dry_run:
            print(f"[预览] {original_name}  ->  {new_name}")
        else:
            f.rename(new_path)
            print(f"[完成] {original_name}  ->  {new_name}")
        count += 1

    print(f"\n共处理 {count} 个文件")


def main():
    parser = argparse.ArgumentParser(description="批量文件重命名工具")
    parser.add_argument("folder", help="目标文件夹路径")
    parser.add_argument("--prefix", default="", help="添加前缀")
    parser.add_argument("--suffix", default="", help="添加后缀")
    parser.add_argument("--replace-from", default="", help="要替换的文本")
    parser.add_argument("--replace-to", default="", help="替换为")
    parser.add_argument("--start-num", type=int, default=1, help="序号起始值")
    parser.add_argument("--num-pad", type=int, default=3, help="序号位数")
    parser.add_argument("--ext", default="", help="修改扩展名（如 .txt）")
    parser.add_argument("--dry-run", action="store_true", help="仅预览，不执行")
    args = parser.parse_args()

    batch_rename(
        args.folder,
        prefix=args.prefix,
        suffix=args.suffix,
        replace_from=args.replace_from,
        replace_to=args.replace_to,
        start_num=args.start_num,
        num_pad=args.num_pad,
        ext=args.ext,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
