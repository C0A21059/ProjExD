import random
import os
import copy
import sys
import time

import pygame as pg


main_dir = os.path.split(os.path.abspath(__file__))[0]

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
        self.rct.centerx = random.choice([
                                        random.randint(0, 200),
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

    #こうかとんの当たり判定
    def kkt_check(self, kkt:Bird, scr:Screen):
        yoko, tate = check_bound(self.rct, kkt.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Time:
    def __init__(self, size):
        #タイマー用のフォント設定
        self.font = pg.font.Font(None, size)
        tmr = pg.time.get_ticks()/1000 #描画するタイムを取得
        self.txt = self.font.render("{:.1f}".format(tmr), True, "black") #黒色でタイムを書いたSurfaceを生成する

    def blit(self,scr:Screen):
        scr.sfc.blit(self.txt, (0,0))

    def update(self,scr:Screen):
        tmr = pg.time.get_ticks()/1000 #描画するタイムを取得
        self.txt = self.font.render("{:.1f}".format(tmr), True, "black") #黒色でタイムを書いたSurfaceを生成する
        self.blit(scr)

class GameOver:
    def __init__(self,xy):
        #GameOver用のフォント設定
        self.font = pg.font.Font(None, 200)
        self.xy = xy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.txt, (self.xy))

    def render(self,scr:Screen,text):
        self.txt = self.font.render(text, True, "black") #黒色でGameOverを書いたSurfaceを生成する
        self.blit(scr)
        pg.display.update()
        pg.time.delay(2000) #GameOverが描画されてから2秒間止める

class Life:
    def __init__(self, life):
        #残機用のフォント設定
        self.font = pg.font.Font(None, 80)
        self.life = life
        self.txt = self.font.render(str(self.life), True, "black") #黒色でタイムを書いたSurfaceを生成する

    def blit(self,scr:Screen):
        self.txt = self.font.render(str(self.life), True, "black") #黒色でタイムを書いたSurfaceを生成する
        scr.sfc.blit(self.txt, (scr.rct.width-80,0))

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

def load_sound(file):
    """because pygame can be be compiled without mixer."""
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None

def main():
    clock =pg.time.Clock()
    #Screenクラスでウィンドウを描画
    scr = Screen("負けるな！こうかとん", (1600,900), "fig/pg_bg.jpg")

    # Birdクラスでこうかとんを作成
    kkt = Bird("fig/6.png", 2.0, (900,400))
    kkt.blit(scr) #blit

    # 爆弾の色は三種類からランダムに設定
    bomb_color = [(255,0,0), (0,255,0), (0,0,255)]
    bomb = Bomb(random.choice(bomb_color), 10, scr)
    bomb.blit(scr) #blit

    #経過時間ごとに追加される爆弾のリスト
    bomb_lis = [bomb]

    time = Time(80)
    time.blit(scr)

    #sを押した際にゲームスタートするように判定を設定
    game_flag = False
    #爆弾にあたった際の音の設定
    boom_sound = load_sound("boom.wav")

    #こうかとんの当たっても大丈夫な回数
    kkt_life = 3

    #Lifeクラスでこうかとんの残機用のフォントを設定
    life_font = Life(kkt_life)

    while True:
        scr.blit() #blit

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            #sキーを押したらゲームスタート
            key_dct = pg.key.get_pressed()
            if key_dct[pg.K_s]: game_flag = True

            #スペースキーを押したとき爆弾が10個以上であれば1個から4個爆弾を削除
            if key_dct[pg.K_SPACE]:
                if len(bomb_lis) >10:
                    del_bomb = random.randint(6, 9)
                    del bomb_lis[del_bomb:]

        if game_flag:
            kkt.update(scr)
            time.update(scr)
            life_font.blit(scr)
            for bomb in bomb_lis:
                bomb.update(scr)
                #こうかとんと爆弾が当たった際に残機を減らすか、GameOverか判定
                if kkt.rct.colliderect(bomb.rct):
                    bomb.kkt_check(kkt,scr)
                    kkt_life -= 1
                    life_font.life = copy.deepcopy(kkt_life)
                    if kkt_life < 1:
                        if pg.mixer:
                            boom_sound.play()
                        GameOver((400,300)).render(scr,"GameOver")
                        return
            #4900msから5000msの間に処理できるだけ爆弾を追加
            if pg.time.get_ticks()%5000 >= 4990:
                bomb_lis.append(Bomb(random.choice(bomb_color), 10,  scr))

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()