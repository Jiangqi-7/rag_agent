# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：13ChatPromptTemplate的使用.py
@Author  ：九成八
@Date    ：2026/3/7 19:16 
"""
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
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

# StringPromptValue    to_string()
prompt_text = chat_prompt_template.invoke({"history": history_data}).to_string()

model = ChatTongyi(
    api_key=get_env("DASHSCOPE_API_KEY"),
    model="qwen3-max"
)

res = model.invoke(prompt_text)

print(res.content, type(res))