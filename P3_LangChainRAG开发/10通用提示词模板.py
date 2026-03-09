# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：10通用提示词模板.py
@Author  ：九成八
@Date    ：2026/3/7 15:24 
"""
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
from AI大模型RAG与智能体开发.common.load_env import get_env

# zero-shot
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字，简单回答。"
)
model = Tongyi(
    api_key=get_env("DASHSCOPE_API_KEY"),
    model="qwen-max"
)
# 调用.format方法注入信息即可
# prompt_text = prompt_template.format(lastname="张", gender="女儿")
#
# model = Tongyi(model="qwen-max")
# res = model.invoke(input=prompt_text)
# print(res)

chain = prompt_template | model

res = chain.invoke(input={"lastname": "张", "gender": "女儿"})
print(res)
