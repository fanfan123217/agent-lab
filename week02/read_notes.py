# 导入 Path：找文件和读文件都用它
from pathlib import Path

# --- 上一步拿到工具，这一块定位输入目录
# 指向 notes 文件夹：相对路径，必须在 week02 里跑
notes_dir = Path("notes")

# 找出所有 txt：sorted 让顺序固定，便于对比
txt_files = sorted(notes_dir.glob("*.txt"))

# --- 上一步拿到文件清单，这一块逐个读进来
# 空列表装结果：读一个塞一个
notes = []

# 逐个文件处理：变量名直接说明是哪个文件
for note_file in txt_files:
    # 读全文：encoding 写死，Windows 默认不是 utf-8
    text = note_file.read_text(encoding="utf-8")
    # 正文去掉空白后为空，说明这文件没内容
    if not text.strip():
        # 喊一声再跳过：不悄悄丢数据
        print("跳过空文件:", note_file.name)
        # 结束这一轮，直接处理下一个文件
        continue
    # 存成字典：名字和正文分开，统计好取
    notes.append({"name": note_file.name, "text": text})

# --- 上一步只留下有内容的，这一块打印核对
# 先打印有效条数：应该是 3
print("有效条数:", len(notes))

# 再打印名字和字数：确认中文没乱码
for note in notes:
    print(note["name"], len(note["text"]))

# 导入 json：把 Python 的列表变成文本，能存盘也能读回来
import json

# --- 上面所有代码不变，这一块在最后追加统计
# 总字数先归零：统计前必须有个起点
total_chars = 0

# 逐条累加：每条正文的长度加起来
for note in notes:
    total_chars = total_chars + len(note["text"])

# --- 上一步拿到数据，这一块把它写进文件
# 打开文件准备写：w 表示覆盖写，每次跑都是最新的
with open("report.json", "w", encoding="utf-8") as report_file:
    # ensure_ascii=False 让中文原样写，否则全变成 \u 转义
    # indent=2 让每个字段单独一行，人眼能看懂
    json.dump(notes, report_file, ensure_ascii=False, indent=2)

# 打完这行，这周的任务就闭环了
print("已写入 report.json，总字数:", total_chars)