#탱크게임뿌슝빠슝
#스페이스 조준
import pygame
pygame.init()

BLACK = [0, 0, 0]#검은색
WHITE = [255, 255, 255]#하얀색
YELLOW = [255, 255, 0]#노란색

screen_whight = 1920
screen_height = 1080

size  = [screen_whight ,screen_height]#크기설정
screen = pygame.display.set_mode(size)#창출력
pygame.display.set_caption("Tank")#제목

clock = pygame.time.Clock()#FPS 변수
FPS = 60#FPS

tank1_whight = 50
tank1_height = 30

bullet1_whight = 20
bullet1_height = 20

tank1 = pygame.image.load("C:/Users/emeni/OneDrive/바탕 화면/nemo.png").convert_alpha()#이미지불러오기
tank1 = pygame.transform.scale(tank1, (tank1_whight, tank1_height))#이미지크기설정

bullet1 = pygame.image.load("C:/Users/emeni/OneDrive/바탕 화면/bullet.png").convert_alpha()#이미지불러오기
bullet1 = pygame.transform.scale(bullet1, (bullet1_whight, bullet1_height))#이미지크기설정

bullet1_aim = pygame.image.load("C:/Users/emeni/OneDrive/바탕 화면/aim.png").convert_alpha()#이미지불러오기
bullet1_aim = pygame.transform.scale(bullet1, (bullet1_whight, bullet1_height))#이미지크기설정


playing = True

tank1_x = 0
tank1_y = 500

bullet1_x = tank1_x
bullet1_y = tank1_y

tank1_speed = 0.05

bullet1_power_x = 0.15
bullet1_power_y = 0.15

aim = 0.001

bullet1_aim_power_x = 0.15
bullet1_aim_power_y = 0.15

bullet1_aim_x = tank1_x
bullet1_aim_y = tank1_y


bullet1_power_x *= FPS#총알속도고정
bullet1_power_y *= FPS#총알속도고정
tank1_speed *= FPS#캐릭터속도고정
aim *= FPS#조준속도고정

fry = False


gravity = 0.0015

gravity *=FPS

while playing:
    
    clock.tick(FPS)#FPS설정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#닫았는지확인
                playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:#마우스클릭
            mouse_x = pygame.mouse.get_pressed()
            fry = True
    
    
    
    keys = pygame.key.get_pressed()#키눌렀는지확인
    if keys[pygame.K_a]:#왼
        if tank1_x > 0:
            tank1_x -= tank1_speed

    if keys[pygame.K_d]:#오
        if tank1_x < screen_whight - tank1_whight:
            tank1_x += tank1_speed
        
    if keys[pygame.K_w]:#위
        if tank1_y > 0:
            tank1_y -= tank1_speed
        
    if keys[pygame.K_s]:#아래
        if tank1_y < screen_height - tank1_height:
            tank1_y += tank1_speed
        
    
    if keys[pygame.K_LEFT]:
        bullet1_power_y += aim
        bullet1_power_x -= aim
    if keys[pygame.K_RIGHT]:
        bullet1_power_y -= aim
        bullet1_power_x += aim
    
    if keys[pygame.K_SPACE]:
        fry = True
    
    screen.fill(BLACK)
    
    screen.blit(tank1, (tank1_x, tank1_y))#캐릭터출력
    if fry == True:
        bullet1_power_y -= gravity
        bullet1_x += bullet1_power_x
        bullet1_y -= bullet1_power_y
        screen.blit(bullet1, (bullet1_x, bullet1_y))#총알출력
    elif fry == False:
        bullet1_aim_x = tank1_x
        bullet1_aim_y = tank1_y
        bullet1_aim_power_y = bullet1_power_y
        for i in range(0,30):
            bullet1_aim_power_y -= gravity
            bullet1_aim_x += bullet1_aim_power_x
            bullet1_aim_y -= bullet1_aim_power_y
            screen.blit(bullet1_aim, (bullet1_aim_x, bullet1_aim_y))
            
    pygame.display.update()#화면업데이트

pygame.quit()#창닫기

#bullet power 초기화




#탱크게임뿌슝빠슝
import pygame
pygame.init()

BLACK = [0, 0, 0]#검은색
WHITE = [255, 255, 255]#하얀색
YELLOW = [255, 255, 0]#노란색

screen_whight = 1920
screen_height = 1080

size  = [screen_whight ,screen_height]#크기설정
screen = pygame.display.set_mode(size)#창출력
pygame.display.set_caption("Tank")#제목

clock = pygame.time.Clock()#FPS 변수
FPS = 60#FPS

tank1_whight = 50
tank1_height = 30

bullet1_whight = 20
bullet1_height = 20

tank1 = pygame.image.load("C:/Users/emeni/OneDrive/바탕 화면/nemo.png").convert_alpha()#이미지불러오기
tank1 = pygame.transform.scale(tank1, (tank1_whight, tank1_height))#이미지크기설정

bullet1 = pygame.image.load("C:/Users/emeni/OneDrive/바탕 화면/bullet.png").convert_alpha()#이미지불러오기
bullet1 = pygame.transform.scale(bullet1, (bullet1_whight, bullet1_height))#이미지크기설정


playing = True

tank1_x = 0
tank1_y = 500

bullet1_x = 0
bullet1_y = 500

tank1_speed = 0.05

bullet1_power_x = 0.15
bullet1_power_y = 0.15

aim = 0.001

bullet1_power_x *= FPS#총알속도고정
bullet1_power_y *= FPS#총알속도고정
tank1_speed *= FPS#캐릭터속도고정
aim *= FPS#조준속도고정

fry = False


gravity = 0.0015

gravity *=FPS

while playing:
    
    clock.tick(FPS)#FPS설정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#닫았는지확인
                playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:#마우스클릭
            mouse_x = pygame.mouse.get_pressed()
            fry = True
    
    
    
    keys = pygame.key.get_pressed()#키눌렀는지확인
    if keys[pygame.K_a]:#왼
        if tank1_x > 0:
            tank1_x -= tank1_speed

    if keys[pygame.K_d]:#오
        if tank1_x < screen_whight - tank1_whight:
            tank1_x += tank1_speed
        
    if keys[pygame.K_w]:#위
        if tank1_y > 0:
            tank1_y -= tank1_speed
        
    if keys[pygame.K_s]:#아래
        if tank1_y < screen_height - tank1_height:
            tank1_y += tank1_speed
        
    if fry == False:
        if keys[pygame.K_LEFT]:
            bullet1_power_y += aim
            bullet1_power_x -= aim
        if keys[pygame.K_RIGHT]:
            bullet1_power_y -= aim
            bullet1_power_x += aim
    
    if fry == True:
        bullet1_power_y -= gravity
        bullet1_x += bullet1_power_x
        bullet1_y -= bullet1_power_y
    
    screen.fill(BLACK)
    
    screen.blit(tank1, (tank1_x, tank1_y))#캐릭터출력
    if fry == True:
        screen.blit(bullet1, (bullet1_x, bullet1_y))#총알출력
    
    pygame.display.update()#화면업데이트

pygame.quit()#창닫기
