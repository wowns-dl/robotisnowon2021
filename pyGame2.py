import pygame
      
pygame.init()

BLACK = [0, 0, 0]#검은색
WHITE = [255, 255, 255]#하얀색
YELLOW = [255, 255, 0]#노란색

count = 0

screen_whight = 800
screen_height = 600

size  = [screen_whight ,screen_height]#크기설정
screen = pygame.display.set_mode(size)#창출력
pygame.display.set_caption("pyGame")#제목

clock = pygame.time.Clock()#FPS 변수
FPS = 60#FPS

playing = True

char_speed = 0.1#캐릭터속도

char_whight = 50
char_height = 50

char_x = 0#캐릭터x
char_y = 0#캐릭터y


shot = 'num'

bullet_speed = 0.3

bullet_whight = 20
bullet_height = 20
bullet_half = 10

bullet_x = 0#총알x
bullet_y = 0#총알y

shooting = False


bullet_speed *= FPS#총알속도고정
char_speed *= FPS#캐릭터속도고정


nemo = pygame.image.load("C:/Users/emeni/OneDrive/바탕 화면/nemo.png").convert_alpha()#이미지불러오기
nemo = pygame.transform.scale(nemo, (char_whight, char_height))#이미지크기설정

bullet = pygame.image.load("C:/Users/emeni/OneDrive/바탕 화면/bullet.png").convert_alpha()#이미지불러오기
bullet = pygame.transform.scale(bullet, (bullet_whight, bullet_height))#이미지크기설정

background = pygame.image.load("C:/Users/emeni/OneDrive/사진/Saved Pictures/배경.jpg")#이미지불러오기
background = pygame.transform.scale(background, (screen_whight, screen_height)).convert_alpha()#이미지크기설정

player = 'num'
player = 'sniper'
while playing:
    
    clock.tick(FPS)#FPS설정
    
    if player == 'sniper':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#닫았는지확인
                playing = False
            if event.type == pygame.KEYDOWN:#눌렸는지
                if event.key == pygame.K_LSHIFT:#느리게
                    char_speed = char_speed / 2
                #elif event.key == pygame.K_LCTRL:#달리기
                    #char_speed = char_speed * 2
            if event.type == pygame.KEYUP:#올라갔는지
                if event.key == pygame.K_LSHIFT:#느리게
                    char_speed = char_speed * 2
                #elif event.key == pygame.K_LCTRL:#달리기
                    #char_speed = char_speed / 2
        
        
        keys = pygame.key.get_pressed()#키눌렀는지확인
        if keys[pygame.K_a]:#왼
            if char_x > 0:
                char_x -= char_speed
        
        if keys[pygame.K_d]:#오
            if char_x < screen_whight - char_whight:
                char_x += char_speed
        
        if keys[pygame.K_w]:#위
            if char_y > 0:
                char_y -= char_speed
        
        if keys[pygame.K_s]:#아래
            if char_y < screen_height - char_height:
                char_y += char_speed
        
        if count == 0:
            if keys[pygame.K_UP]:#공격
                shot = 'Up'
                bullet_x = char_x
                bullet_y = char_y
                shooting = True
        
        if bullet_y < 0 or bullet_y > screen_height or bullet_x < 0 or bullet_x > screen_whight:
            shooting = False
        
        screen.blit(background, (0, 0))#배경출력
        
        screen.blit(nemo, (char_x, char_y))#캐릭터출력
        if shot == 'Up':
            bullet_y -= bullet_speed
            count += 1
        
        if shooting == True:
            #pygame.draw.circle(screen, YELLOW,[bullet_x, bullet_y],10)
            screen.blit(bullet, (bullet_x, bullet_y))#총알출력

        if count == 42:#0.7초
            count = 0
        
        pygame.display.update()#화면업데이트
    
    
pygame.quit()#창닫기


# https://runebook.dev/ko/docs/pygame/ref/key
# https://nightshadow.tistory.com/entry/pygame-%EC%9D%98-%EC%8A%A4%ED%94%84%EB%9D%BC%EC%9D%B4%ED%8A%B8-%EC%B6%A9%EB%8F%8C%EC%B2%B4%ED%81%AC-%EB%B0%A9%EB%B2%95
# https://codesample-factory.tistory.com/62

# https://kkamikoon.tistory.com/129

# https://volfeed.blogspot.com/2020/12/pygame-cannon-4.html      스프라이트 클래스
# 


#if(pygame.sprite.collide_mask(nemo,bullet)):
#        ddd
