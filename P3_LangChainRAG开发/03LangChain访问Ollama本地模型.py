# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：03LangChain访问Ollama本地模型.py
@Author  ：九成八
@Date    ：2026/3/7 13:52 
"""
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="deepseek-r1:7b")
res = model.invoke(input="你是谁,能做什么?")
print(res)

