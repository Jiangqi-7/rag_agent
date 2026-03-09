import time

import streamlit as st

# 测试标题
st.title("Streamlit Test")

# 在网页中渲染提供的内容
st.write("你好小伙子")

# 分隔符
st.divider()

# 聊天输入框
name = st.chat_input("请输入你的名字")
if name:
    st.write(f"你好:{name}")

# 等待提示框
with st.spinner("思考中"):
    time.sleep(5)
    st.write("思考完成")

# 消息容器
# 角色支持: user、assistant、ai、human
st.chat_message('user').markdown('你是谁')
st.chat_message('assistant').markdown('我是你的小娇妻')

