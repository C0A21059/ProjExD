import pygame as pg
import random
import sys


class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) #"負けるな！こうかとん" タイトルバーに「逃げろ！こうかとん」と表示する
        self.sfc = pg.display.set_mode(wh) #(1600, 900)1600x900の画面Surfaceを生成する
        self.rct = self.sfc.get_rect()
        self.pgbg_sfc = pg.image.load(img_path) #fig/pg_bg.jpg 背景となる「pg_bg.jpg」のSurface
        self.pgbg_rct = self.pgbg_sfc.get_rect() #Rect

    #スクリーン用のSurfaceのblitメソッドを呼び出し，背景画像をblitする
    def blit(self):
        self.sfc.blit(self.pgbg_sfc, self.pgbg_rct) #blit

class Bird():
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }
    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path) #fig/6.png こうかとんのSurface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)#こうかとんの傾き0度、大きさを2倍に
        self.rct = self.sfc.get_rect() #Rect
        self.rct.center = xy #900, 400

    #scrにself.rctに従って，self_sfcを貼り付ける
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    #こうかとんの座標を変更
    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)

class Bomb():
    def __init__(self, color, rad, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) #(20, 20) 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0)) #四隅の黒を透明に
        pg.draw.circle(self.sfc, color, (rad, rad), rad) #Surface内の色、位置、半径を指定
        self.rct = self.sfc.get_rect() #Rect
        self.rct.centerx = random.choice([random.randint(0, 200),
                                        random.randint(scr.rct.width-200, scr.rct.width)]) #左右にランダムに設定
        self.rct.centery = random.randint(0, 200) #上部200までに設定
        self.vx, self.vy = random.choice([-1,+1]), random.choice([-1,+1]) #方向をランダムに設定

    # scrにself.rctに従って，self_sfcを貼り付ける
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    #爆弾の座標を変更
    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        scr.sfc.blit(self.sfc, self.rct)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

class Time:
    def __init__(self, size):
        #タイマー用のフォント設定
        self.font = pg.font.Font(None, size)
        tmr = pg.time.get_ticks()/1000 #描画するタイムを取得
        self.txt = self.font.render("{:.1f}".format(tmr), True, "black") #黒色でタイムを書いたSurfaceを生成する

    def bilt(self,scr:Screen):
        scr.sfc.blit(self.txt, (0,0))

    def update(self,scr:Screen):
        tmr = pg.time.get_ticks()/1000 #描画するタイムを取得
        self.txt = self.font.render("{:.1f}".format(tmr), True, "black") #黒色でタイムを書いたSurfaceを生成する
        self.bilt(scr)

class GameOver:
    def __init__(self):
        #GameOver用のフォント設定
        self.font = pg.font.Font(None, 200)

    def blit(self,scr:Screen):
        scr.sfc.blit(self.txt, (400,300))

    def render(self,scr:Screen):
        self.txt = self.font.render("GameOver", True, "black") #黒色でGameOverを書いたSurfaceを生成する
        self.blit(scr)
        pg.display.update()
        pg.time.delay(2000) #GameOverが描画されてから2秒間止める


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    # 練習１
    scr = Screen("にげろ！こうかとん", (1600,900), "fig/pg_bg.jpg")

    # 練習2
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    kkt.blit(scr) #blit

    # 練習3
    bomb_color = [(255,0,0),(0,255,0),(0,0,255)]
    bomb = Bomb(random.choice(bomb_color), 10, scr)
    bomb.blit(scr) #blit

    bomb_lis = [bomb]

    time = Time(80)
    time.bilt(scr)

    game_flag = False

    # 練習２
    while True:
        scr.blit() #blit

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            key_dct = pg.key.get_pressed()
            if key_dct[pg.K_s]: game_flag = True

        if game_flag:
            kkt.update(scr)
            for bomb in bomb_lis:
                bomb.update(scr)
                if kkt.rct.colliderect(bomb.rct):
                    GameOver().render(scr)
                    return
            #4900msから5000msの間に処理できるだけ追加
            if pg.time.get_ticks()%5000 >= 4990:
                bomb_lis.append(Bomb(random.choice(bomb_color), 10,  scr))


            time.update(scr)
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()