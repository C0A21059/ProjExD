import tkinter as tk

def count_up():
    global tmr
    label["text"] = tmr
    tmr = tmr+1
    root.after(1000,count_up)

if __name__ == "__main__":
    root = tk.Tk()
    label= tk.Label(root, text="-", font=("", 80))
    label.pack()

    tmr = 0
    count_up()
    root.mainloop()