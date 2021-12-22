import pygame as pg
pg.init()

BLACK = [0, 0, 0]#검은색
WHITE = [255, 255, 255]#하얀색

size  = [800 ,600]#크기설정
screen = pg.display.set_mode(size)#창출력
pg.display.set_caption("pyGame")#제목

clock = pg.time.Clock()#FPS 변수
FPS = 60#FPS

playing = True
char_speed = 0.5#캐릭터속도

char_x = 0#캐릭터좌표
char_y = 0#캐릭터좌표

char_speed *= FPS#속도고정

while playing:
    
    clock.tick(FPS)#FPS설정
    
    for event in pg.event.get():
        if event.type == pg.QUIT:#닫았는지확인
            playing = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LSHIFT:
                char_speed = char_speed / 2
            elif event.key == pg.K_LCTRL:
                char_speed = char_speed * 2
        if event.type == pg.KEYUP:
            if event.key == pg.K_a:
                if char_x > 0:
                    char_x -= char_speed
            elif event.key == pg.K_d:
                if char_x < 800:
                    char_x += char_speed
            elif event.key == pg.K_w:
                if char_y > 0:
                    char_y -= char_speed
            elif event.key == pg.K_s:
                if char_y < 600:
                    char_y += char_speed
            elif event.key == pg.K_SPACE:
                pass
            elif event.key == pg.K_LSHIFT:
                char_speed = char_speed * 2
            elif event.key == pg.K_LCTRL:
                char_speed = char_speed / 2
    
    
    
    screen.fill(BLACK)#화면초기화
    pg.draw.rect(screen, WHITE , [char_x, char_y, 50, 50],0)#캐릭터출력
    
    pg.display.update()#화면업데이트
    
    
pg.quit()#창닫기


# https://runebook.dev/ko/docs/pygame/ref/key
# https://nightshadow.tistory.com/entry/pygame-%EC%9D%98-%EC%8A%A4%ED%94%84%EB%9D%BC%EC%9D%B4%ED%8A%B8-%EC%B6%A9%EB%8F%8C%EC%B2%B4%ED%81%AC-%EB%B0%A9%EB%B2%95
