import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)  #8
    kk_img = pg.image.load("fig/3.png") #１
    kk_img = pg.transform.flip(kk_img, True, False)  #２
    kk_rct = kk_img.get_rect()   #10↓
    kk_rct.center = 300, 200
    
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()

        
        if key_lst[pg.K_UP]:
         #   kk_rct.move_ip((0, -1))
            a = -1
            b = -1
            
        elif key_lst[pg.K_DOWN]:
         #   kk_rct.move_ip((0, 1))
            a = -1
            b = 1
            
        elif key_lst[pg.K_RIGHT]:
         #   kk_rct.move_ip((2, 0))
            a = 2
            b = 0
            
        elif key_lst[pg.K_LEFT]:
         #   kk_rct.move_ip((-2, 0))
            a = -2
            b = 0
            
        
        elif not key_lst[pg.K_RIGHT] :
            a = -1
            b = 0
        
        kk_rct.move_ip((a, b))   #演習１
            

        x = tmr%3200   #6
        screen.blit(bg_img, [-x, 0])  #6
        screen.blit(bg_img2, [-x+1600, 0])  #7
        screen.blit(bg_img, [-x+3200, 0])  #9
        screen.blit(kk_img, kk_rct)

        pg.display.update()
        tmr += 1        
        clock.tick(200)  #5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()