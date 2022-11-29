import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

root = tk.Tk()
root.title("tk")
root.geometry("300x500")
entry = tk.Entry(justify="right",width=10,font=("",40))
entry.grid(row=0,column=0,columnspan=3)
for i in range(12):
    if 9<i:
        if i ==11:
            button = tk.Button(root,text=f"=",font=("",30),width=4,height=2)
            button.grid(row = i//3+1, column=i%3)
            button.bind("<1>",button_click)
        elif i ==10:
            button = tk.Button(root,text=f"+",font=("",30),width=4,height=2)
            button.grid(row = i//3+1, column=i%3)
            button.bind("<1>",button_click)
    else:
        button = tk.Button(root,text=f"{9-i}",font=("",30),width=4,height=2)
        button.grid(row = i//3+1, column=i%3)
        button.bind("<1>",button_click)
"""
button8 = tk.Button(root,text="8",font=("",30),width=4,height=2)
button8.grid(row = 0, column=1)
button8.bind("<1>",button_click)

button8 = tk.Button(root,text="7",font=("",30),width=4,height=2)
button8.grid(row = 0, column=1)
button8.bind("<1>",button_click)
"""
root.mainloop()
