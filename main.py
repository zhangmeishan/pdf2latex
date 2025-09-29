
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key="sk-72af4e874dff479197ce77a4d8b29f52",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

xinput = "I just think the idea is not exciting since it is a combination of several modules. After the author response, I think the paper presents a work without significant flaws but overall rather boring to me. Thus my point is borderline reject."
task_description = "Please polish the above text in a more academic style. "
completion = client.chat.completions.create(
    model="qwen3-max-2025-09-23",
    messages=[
        {"role": "user", "content": xinput + " " + task_description},
    ],
    temperature=0.2,
    top_p=0.95,
    frequency_penalty=0,
    max_tokens=65536,
    stream=True,
)

print("output: \n")
for chunk in completion:
    print(chunk.choices[0].delta.content, end="", flush=True)
#print(completion.model_dump_json())

