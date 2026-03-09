import ollama,streamlit as st

print(f"ollama当前可用的模型有：{ollama.list()}")
print(f"streamlit库的版本是：{st.__version__}")