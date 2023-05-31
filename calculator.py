import tkinter
import _pyinstaller_hooks_contrib
calculator = tkinter.Tk()
# 设置标题
calculator.title("计算器")
# 设置窗口尺寸以及出现的位置
calculator.geometry("440x500+1000+200")
# 设置背景颜色
calculator["background"] = "#EFEBE7"

# 显示结果的文本框
result = tkinter.StringVar()
# 设置文本框尺寸，对齐方式，颜色等(textvariable=result:将一个tkinter变量与文本框的内容绑定)
result_label = tkinter.Label(calculator, textvariable=result, font=('宋体', 30), width=21, height=2, anchor='e', background='#F5F5F5')
# 文本框位置
result_label.grid(row=0, column=0, columnspan=4, padx=4, pady=4)

# 清除文本框内容
def clear():
    # 设置result字符串的值为空字符串(清除内容)
    result.set("")

# 删除文本框中的最后一个字符
def delete():
    # 通过 result.get()获取文本框中的内容,用text储存
    text = result.get()
    # 使用切片操作 [:-1] 获取除了最后一个字符以外的所有字符
    result.set(text[:-1])

# 计算结果
def calculate():
    # 通过 result.get()获取文本框中的内容,用text储存
    text = result.get()
    try:
        # 使用eval()函数计算 text 中的表达式
        result.set(eval(text))
        # 添加到历史记录中
        history.append(text + " = " + result.get())
    except:
        # 如果计算失败返回 "Error"
        result.set("Error")
        # 添加到历史记录中
        history.append("Error")

# 历史记录列表
history = []
# 显示历史记录的窗口
def show_history():
    # 创建新窗口,并将其作为 calculator 窗口的子窗口
    history_window = tkinter.Toplevel(calculator)
    # 设置窗口标题
    history_window.title("历史记录")
    # 设置窗口尺寸以及出现的位置
    history_window.geometry("300x300+600+200")
    # 设置背景颜色
    history_window["background"] = "#EFEBE7"
    # 创建文本框显示历史记录
    history_text = tkinter.Text(history_window, font=("微软雅黑", 12), bg="#FFFFFF", width=30, height=15)
    # 将历史记录添加到文本框中
    for everytext in history:
        # 使用tkinter.END作为索引值确保新插入的文本始终出现在文本框的最后面
        history_text.insert(tkinter.END, everytext + "\n")
    # 使用 pack 方法将文本框放置在窗口中
    history_text.pack()

# 创建按钮
button_CE1 = tkinter.Button(calculator, text='C', width=8, height=2, font=('宋体', 16), relief='ridge',
                           pady=2, background='#FFFACD', command=lambda: clear())
button_CE2 = tkinter.Button(calculator, text='E', width=8, height=2, font=('宋体', 16), relief='ridge',
                           pady=2, background='#FFFACD', command=lambda: clear())
button_percent = tkinter.Button(calculator, text='%', width=8, height=2, font=('宋体', 16), relief='ridge',
                           padx=2, pady=2, background='#FFFACD', command=lambda: result.set(str(float(result.get())/100)))
button_delete = tkinter.Button(calculator, text='←', width=8, height=2, font=('宋体', 16), relief='ridge',
                           padx=2, pady=2, background='#FFFACD', command=lambda: delete())
button_inverse_proportion = tkinter.Button(calculator, text='1/X', width=8, height=2, font=('宋体', 16), relief='ridge',
                           padx=2, pady=2, background='#FFFACD', command=lambda: result.set(str(1/float(result.get()))))
button_square = tkinter.Button(calculator, text='X²', width=8, height=2, font=('宋体', 16), relief='ridge',
                           padx=2, pady=2, background='#FFFACD', command=lambda: result.set(str(float(result.get())**2)))
button_square_root = tkinter.Button(calculator, text='√X', width=8, height=2, font=('宋体', 16), relief='ridge',
                           padx=2, pady=2, background='#FFFACD', command=lambda: result.set(str(float(result.get())**0.5)))
button_divide = tkinter.Button(calculator, text='÷', width=8, height=2, font=('宋体', 16), relief='ridge',
                           padx=2, pady=2, background='#FFFACD', command=lambda: result.set(result.get()+'/'))
button_7 = tkinter.Button(calculator, text='7', width=8, height=2, font=('宋体', 16), relief='ridge',
                           padx=2, pady=2, background='#E1FFFF', command=lambda: result.set(result.get()+'7'))
button_8 = tkinter.Button(calculator, text='8', width=8, height=2, font=('宋体', 16), relief='ridge',
                           padx=2, pady=2, background='#E1FFFF', command=lambda: result.set(result.get()+'8'))
button_9 = tkinter.Button(calculator, text='9', width=8, height=2, font=('宋体', 16), relief='ridge',
                           padx=2, pady=2, background='#E1FFFF', command=lambda: result.set(result.get()+'9'))
button_X = tkinter.Button(calculator, text='X', width=8, height=2, font=('宋体', 16), relief='ridge',
                           padx=2, pady=2, background='#FFFACD', command=lambda: result.set(result.get()+'*'))
button_4 = tkinter.Button(calculator, text='4', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#E1FFFF', command=lambda: result.set(result.get()+'4'))
button_5 = tkinter.Button(calculator, text='5', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#E1FFFF', command=lambda: result.set(result.get()+'5'))
button_6 = tkinter.Button(calculator, text='6', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#E1FFFF', command=lambda: result.set(result.get()+'6'))
button_minus = tkinter.Button(calculator, text='-', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#FFFACD', command=lambda: result.set(result.get()+'-'))
button_1 = tkinter.Button(calculator, text='1', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#E1FFFF', command=lambda: result.set(result.get()+'1'))
button_2 = tkinter.Button(calculator, text='2', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#E1FFFF', command=lambda: result.set(result.get()+'2'))
button_3 = tkinter.Button(calculator, text='3', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#E1FFFF', command=lambda: result.set(result.get()+'3'))
button_plus = tkinter.Button(calculator, text='+', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#FFFACD', command=lambda: result.set(result.get()+'+'))
button_0 = tkinter.Button(calculator, text='0', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#E1FFFF', command=lambda: result.set(result.get()+'0'))
button_history = tkinter.Button(calculator, text='history', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#E1FFFF', command=lambda: show_history())
button_point = tkinter.Button(calculator, text='.', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#E1FFFF', command=lambda: result.set(result.get()+'.'))
button_equal = tkinter.Button(calculator, text='=', width=8, height=2, font=('宋体', 16), relief='ridge',
                           background='#FFFACD', command=lambda: calculate())

# 布局按钮
button_CE1.grid(padx=4, pady=4, row=1, column=0)
button_CE2.grid(padx=0, pady=4, row=1, column=1)
button_percent.grid(padx=4, pady=4, row=1, column=2)
button_delete.grid(padx=4, pady=4, row=1, column=3)
button_inverse_proportion.grid(padx=4, pady=4, row=2, column=0)
button_square.grid(padx=4, pady=4, row=2, column=1)
button_square_root.grid(padx=4, pady=4, row=2, column=2)
button_divide.grid(padx=4, pady=4, row=2, column=3)
button_7.grid(padx=4, pady=4, row=3, column=0)
button_8.grid(padx=4, pady=4, row=3, column=1)
button_9.grid(padx=4, pady=4, row=3, column=2)
button_X.grid(padx=4, pady=4, row=3, column=3)
button_4.grid(padx=4, pady=4, row=4, column=0)
button_5.grid(padx=4, pady=4, row=4, column=1)
button_6.grid(padx=4, pady=4, row=4, column=2)
button_minus.grid(padx=4, pady=4, row=4, column=3)
button_1.grid(padx=4, pady=4, row=5, column=0)
button_2.grid(padx=4, pady=4, row=5, column=1)
button_3.grid(padx=4, pady=4, row=5, column=2)
button_plus.grid(padx=4, pady=4, row=5, column=3)
button_0.grid(padx=4, pady=4, row=6, column=0)
button_history.grid(padx=4, pady=4, row=6, column=1)
button_point.grid(padx=4, pady=4, row=6, column=2)
button_equal.grid(padx=4, pady=4, row=6, column=3)

# 进入消息循环
calculator.mainloop()

