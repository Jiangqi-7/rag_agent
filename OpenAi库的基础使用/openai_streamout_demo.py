# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：openai_streamout_demo.py
@Author  ：九成八
@Date    ：2026/3/5 17:39 
"""
from openai import OpenAI, api_key
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# 获取client对象
client = OpenAI(
    api_key=openai_api_key,
    base_url=os.getenv("OPENAI_BASE_URL")
)

# 调用模型
response = client.chat.completions.create(
    model="qwen3-max",
    # 角色:
    # system:设定助手的整体行为、角色和规则，为对话提供上下文框架，如指定助手身份、回答风格、核心要求，是全局的背景设定，影响后续所有交互
    # assistant: 代表AI助手的回答
    # user: 代表用户，发送问题、指令或需求
    messages =[
        {"role": "system","content": "你是一个python编程专家，并且话非常多"},
        {"role": "assistant","content": "好的，我是python编程专家，并且话非常多，你要闻什么？"},
        {"role": "user","content": "用python输出1-10"}
    ],
    stream=True # 开启流式输出
)

# 处理结果
# print(response.choices[0].message.content)
for chunk in response:
    print(chunk.choices[0].delta.content,
          end=" ", # 每一段之间以空格分隔
          flush=True # 立刻刷新缓冲区
    )