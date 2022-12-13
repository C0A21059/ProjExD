import pygame as pg
import sys
import random
import copy

def check_bound(obj_rct, scr_rct):
    # 第一引数：こうかとんrectまたは爆弾rect
    # 第二引数：スクリーンrect
    # 範囲内なら+1, 範囲外なら-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or obj_rct.right > scr_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or obj_rct.bottom > scr_rct.bottom:
        tate = -1
    return yoko, tate

def bomb_copy(bomb_rct,bomb_lis, scrn_rct):
    #左上か左下にランダムに生成
    #deepcopyで複製し、別オブジェクトとしてcenterxとcenteryの値を変更可能に
    vx, vy = random.choice([-1, 1]), random.choice([-1, 1]) #どの方向に進むかはランダム
    new_bomb_rct = copy.deepcopy(bomb_rct) #Rectをdeepcopyで複製。
    new_bomb_rct.centerx = random.choice([random.randint(scrn_rct.centerx - 200, scrn_rct.centerx),
                                        random.randint(0, 200)]) #左上か右上か選ぶ
    new_bomb_rct.centery = random.randint(0, 200) #高さは固定
    bomb_lis.append([new_bomb_rct, vx, vy])

def main():
    clock = pg.time.Clock() #時間計測用のオブジェクト

    pg.display.set_caption("逃げろ！こうかとん") #タイトルバーに「逃げろ！こうかとん」と表示する
    scrn_sfc = pg.display.set_mode((1600, 900)) #1600x900の画面Surfaceを生成する
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

    #タイマー用のフォント設定
    font = pg.font.Font(None, 80)
    #GameOver用のフォント設定
    font_go = pg.font.Font(None, 200)

    vx, vy = +1, +1 #爆弾の移動方向
    bomb_lis = [[bomb_rct, vx, vy]]
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #blit
        for event in pg.event.get(): #イベントを繰り返しで処理
            if event.type == pg.QUIT: return #ウィンドウの✖ボタンをクリックしたら

        key_dct = pg.key.get_pressed() #辞書型　キーの判定に利用

        #移動方向の判定をキーに移動量を値に設定した辞書
        data = {key_dct[pg.K_UP]:    [ 0, -1],
                key_dct[pg.K_DOWN]:  [ 0, +1],
                key_dct[pg.K_LEFT]:  [-1,  0],
                key_dct[pg.K_RIGHT]: [+1,  0]}
        for k, v in data.items():
            if k:
                tori_rct.centerx += v[0]
                tori_rct.centery += v[1]

        #check_boundで用いる、移動方向の判定をキーに移動量を値に設定した辞書
        data_bound = {key_dct[pg.K_UP]:  [ 0, +1],
                    key_dct[pg.K_DOWN]:  [ 0, -1],
                    key_dct[pg.K_LEFT]:  [+1,  0],
                    key_dct[pg.K_RIGHT]: [-1,  0]}

        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            for k, v in data_bound.items():
                if k:
                    tori_rct.centerx += v[0]
                    tori_rct.centery += v[1]

        scrn_sfc.blit(tori_sfc, tori_rct) #blit
        for bomb_r in bomb_lis:
            yoko, tate = check_bound(bomb_r[0], scrn_rct) #壁に当たる爆弾ごとの判定
            bomb_r[1] *= yoko
            bomb_r[2] *= tate
            bomb_r[0].move_ip(bomb_r[1], bomb_r[2]) #爆弾をvx, vy分移動
            scrn_sfc.blit(bomb_sfc, bomb_r[0]) #blit
        tmr = pg.time.get_ticks()/1000 #描画するタイムを取得
        txt = font.render("{:.1f}".format(tmr), True, "black") #黒色でタイムを書いたSurfaceを生成する
        scrn_sfc.blit(txt, (0, 0)) #blit

        for bomb_r in bomb_lis:
            if tori_rct.colliderect(bomb_r[0]):
                txt_go = font_go.render("GameOver", True, "black") #黒色でGameOverを書いたSurfaceを生成する
                scrn_sfc.blit(txt_go, (400, 300)) #blit
                pg.display.update()
                pg.time.delay(2000) #GameOverが描画されてから2秒間止める
                return
        pg.display.update() #blitしてもスクリーンを更新しないと表示されない

        #4990msから5000msに処理が追いつくだけ爆弾を追加
        if pg.time.get_ticks()%5000 >= 4990:
            bomb_copy(bomb_rct,bomb_lis, scrn_rct) #bomb_rctを複製
        clock.tick(1000) #1000fpsの時を刻む

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()