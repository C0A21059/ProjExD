import tkinter as tk
import tkinter.messagebox as tkm

def count_up():
    global tmr
    label["text"] = tmr
    tmr = tmr+1
    root.after(1000,count_up)

def key_down(event):
    key = event.keysym
    root.after(1000,count_up)
    tkm.showinfo("キー押下", f"{key}キーが押されました")

if __name__ == "__main__":
    root = tk.Tk()
    label= tk.Label(root, text="-", font=("", 80))
    label.pack()

    tmr = 0
    #count_up()
    root.bind("<KeyPress>", key_down)
    root.mainloop()