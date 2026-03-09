# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：04LangChain的流式输出.py
@Author  ：九成八
@Date    ：2026/3/7 13:57 
"""
# from langchain_community.llms.tongyi import Tongyi
# from AI大模型RAG与智能体开发.common.load_env import get_env

#
# model = Tongyi(
#     api_key=get_env("DASHSCOPE_API_KEY"),
#     model="qwen-max"
# )
# # 通过stream方法获得流式输出
# res = model.stream(input="你是谁,能做什么")
#
# for chunk in res:
#     print(chunk,end="",flush=True)

from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3:4b")
res = model.stream(input="你是谁,能做什么")
for chunk in res:
    print(chunk,end="",flush=True)