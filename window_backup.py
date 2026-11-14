#导入模块
import tkinter as tk
import openai as ai

#类
class InputAI():
    pass

#赋值变量
window = tk.Tk()
UserMaxSize=window.maxsize()
print(UserMaxSize)
k,g=UserMaxSize
uAIAPI=tk.StringVar()
uAIHTTP=tk.StringVar()
uAIMoudel=tk.StringVar()

#设置函数

#窗口设置
window.title("AI_Agent(设置AI)")
window.geometry(f'{k}x{g}')
#标签
Label_Title=tk.Label(window,text='简易AI_Agent',font=('宋体',25))
Label_Title.pack()
Label_AI_API=tk.Label(window,text='AI_API',font=('宋体',20)).place(x=50,y=100)
Label_AI_HTTP=tk.Label(window,text='AI_HTTP',font=('宋体',20)).place(x=50,y=150)
Label_AI_Moudel=tk.Label(window,text='AI_Moudel',font=('宋体',20)).place(x=50,y=200)

#设置输入框
tk.Entry(window,textvariable=uAIAPI,font=('宋体',20)).place(x=140,y=100)
tk.Entry(window,textvariable=uAIHTTP,font=('宋体',20)).place(x=160,y=150)
tk.Entry(window,textvariable=uAIMoudel,font=('宋体',20)).place(x=180,y=200)

#设置按钮函数
def InputAI():
    pass

#设置按钮
tk.Button(window,command=InputAI(),text='读取AI配置',font=('宋体',20),width=15).place(x=180,y=250)

#打开窗口
window .mainloop()