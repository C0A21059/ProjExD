import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, key
    if key == "Up": cy -= 20
    if key == "Down": cy += 20
    if key == "Left": cx -= 20
    if key == "Right": cx += 20
    canvas.coords("kokaton", cx, cy)
    root.after(100,main_proc)



if __name__ == "__main__":
    cx = 300
    cy = 400
    key = ""

    root = tk.Tk()
    root.title("迷えるこうかとん")
    image = tk.PhotoImage(file="fig/0.png")

    canvas = tk.Canvas(width=1500,height=900,bg="#000000")
    canvas.create_image(cx, cy,
                        image=image,
                        tag="kokaton")
    canvas.pack()

    root.bind("<KeyPress>", key_down)
    main_proc()
    root.bind("<KeyRelease>", key_up)
    root.mainloop()