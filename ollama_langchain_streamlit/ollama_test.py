import ollama

# 获得ollama的客户端对象
client = ollama.Client(host="http://localhost:11434")

# 列出可用模型
print(client.list())

# 展示模型详细信息
print(client.show('deepseek-r1:7b'))

# 列出正在运行的模型
print(client.ps())

# 和模型进行对话
while True:
    prompt = input("请输入问题 >")
    response = client.chat(
        model='deepseek-r1:7b',
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    print(response['message']['content'])