import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("tk")
    root.geometry("300x500")
    for i in range(10):

        button = tk.Button(root,text=f"{9-i}",font=("",30),width=4,height=2)
        button.grid(row = i//3, column=i%3)
        button.bind("<1>",button_click)

    root.mainloop()