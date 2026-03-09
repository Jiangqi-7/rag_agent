# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：09LangChain访问Ollama的本地嵌入模型.py
@Author  ：九成八
@Date    ：2026/3/7 15:15 
"""
from langchain_ollama import OllamaEmbeddings

# 创建模型对象 不传model默认用的是 text-embeddings-v1 1536维度
model = OllamaEmbeddings(model="qwen3-embedding:4b")

# 不用invoke stream
# embed_query、embed_documents
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "我稀饭你", "晚上吃啥"]))