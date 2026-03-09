# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：02LangChain访问阿里云通义千问大模型.py
@Author  ：九成八
@Date    ：2026/3/7 13:41 
"""
from langchain_community.llms.tongyi import Tongyi
from AI大模型RAG与智能体开发.common.load_env import get_env

# 不用qwen3-max,因为qwen3-max是聊天模型,qwen-max是大语言模型
model = Tongyi(
    api_key=get_env("DASHSCOPE_API_KEY"),
    model='qwen-max'
)

# 调用invoke向模型提问
res = model.invoke(input="你是谁，能做什么？")
print(res)