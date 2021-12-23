import pygame
pygame.init()

BLACK = [0, 0, 0]#검은색
WHITE = [255, 255, 255]#하얀색

wheight = 800
height = 600

size  = [wheight ,height]#크기설정
screen = pygame.display.set_mode(size)#창출력
pygame.display.set_caption("pyGame")#제목

clock = pygame.time.Clock()#FPS 변수
FPS = 60#FPS

playing = True
char_speed = 0.1#캐릭터속도

char_x = 0#캐릭터좌표
char_y = 0#캐릭터좌표

char_speed *= FPS#속도고정

#last_char_speed_x = wheight % char_speed
#last_char_speed_y = height % char_speed

while playing:
    
    clock.tick(FPS)#FPS설정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#닫았는지확인
            playing = False
        if event.type == pygame.KEYDOWN:#눌렸는지
            if event.key == pygame.K_LSHIFT:#느리게
                char_speed = char_speed / 2
            elif event.key == pygame.K_LCTRL:#달리기
                char_speed = char_speed * 2
        if event.type == pygame.KEYUP:#올라갔는지
            if event.key == pygame.K_SPACE:
                pass
            elif event.key == pygame.K_LSHIFT:#느리게
                char_speed = char_speed * 2
            elif event.key == pygame.K_LCTRL:#달리기
                char_speed = char_speed / 2
    
    
    keys = pygame.key.get_pressed()#키눌렀는지확인
    
    if keys[pygame.K_a]:#왼
        if char_x > 0:
            char_x -= char_speed
            
    if keys[pygame.K_d]:#오
        if char_x < 800:
            char_x += char_speed
                
    if keys[pygame.K_w]:#위
        if char_y > 0:
            char_y -= char_speed
                
    if keys[pygame.K_s]:#아래
        if char_y < 600:
            char_y += char_speed
                    
    if keys[pygame.K_SPACE]:#공격
        pass
    
    
    
    screen.fill(BLACK)#화면초기화
    pygame.draw.rect(screen, WHITE , [char_x, char_y, 50, 50],0)#캐릭터출력
    
    pygame.display.update()#화면업데이트
    
    
pygame.quit()#창닫기


# https://runebook.dev/ko/docs/pygame/ref/key
# https://nightshadow.tistory.com/entry/pygame-%EC%9D%98-%EC%8A%A4%ED%94%84%EB%9D%BC%EC%9D%B4%ED%8A%B8-%EC%B6%A9%EB%8F%8C%EC%B2%B4%ED%81%AC-%EB%B0%A9%EB%B2%95
#https://codesample-factory.tistory.com/62
#https://blog.dalso.org/language/python/14172
