import streamlit as st
import ollama

# 获取ollama客户端
client = ollama.Client(host='http://localhost:11434')

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
       response = client.chat(
            model="deepseek-r1:7b",
            messages=[{"role": "user","content": prompt}]
        )

       # 从response中取出message和content两个key
       st.session_state["message"].append({"role": "assistant","content": response["message"]["content"]})
       # 在页面中渲染AI的回答
       st.chat_message("assistant").markdown(response["message"]["content"])