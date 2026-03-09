# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：08LangChain访问阿里云嵌入模型.py
@Author  ：九成八
@Date    ：2026/3/7 15:10 
"""
from langchain_community.embeddings import DashScopeEmbeddings
from AI大模型RAG与智能体开发.common.load_env import get_env
# 创建模型对象 不传model默认用的是 text-embeddings-v1 1536维度
model = DashScopeEmbeddings(dashscope_api_key=get_env("DASHSCOPE_API_KEY"))

# 不用invoke stream
# embed_query、embed_documents
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "我稀饭你", "晚上吃啥"]))