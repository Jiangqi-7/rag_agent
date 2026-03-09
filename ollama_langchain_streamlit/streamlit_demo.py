import time
import streamlit as st

if "message" not in st.session_state:
    st.session_state["message"] = []

# 给予标题
st.title("三秒的小娇妻")

# 分割线
st.divider()

# 消息输入框
prompt = st.chat_input("请输入你的问题 >")

# 历史消息记录 1.角色 2.消息 [{"role": "user/assistant","content": "xxx"},{"role": "user/assistant","content": "xxx"}]

# 消息容器
if prompt:
    st.session_state["message"].append({"role": "user", "content": prompt})
    for message in st.session_state["message"]:
        # 用户提问
        st.chat_message(message["role"]).markdown(message["content"])

    # AI回答
    with st.spinner("思考中..."):
        time.sleep(1)
        response = f"我不会{st.session_state['message']}"
        st.session_state("assistant").markdown(prompt)

        # 把AI回答渲染到界面中
        st.chat_message("assistant").markdown(response)
