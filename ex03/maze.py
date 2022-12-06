import tkinter as tk

if __name__ == "__main__":
    cx = 300
    cy = 400

    root = tk.Tk()
    root.title("迷えるこうかとん")
    image = tk.PhotoImage(file="fig/0.png")

    canvas = tk.Canvas(width=1500,height=900,bg="#000000")
    canvas.create_image(cx, cy, image=image)
    canvas.pack()
    root.mainloop()