import pygame as pg
import sys

def main():
    clock = pg.time.Clock() #時間計測用のオブジェクト

    pg.display.set_caption("逃げろ！こうかとん") #タイトルバーに「逃げろ！こうかとん」と表示する
    scrn_sfc = pg.display.set_mode((1600,900)) #1600x900の画面Surfaceを生成する

    bg_sfc = pg.image.load("fig/pg_bg.jpg") #背景となる「pg_bg.jpg」のSurface
    bg_rct = bg_sfc.get_rect() #Rect
    scrn_sfc.blit(bg_sfc, bg_rct) #blit

    tori_sfc = pg.image.load("fig/3.png") #こうかとんのSurface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0) #こうかとんの大きさを2倍に
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900, 300
    scrn_sfc.blit(tori_sfc, tori_rct) #blit

    pg.display.update() #blitしてもスクリーンを更新しないと表示されない
    clock.tick(1000) #1000fpsの時を刻む

    while True:
        for event in pg.event.get(): #イベントを繰り返しで処理
            if event.type == pg.QUIT: return #ウィンドウの✖ボタンをクリックしたら


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()