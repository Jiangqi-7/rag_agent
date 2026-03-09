import streamlit as st
from langchain_util import get_response
from dotenv import load_dotenv
import os

# 加载.env文件（默认读取项目根目录的.env）
# 如果.env文件不在根目录，可指定路径：load_dotenv(dotenv_path="./config/.env")
load_dotenv()
api_key = os.getenv("LANGCHAIN_API_KEY")

# 初始化消息记录
if "message" not in st.session_state:
    st.session_state["message"] = []

# 添加标题
st.title("三秒的智能小娇妻")
# 添加分割线
st.divider()

# 用户输入
prompt = st.chat_input("请输入你的问题 >")

if prompt:
    # 将用户提问添加到历史记录中
    st.session_state["message"].append({"role": "user","content": prompt})
    # 将历史消息全部输入到消息容器
    for message in st.session_state["message"]:
        st.chat_message(message["role"]).markdown(message["content"])

    with st.spinner("娇妻思考中..."):
       response = get_response(prompt,api_key=api_key)

       # 从response中取出message和content两个key
       st.session_state["message"].append({"role": "assistant","content": response})
       # 在页面中渲染AI的回答
       st.chat_message("assistant").markdown(response)