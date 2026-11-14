#这份是AI生成的
#导入模块
import os
import threading
import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI

#类

#赋值变量
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.txt")

window = tk.Tk()
uAIAPI = tk.StringVar()
uAIHTTP = tk.StringVar()
uAIMoudel = tk.StringVar()
history = []          #多轮对话历史
busy = False          #是否正在请求

#设置函数

def SaveConfig():
    a = f"""{uAIAPI.get().strip()}
{uAIHTTP.get().strip()}
{uAIMoudel.get().strip()}"""
    with open(config_path, "w", encoding="utf-8") as file:
        file.write(a)
    Output("配置已保存到 config.txt")

def LoadConfig():
    if not os.path.exists(config_path):
        Output("没有找到 config.txt")
        return
    with open(config_path, "r", encoding="utf-8") as file:
        data_list = [line.strip() for line in file if line.strip()]
    if len(data_list) >= 3:
        uAIAPI.set(data_list[0])
        uAIHTTP.set(data_list[1])
        uAIMoudel.set(data_list[2])
        Output("已读取配置")
    else:
        Output("config.txt 内容不足三行")

def Output(text):
    Text_Out.configure(state="normal")
    Text_Out.insert("end", text + "\n")
    Text_Out.see("end")
    Text_Out.configure(state="disabled")

def AskAI():
    global busy
    if busy:
        return
    question = Text_In.get("1.0", "end").strip()
    if not question:
        return
    api_key = uAIAPI.get().strip()
    base_url = uAIHTTP.get().strip()
    model = uAIMoudel.get().strip()
    if not api_key or not model:
        Output("请先填写 AI_API 和 AI_Moudel")
        return

    Text_In.delete("1.0", "end")
    Output(f"你: {question}")
    Output("AI: 思考中...")

    history.append({"role": "user", "content": question})
    busy = True
    Button_Send.configure(state="disabled")

    def work():
        try:
            client = OpenAI(api_key=api_key, base_url=base_url or None, timeout=60)
            resp = client.chat.completions.create(model=model, messages=history)
            answer = resp.choices[0].message.content or ""
            history.append({"role": "assistant", "content": answer})
            window.after(0, lambda: Output(f"AI(原文): {answer}\n"))
        except Exception as e:
            history.pop()
            window.after(0, lambda: Output(f"出错: {e}\n"))
        finally:
            window.after(0, done)

    def done():
        global busy
        busy = False
        Button_Send.configure(state="normal")

    threading.Thread(target=work, daemon=True).start()

def ClearChat():
    history.clear()
    Text_Out.configure(state="normal")
    Text_Out.delete("1.0", "end")
    Text_Out.configure(state="disabled")

#窗口设置
window.title("AI_Agent")
window.geometry("900x760")

#标签
tk.Label(window, text='简易AI_Agent', font=('宋体', 25)).pack(pady=10)
tk.Label(window, text='AI_API', font=('宋体', 16)).place(x=30, y=70)
tk.Label(window, text='AI_HTTP', font=('宋体', 16)).place(x=30, y=115)
tk.Label(window, text='AI_Moudel', font=('宋体', 16)).place(x=30, y=160)

#设置输入框
tk.Entry(window, textvariable=uAIAPI, font=('宋体', 14), width=40).place(x=160, y=70)
tk.Entry(window, textvariable=uAIHTTP, font=('宋体', 14), width=40).place(x=160, y=115)
tk.Entry(window, textvariable=uAIMoudel, font=('宋体', 14), width=40).place(x=160, y=160)

#设置按钮
tk.Button(window, command=SaveConfig, text='保存配置', font=('宋体', 14), width=12).place(x=520, y=70)
tk.Button(window, command=LoadConfig, text='读取配置', font=('宋体', 14), width=12).place(x=520, y=115)
tk.Button(window, command=ClearChat, text='清空对话', font=('宋体', 14), width=12).place(x=520, y=160)

#输出区
Text_Out = scrolledtext.ScrolledText(window, font=('宋体', 12), wrap="word")
Text_Out.place(x=30, y=215, width=840, height=380)
Text_Out.configure(state="disabled")

#输入区
Text_In = tk.Text(window, font=('宋体', 12), height=4, wrap="word")
Text_In.place(x=30, y=610, width=840, height=90)
Button_Send = tk.Button(window, command=AskAI, text='发送问题', font=('宋体', 14), width=12)
Button_Send.place(x=30, y=710)
tk.Label(window, text='回车换行，点击按钮发送', font=('宋体', 10)).place(x=170, y=722)

#启动时读取配置
LoadConfig()

#打开窗口
window.mainloop()
