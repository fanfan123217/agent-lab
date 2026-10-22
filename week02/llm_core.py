def build_payload(prompt: str, model: str = "deepseek-chat") -> dict:
    # 新增校验：如果去掉空格后是空的，说明用户什么都没填
    if not prompt.strip():
        # 主动抛出异常，拦截这次调用
        raise ValueError("提问不能为空")
        
    return {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt},
        ],
    }