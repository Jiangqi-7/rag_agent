# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：07LangChain消息的简写形式.py
@Author  ：九成八
@Date    ：2026/3/7 15:03 
"""
from langchain_community.chat_models.tongyi import ChatTongyi
from AI大模型RAG与智能体开发.common.load_env import get_env

# 得到模型对象, qwen3-max就是聊天模型
model = ChatTongyi(
    api_key=get_env("DASHSCOPE_API_KEY"),
    model="qwen3-max"
)

# 准备消息列表
messages = [
    # (角色，内容)  角色：system/human/ai
    ("system", "你是一个边塞诗人。"),
    ("human", "写一首唐诗。"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    ("human", "按照你上一个回复的格式，在写一首唐诗。")
]

# 调用stream流式执行
res = model.stream(input=messages)

# for循环迭代打印输出，通过.content来获取到内容
for chunk in res:
    print(chunk.content, end="", flush=True)
