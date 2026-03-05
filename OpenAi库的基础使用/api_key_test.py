# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：api_key_test.py
@Author  ：九成八
@Date    ：2026/3/5 16:45 
"""
from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载.env文件（默认读取项目根目录的.env）
# 如果.env文件不在根目录，可指定路径：load_dotenv(dotenv_path="./config/.env")
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    # api_key=os.getenv("DASHSCOPE_API_KEY"),
    api_key=api_key,
    # base_url=os.getenv("OPENAI_BASE_URL"),
    base_url=os.getenv("LOCAL_BASE_URL")
)

messages = [{"role": "user", "content": "你是谁"}]
completion = client.chat.completions.create(
    # model="qwen3-max",  # 您可以按需更换为其它深度思考模型
    model="deepseek-r1:7b",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    extra_body={"enable_thinking": True},
    stream=True
)
is_answering = False  # 是否进入回复阶段
print("\n" + "=" * 20 + "思考过程" + "=" * 20)
for chunk in completion:
    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        if not is_answering:
            print(delta.reasoning_content, end="", flush=True)
    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            print("\n" + "=" * 20 + "完整回复" + "=" * 20)
            is_answering = True
        print(delta.content, end="", flush=True)