import os
import sys

# 打印 Python 版本，确认用的是 .venv 里那个
print("Python 版本:", sys.version.split()[0])
print("当前目录:", os.getcwd())

# 看看 Key 在不在，但只打印头尾几位，不泄露全文
key = os.environ.get("LLM_API_KEY", "")
if not key:
    print("Key: 没读到  <-- 回上一步设环境变量")
else:
    print("Key: 读到了，长度", len(key))
    print("     开头", key[:4], "结尾", key[-3:])