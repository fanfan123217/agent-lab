import json
import os
import urllib.request

# 换厂商只改这两行: DeepSeek 用下面默认值
# OpenAI: https://api.openai.com/v1/chat/completions
# 百炼: https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions
BASE_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"

# 从环境变量取 Key，取不到就停下并说清楚原因
key = os.environ.get("LLM_API_KEY", "")
if not key:
    raise SystemExit("没读到 LLM_API_KEY，先设环境变量")

import json
import os
import urllib.request
# 导入我们刚刚写好、测好的模块
from week02.llm_core import build_payload

BASE_URL = "https://api.deepseek.com/chat/completions"

key = os.environ.get("LLM_API_KEY", "")
if not key:
    raise SystemExit("没读到 LLM_API_KEY，先设环境变量")

# 这里不再手写字典，直接调函数，传题目进去
body = build_payload("用一句话介绍你自己")

data = json.dumps(body, ensure_ascii=False).encode("utf-8")

# 下面的请求代码不用改
req = urllib.request.Request(
    BASE_URL,
    data=data,
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + key,
    },
)

with urllib.request.urlopen(req, timeout=60) as resp:
    raw = resp.read().decode("utf-8")

result = json.loads(raw)
print(result["choices"][0]["message"]["content"])
# 字典 -> JSON 文本 -> 字节串（网络只认字节）
data = json.dumps(body, ensure_ascii=False).encode("utf-8")

req = urllib.request.Request(
    BASE_URL,
    data=data,
    headers={
        "Content-Type": "application/json",
        # 身份牌，服务器靠这个认出你、给你计费
        "Authorization": "Bearer " + key,
    },
)

# 发送请求，60秒没回就报超时
with urllib.request.urlopen(req, timeout=60) as resp:
    res_body = resp.read().decode("utf-8")
res_json = json.loads(res_body)
print(res_json["choices"][0]["message"]["content"])
