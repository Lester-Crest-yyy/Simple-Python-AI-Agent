#这份是手打的第二个文件，没写完
import os
from openai import OpenAI
import window

script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, "config.txt")

with open(save_path, "r", encoding="utf-8") as fp:
    # 读所有行，剔除换行、跳过空行
    data_list = [line.strip() for line in fp if line.strip()]


# data_list[0] → API Key
# data_list[1] → HTTP
# data_list[2] → 模型名称

client = OpenAI(
    api_key=data_list[0],
    base_url=data_list[1],   # 换成国产模型就改这里
)

resp = client.chat.completions.create(
    model=data_list[2],
    messages=[
        {"role": "system", "content": "你是简洁的助手"},
        {"role": "user", "content": UserProblem},
    ],
    temperature=0.7,
    max_tokens=1024,
)
