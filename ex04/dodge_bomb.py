import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバーに「逃げろ！こうかとん」と表示する
    scrn_sfc = pg.display.set_mode((1600,900)) #1600x900の画面Surfaceを生成する

    bg_sfc = pg.image.load("fig/pg_bg.jpg") #背景となる「pg_bg.jpg」のSurface
    bg_rct = bg_sfc.get_rect() #Rect
    scrn_sfc.blit(bg_sfc, bg_rct) #bilt

    pg.display.update() #biltしてもスクリーンを更新しないと表示されない

    clock = pg.time.Clock() #時間計測用のオブジェクト
    clock.tick(1000) #1000fpsの時を刻む

    while True:
        for event in pg.event.get(): #イベントを繰り返しで処理
            if event.type == pg.QUIT: return #ウィンドウの✖ボタンをクリックしたら


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()