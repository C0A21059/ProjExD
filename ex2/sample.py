print("hello world")

import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

root = tk.Tk()
root.title("お試しか")
root.geometry("500x200")
label = tk.Label(root,
                text="ラベルを書いてみた件",
                font=("",20)
                )
label.pack()
button = tk.Button(root,text="押すな")
button.bind("<1>",button_click)
button.pack()

image = tk.PhotoImage(file="index.png")

canvas = tk.Canvas(width=50,height=80)
canvas.create_image(24,36.5,image=image)
canvas.pack()

entry = tk.Entry(width=30)
entry.insert(tk.END,"fugapiyo")
entry.pack()
root.mainloop()