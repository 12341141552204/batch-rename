# 批量文件重命名工具 (batch-rename)

一个简单强大的批量文件重命名命令行工具，支持前缀、后缀、文本替换、序号、扩展名修改。

## 功能

- 添加前缀 / 后缀
- 文本替换
- 序号自动编号（可指定位数）
- 修改扩展名
- 预览模式（dry-run）

## 使用方法

```bash
# 基本用法：给所有文件加前缀 "photo_" 并编号
python main.py ./photos --prefix photo_

# 替换文件名中的文本
python main.py ./docs --replace-from "旧" --replace-to "新"

# 修改扩展名
python main.py ./files --ext .txt

# 预览效果（不实际执行）
python main.py ./photos --prefix img_ --dry-run
```

## 参数说明

| 参数 | 说明 |
|------|------|
| `folder` | 目标文件夹路径（必填） |
| `--prefix` | 添加前缀 |
| `--suffix` | 添加后缀 |
| `--replace-from` | 要替换的文本 |
| `--replace-to` | 替换为 |
| `--start-num` | 序号起始值（默认 1） |
| `--num-pad` | 序号位数（默认 3） |
| `--ext` | 修改扩展名（如 `.txt`） |
| `--dry-run` | 仅预览，不实际执行 |

## 示例

```bash
# 将 photo_001.jpg, photo_002.jpg 重命名
python main.py ./images --prefix trip_ --start-num 100 --num-pad 4
# 结果: trip_0100.jpg, trip_0101.jpg ...
```

## 依赖

仅使用 Python 标准库，无需额外安装。
