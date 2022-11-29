import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num =="=":
        siki = entry.get()
        ans = eval(siki)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    else:
        entry.insert(tk.END,num)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("tk")
    root.geometry("300x500")
    entry = tk.Entry(justify="right",width=10,font=("",40))
    entry.grid(row=0,column=0,columnspan=3)

    num = 0
    for i in range(10):

        button = tk.Button(root,text=f"{9-num}",font=("",30),width=4,height=2)
        button.grid(row = num//3+1, column=num%3)
        button.bind("<1>",button_click)
        num += 1

    option = ["+","="]
    for op in option:
        button = tk.Button(root,text=f"{op}",font=("",30),width=4,height=2)
        button.grid(row = num//3+1, column=num%3)
        button.bind("<1>",button_click)
        num +=1
    root.mainloop()