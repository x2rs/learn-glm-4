# 在__api_key文件填写您自己的APIKey

model_name = "glm-4-flash" # 填写需要调用的模型名称

with open("__api_key",mode="r") as f:
    __api_key = f.read()

with open("__system_prompt.md", mode="r", encoding='utf-8') as f:
    __system_prompt = f.read()

from zhipuai import ZhipuAI
client = ZhipuAI(api_key=__api_key)

system_prompt = __system_prompt

messages_and_history=[
    {"role": "system", "content": system_prompt}
]

while True:
    message=input("user >>> ")
    messages_and_history.append(
        {"role": "user", "content": message}
    )
    response = client.chat.completions.create(
        model=model_name,
        messages=messages_and_history,
        stream=True,
        temperature=0.0
    )
    contents=[]
    for chunk in response:
        contents.append(chunk.choices[0].delta.content)
    response_message = ''.join(contents)
    print(f"{model_name} >>> {response_message}")
    messages_and_history.append(
        {"role": "assistant", "content": response_message}
    )




