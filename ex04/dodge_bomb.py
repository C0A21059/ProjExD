import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock() #時間計測用のオブジェクト

    pg.display.set_caption("逃げろ！こうかとん") #タイトルバーに「逃げろ！こうかとん」と表示する
    scrn_sfc = pg.display.set_mode((1600,900)) #1600x900の画面Surfaceを生成する
    scrn_rct = scrn_sfc.get_rect()

    bg_sfc = pg.image.load("fig/pg_bg.jpg") #背景となる「pg_bg.jpg」のSurface
    bg_rct = bg_sfc.get_rect() #Rect

    tori_sfc = pg.image.load("fig/3.png") #こうかとんのSurface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0) #こうかとんの大きさを2倍に
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct) #blit

    #練習5
    bomb_sfc = pg.Surface((20,20)) #正方形の空のSurface
    bomb_sfc.set_colorkey("black") #四隅の黒を透明に
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) #Surface内の色、位置、半径を指定
    bomb_rct = bomb_sfc.get_rect() #Rect
    bomb_rct.centerx = random.randint(0, scrn_rct.centerx)
    bomb_rct.centery = random.randint(0, scrn_rct.centery)
    scrn_sfc.blit(bomb_sfc, bomb_rct) #blit

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #blit
        for event in pg.event.get(): #イベントを繰り返しで処理
            if event.type == pg.QUIT: return #ウィンドウの✖ボタンをクリックしたら

        key_dct = pg.key.get_pressed() #辞書型　キーの判定に利用
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -=1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx +=1
        scrn_sfc.blit(tori_sfc, tori_rct) #blit
        scrn_sfc.blit(bomb_sfc, bomb_rct) #blit
        pg.display.update() #blitしてもスクリーンを更新しないと表示されない
        clock.tick(1000) #1000fpsの時を刻む

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()