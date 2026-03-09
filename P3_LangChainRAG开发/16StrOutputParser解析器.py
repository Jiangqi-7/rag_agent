# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：16StrOutputParser解析器.py
@Author  ：九成八
@Date    ：2026/3/7 21:40 
"""
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from AI大模型RAG与智能体开发.common.load_env import get_env

parser = StrOutputParser()
model = ChatTongyi(
    api_key=get_env("DASHSCOPE_API_KEY"),
    model="qwen3-max"
)
prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请起名，仅告知我名字无需其它内容。"
)

chain = prompt | model | parser | model | parser

res: str = chain.invoke({"lastname": "张", "gender": "女儿"})
print(res)
print(type(res))