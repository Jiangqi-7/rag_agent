# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：18RunnableLambda的基础使用.py
@Author  ：九成八
@Date    ：2026/3/7 22:06 
"""
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from AI大模型RAG与智能体开发.common.load_env import get_env

model = ChatTongyi(
    api_key=get_env("DASHBOARD_API_KEY"),
    model="qwen3-max"
)
str_parser = StrOutputParser()

first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请帮忙起名字，仅生成一个名字，并告知我名字，不要额外信息。"
)

second_prompt = PromptTemplate.from_template(
    "姓名{name}，请帮我解析含义。"
)

# 函数的入参：AIMessage -> dict  ({"name": "xxx"})
# my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

chain = first_prompt | model | (lambda ai_msg: {"name": ai_msg.content}) | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "曹", "gender": "女孩"}):
    print(chunk, end="", flush=True)