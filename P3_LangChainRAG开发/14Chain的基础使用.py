# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：14Chain的基础使用.py
@Author  ：九成八
@Date    ：2026/3/7 19:24 
"""
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from AI大模型RAG与智能体开发.common.load_env import get_env

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞诗人，可以作诗。"),
        MessagesPlaceholder("history"),
        ("human", "请再来一首唐诗"),
    ]
)

history_data = [
    ("human", "你来写一个唐诗"),
    ("ai", "床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("human", "好诗再来一个"),
    ("ai", "锄禾日当午，汗滴禾下锄，谁知盘中餐，粒粒皆辛苦"),
]

model = ChatTongyi(
    api_key=get_env("DASHBOARD_API_KEY"),
    model="qwen3-max"
)

# 组成链，要求每一个组件都是Runnable接口的子类
chain = chat_prompt_template | model

# 通过链去调用invoke或stream
# res = chain.invoke({"history": history_data})
# print(res.content)

# 通过stream流式输出
for chunk in chain.stream({"history": history_data}):
    print(chunk.content, end="", flush=True)
