# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：17JsonOutputParser解析器.py
@Author  ：九成八
@Date    ：2026/3/7 21:50 
"""
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from AI大模型RAG与智能体开发.common.load_env import get_env

# 创建所需的解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

# 模型创建
model = ChatTongyi(
    api_key=get_env("DASHBOARD_API_KEY"),
    model="qwen3-max"
)

# 第一个提示词模板
first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请帮忙起名字，"
    "并封装为JSON格式返回给我。要求key是name，value就是你起的名字，请严格遵守格式要求。"
)

# 第二个提示词模板
second_prompt = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义。"
)

# 构建链   （AIMessage("{name: 张若曦}")
chain = first_prompt | model | json_parser | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "张", "gender": "女儿"}):
    print(chunk, end="", flush=True)