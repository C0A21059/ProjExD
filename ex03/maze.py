import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx,cy, mx, my
    if key == "Up":
        if maze_lis[mx][my-1] !=1:
            cy =cy - 100*my
            my -= 1
    if key == "Down":
        if maze_lis[mx][my+1] !=1:
            cy += 100*my
            my += 1
    if key == "Left":
        if maze_lis[mx-1][my] !=1:
            cx -= 100*mx
            mx -= 1
    if key == "Right":
        if maze_lis[mx+1][my] !=1:
            cx += 100*mx
            mx += 1
    cx,cy = 50 +mx*100, 50+my*100
    canvas.coords("kokaton", cx, cy)
    root.after(100,main_proc)



if __name__ == "__main__":
    key = ""
    mx,my = 1, 1
    cx,cy = 50 +mx*100, 50+my*100

    root = tk.Tk()
    root.title("迷えるこうかとん")
    image = tk.PhotoImage(file="fig/0.png")

    canvas = tk.Canvas(width=1500,height=900,bg="#000000")
    canvas.pack()

    maze_lis = mm.make_maze(15,9)
    #print(maze_lis)
    mm.show_maze(canvas, maze_lis)
    canvas.create_image(cx, cy,
                        image=image,
                        tag="kokaton")

    root.bind("<KeyPress>", key_down)
    main_proc()
    root.bind("<KeyRelease>", key_up)
    root.mainloop()