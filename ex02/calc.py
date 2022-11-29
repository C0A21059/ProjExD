import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num =="=":
        siki = entry.get()
        ans = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, ans)
    elif num =="C":
        #Cが検出された場合全て削除
        entry.delete(0, tk.END)
    elif num =="CE":
        back = len(entry.get())-1
        entry.delete(back, tk.END)
    elif num =="%":
        parsent = eval(entry.get())*100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(parsent)+"%")
    elif num =="√":
        square = eval(entry.get())**(1/2)
        entry.delete(0, tk.END)
        entry.insert(tk.END, square)
    else:
        entry.insert(tk.END, num)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("tk")
    root.geometry("400x600")
    entry = tk.Entry(justify="right",width=10,font=("",40))
    entry.grid(row=0,column=0,columnspan=4)

    num = 0
    for i in range(10):
        if i ==9:
            button = tk.Button(root,text=f"{9-num}",font=("",30), width = 4, height = 2, bg="#ffffff")#数字の色変更、0のみ真ん中の4段目に移動
            button.grid(row = num // 3 + 2, column = num % 3 +1)
            button.bind("<1>", button_click)
        else:
            button = tk.Button(root,text=f"{9-num}",font=("",30), width = 4, height = 2, bg="#ffffff")#数字の色変更
            button.grid(row = num // 3 + 2, column = num % 3)
            button.bind("<1>", button_click)
        num += 1

    option = ["/", "*", "-", "+", "="]#演算子の追加はここに
    for op in option:
        button = tk.Button(root, text = f"{op}", font=("", 30), width = 4, height = 2)
        button.grid(row = num % len(option)+1 , column = 4)
        button.bind("<1>", button_click)
        num += 1

    option_5 = ["C","."]#数字の下に置く5段目のオールクリアのCと小数点.を入れている。そのためrowの位置は固定
    for i,op in enumerate(option_5):
        button = tk.Button(root,text=f"{op}", font=("", 30), width = 4, height = 2)
        button.grid(row = 5, column = i * 2)
        button.bind("<1>", button_click)

    option_1 = ["√", "%", "CE"]#
    for i,op in enumerate(option_1):
        button = tk.Button(root,text=f"{op}", font=("", 30), width = 4, height = 2)
        button.grid(row = 1, column = i)
        button.bind("<1>", button_click)
    root.mainloop()