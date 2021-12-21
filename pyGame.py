import pygame as pg
pg.init()

BLACK = [0 , 0 , 0]#검은색
WHITE = [255 , 255 , 255]#하얀색

size  = [400,300]#크기설정
screen = pg.display.set_mode(size)
pg.display.set_caption("Game Title")#제목

clock = pg.time.Clock()#FPS 변수

playing = True
char_speed = 50#캐릭터속도

x = 0#좌표
y = 0#좌표

while playing:
    FPS = clock.tick(60)#FPS설정
    for event in pg.event.get():
        if event.type == pg.QUIT:#닫았는지확인
            playing = False
        if event.type == pg.KEYDOWN:#키눌렀을때
            if event.key == pg.K_LEFT:
                x -= char_speed
            elif event.key == pg.K_RIGHT:
                x += char_speed
            elif event.key == pg.K_UP:
                y -= char_speed
            elif event.key == pg.K_DOWN:
                y += char_speed
            
    
    
    screen.fill(BLACK)
    pg.draw.rect(screen, WHITE , [x,y,50,50],0)#캐릭터출력
    
    
    
    
    pg.display.update()
pg.quit()
