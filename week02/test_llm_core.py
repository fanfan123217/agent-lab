import pytest
# 导入被测函数，文件名不带 .py
from llm_core import build_payload

# 第一个测试：只验提问有没有被放进消息里
def test_prompt_goes_into_message():
    # 调用被测函数，不联网
    payload = build_payload("你好")
    # 只留这一条断言
    assert payload["messages"][0]["content"] == "你好"

# 第二个测试：只验默认模型名
def test_default_model_name():
    # 再调一次，拿独立结果
    payload = build_payload("你好")
    # 这条只管模型名
    assert payload["model"] == "deepseek-chat"

# 新测试：验证传空字符串会报错
def test_empty_prompt_raises_error():
    # pytest.raises 是断言：我期待这段代码报错
    with pytest.raises(ValueError):
        # 故意传一堆空格进去
        build_payload("   ")