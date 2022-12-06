import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key,mode
    key = event.keysym
    if key =="a":
        if mode ==0:
            mode = 1
        else:
            mode =0

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx,cy, mx, my,index
    #辞書のキーを押したキーの判定、値に次のマスの判定、成功したときの横の移動量、縦の移動量,増殖するこうかとんの画像識別
    data = {key == "Up": [maze_lis[mx][my-1] !=1, 0, -1, 1],
            key == "Down": [maze_lis[mx][my+1] !=1, 0, 1, 2],
            key == "Left": [maze_lis[mx-1][my] !=1, -1, 0, 3],
            key == "Right": [maze_lis[mx+1][my] !=1, 1, 0, 4]}
    for k,v in data.items():
        if k:
            if v[0]:
                mx += v[1]
                my += v[2]
                index = v[3]

    cx, cy = 50 + mx*100, 50 + my*100
    canvas.coords("kokaton", cx, cy)
    if mode ==1:
        canvas.create_image(cx, cy,
                        image=png[index],
                        tag="kokaton")
    root.after(100,main_proc)


if __name__ == "__main__":
    key = ""
    mx,my = 1, 1
    cx,cy = 50 +mx*100, 50+my*100
    index = 0
    mode =0

    root = tk.Tk()
    root.title("迷えるこうかとん")

    png = [tk.PhotoImage(file="fig/0.png"),
            tk.PhotoImage(file="fig/1.png"),
            tk.PhotoImage(file="fig/2.png"),
            tk.PhotoImage(file="fig/3.png"),
            tk.PhotoImage(file="fig/4.png")]

    canvas = tk.Canvas(width=1500,height=900,bg="#000000")
    canvas.pack()

    maze_lis = mm.make_maze(15,9)
    #print(maze_lis)
    mm.show_maze(canvas, maze_lis)
    canvas.create_image(cx, cy,
                        image=png[index],
                        tag="kokaton")

    root.bind("<KeyPress>", key_down)
    main_proc()
    root.bind("<KeyRelease>", key_up)
    root.mainloop()