import pygame as pg
import sys

def main():
    pg.display.set_caption("初めてのPygame")
    scrn_sfc = pg.display.set_mode((800,600))

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 400, 300
    scrn_sfc.blit(tori_sfc, tori_rct)

    draw_sfc = pg.Surface((100,100))
    pg.draw.circle(draw_sfc, (255, 0, 0), (50,50), 50)
    pg.draw.circle(draw_sfc, (191, 0, 0), (50,50), 40)
    pg.draw.circle(draw_sfc, (127, 0, 0), (50,50), 30)
    pg.draw.circle(draw_sfc, ( 63, 0, 0), (50,50), 20)
    pg.draw.circle(draw_sfc, ( 0, 0, 0), (50,50), 10)
    scrn_sfc.blit(draw_sfc, (100,100))
    scrn_sfc.blit(draw_sfc, (200,200))
    scrn_sfc.blit(draw_sfc, (300,300))

    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()