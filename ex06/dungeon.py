import pygame as pg
import sys
import random

WIDTH = 880 #ウィンドウの横幅
HEIGHT = 720 #ウィンドウの縦幅
MAZE_W = 11
MAZE_H = 9
maze = [[0]*MAZE_W for _ in range(MAZE_H)]

imgBtlBG = pg.image.load("ex06/btlbg.png")         #背景画像のSurface
imgEffect = pg.image.load("ex06/zangeki.png")      #斬撃エフェクトのSurface
imgEffect_magic = pg.image.load("ex06/magic2.png") #魔法エフェクトのSurface
imgEnemy = pg.image.load("ex06/dragon.png")        #敵エネミー（ドラゴン）のSurface
imgEnemy = pg.transform.rotozoom(imgEnemy, 0, 0.5) #画像の大きさを半分に
emy_x = WIDTH/2-imgEnemy.get_width()/2             #横の描画位置をウィンドウの中心に
emy_y = HEIGHT-imgEnemy.get_height()               #縦の描画位置をウィンドウの中心に
#敵エネミーの変数
emy_step = 0
emy_blink = 0
dmg_eff = 0
emy_life = 3000
COMMAND = ["[A]ttack", "[I]tems", "[M]agic", "[R]un"] #Playerのコマンドのリスト

message = [""]*10 #Playerと敵エネミーの行動リスト

def make_maze():
    #ダンジョンの迷路を作成
    XP = [ 0, 1, 0,-1]
    YP = [-1, 0, 1, 0]

    #周りの壁
    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[MAZE_H-1][x] = 1
    for y in range(1, MAZE_H-1):
        maze[y][0] = 1
        maze[y][MAZE_W-1] = 1

    #中を何もない状態に
    for y in range(1, MAZE_H-1):
        for x in range(1, MAZE_W-1):
            maze[y][x] = 0

    #柱
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
            maze[y][x] = 1

    #柱から上下左右に壁を作る
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
            d = random.randint(0, 3)
        if x > 2: # 二列目からは左に壁を作らない
            d = random.randint(0, 2)
        maze[y+YP[d]][x+XP[d]] = 1
    maze[MAZE_H-2][MAZE_W-2] = 2

def move_player(pl_x,pl_y, player_rct,mode): # 主人公の移動
    key_dct = pg.key.get_pressed()
    #キーに押したボタンの判定、値に[次のマスの判定,[playerのマスの値,playerの移動距離]]
    key_delta = {
        pg.K_UP:    [maze[pl_y-1][pl_x] != 1, [0, -1, 0, -HEIGHT/MAZE_H]],
        pg.K_DOWN:  [maze[pl_y+1][pl_x] != 1, [0, +1, 0, +HEIGHT/MAZE_H]],
        pg.K_LEFT:  [maze[pl_y][pl_x-1] != 1, [-1, 0, -WIDTH/MAZE_W, 0]],
        pg.K_RIGHT: [maze[pl_y][pl_x+1] != 1, [+1, 0, +WIDTH/MAZE_W, 0]],
    }
    for key, delta in key_delta.items():
        #キーの判定
        if key_dct[key]:
            #次のマスの判定
            if delta[0]:
                #playerのマスの値と移動距離を更新
                pl_x += delta[1][0]
                pl_y += delta[1][1]
                player_rct.centerx += delta[1][2]
                player_rct.centery += delta[1][3]
    #迷路のマスが2であれば戦闘画面に移行
    if maze[pl_y][pl_x] == 2:
        mode = 1
    return pl_x,pl_y,mode


def init_message():
    #戦闘画面の文字列が入るリストを空のリストで用意
    for i in range(10):
        message[i] = ""


def set_message(msg):
    #引数：Playerもしくは敵エネミーの行動
    for i in range(len(message)):
        #messageが空なら追加
        if message[i] == "":
            message[i] = msg
            return
    #空でない場合、上に一つメッセージをずらし、最後に新しいメッサージを追加
    for i in range(len(message)-1):
        message[i] = message[i+1]
    message[-1] = msg


def draw_text(bg, txt, x, y, fnt, col):
    """
    bg  :背景のSurface
    txt :描画する文字列の入ったリスト
    x   :横の描画開始位置
    y   :縦の描画開始位置
    fnt :fontのSurface
    col :色
    """
    sur = fnt.render(txt, True, (  0,  0,  0))
    bg.blit(sur, [x+1, y+2])
    sur = fnt.render(txt, True, col)
    bg.blit(sur, [x, y])

def draw_battle(bg, fnt):
    global emy_blink, dmg_eff
    bx = 0
    by = 0

    if dmg_eff > 0: #敵エネミーの行動をする際に画像を上下させるために描画位置を更新
        dmg_eff = dmg_eff - 1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)
    bg.blit(imgBtlBG, [bx, by])
    if emy_blink%2 == 0: #偶然の場合はエネミーの画像を描画
        bg.blit(imgEnemy, [emy_x, emy_y+emy_step])
    if emy_blink > 0: #奇数の場合はカウントだけ更新し、攻撃を受けた際に点滅しているように描画
        emy_blink = emy_blink - 1
    for i in range(10): #Playerと敵エネミーの行動を描画
        draw_text(bg, message[i], WIDTH-200, 100+i*50, fnt, (255,255,255))

def battle_command(bg, fnt):
    #バトルコマンドを描画
    for i in range(len(COMMAND)):
        draw_text(bg, COMMAND[i], 20, 360+60*i, fnt, (255,255,255))

def main():
    global emy_step, emy_blink, dmg_eff, emy_life
    pg.display.set_caption("不思議のダンジョン") #タイトルバーに「不思議のダンジョン」と表示する
    screen = pg.display.set_mode((WIDTH, HEIGHT)) #(880,720)の画面Surfaceを生成する
    clock = pg.time.Clock()

    make_maze()

    player_sfc = pg.Surface((80,80)) #正方形の空のSurface
    player_sfc.set_colorkey("black") #四隅の黒を透明に
    pg.draw.circle(player_sfc, (255, 0, 0), (40, 40), 40) #Surface内の色、位置、半径を指定
    player_rct = player_sfc.get_rect() #Rect
    player_rct.center = 120, 120
    screen.blit(player_sfc, player_rct) #blit

    pl_x = 1 #Playerの横マス開始位置
    pl_y = 1 #Playerの縦マス開始位置
    mode = 0 #迷路画面と戦闘画面の切り替え変数
    turn = 0 #どの行動を行うか判定に使う変数
    tmr = 0  #どの描画をするか判定に使う変数

    font = pg.font.Font(None, 30) #fontの描画に使うSurface

    init_message() #メッサージを入れるリストを作成
    while True:
        #迷路画面
        if mode == 0:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            #迷路の描画を行う
            for y in range(MAZE_H):
                for x in range(MAZE_W):
                    W = WIDTH / MAZE_W
                    H = HEIGHT / MAZE_H
                    X = x*W
                    Y = y*H
                    if maze[y][x] == 0: # 通路
                        pg.draw.rect(screen, (255,255,255), [X, Y, W, H])
                    if maze[y][x] == 1: # 壁
                        pg.draw.rect(screen, ( 96,  96,  96), [X, Y, W, H])
                    if maze[y][x] == 2:
                        pg.draw.rect(screen, (0,0,255), [X, Y, W, H])
            #Playerの描画と位置の更新
            pl_x, pl_y,mode = move_player(pl_x,pl_y, player_rct,mode)
            screen.blit(player_sfc, player_rct) #blit
        #戦闘画面
        if mode ==1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            draw_battle(screen, font)
            tmr = tmr + 1
            key = pg.key.get_pressed()

            if turn == 0: # 戦闘開始
                if tmr == 1: set_message("Encounter!")
                if tmr == 6:
                    turn = 1
                    tmr = 0

            elif turn == 1: # プレイヤー入力待ち
                if tmr == 1: set_message("Your turn.")
                battle_command(screen, font)
                if key[pg.K_a] == 1 or key[pg.K_SPACE] == 1:
                    turn = 2
                    tmr = 0
                if key[pg.K_m] ==1:
                    turn = 3
                    tmr = 0

            elif turn == 2 or turn == 3: # プレイヤーの攻撃
                if tmr == 1: set_message("You attack!")
                if 2 <= tmr and tmr <= 4:
                    if turn == 2: screen.blit(imgEffect, [HEIGHT-tmr*(HEIGHT/6), -100+tmr*(HEIGHT/6)])
                    if turn ==3: screen.blit(imgEffect_magic, [WIDTH/MAZE_W, tmr*20])
                if tmr == 5:
                    emy_blink = 5
                    if turn == 2:
                        dmg = random.randint(700,900)
                        set_message(f"{dmg} damage!")
                    if turn ==3:
                        dmg = random.randint(400,1200)
                        set_message(f"{dmg} damage!")
                if tmr == 16:
                    emy_life -= dmg
                    if emy_life < 0:
                        break
                    turn = 4
                    tmr = 0

            elif turn == 4: # 敵のターン、敵の攻撃
                if tmr == 1: set_message("Enemy turn.")
                if tmr == 5:
                    set_message("Enemy attack!")
                    emy_step = 30
                if tmr == 9:
                    set_message(f"{random.randint(900,1100)} damage!")
                    dmg_eff = 5
                    emy_step = 0
                if tmr == 20:
                    turn = 1
                    tmr = 0

        pg.display.update()
        clock.tick(10)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()