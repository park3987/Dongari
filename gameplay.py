import pygame
import random

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 1250  # 가로 크기
screen_height = 755  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
apple_width = 30
apple_height = 30
# 점수 설정
score = 0

pygame.display.set_caption("Game")  # 게임 이름

# 배경 이미지 불러오기

background = pygame.image.load("C:/Users/bluew/PycharmProjects/pythonProject2/src/background.png")

apple = pygame.image.load("C:/Users/bluew/PycharmProjects/pythonProject2/src/appleee.png")
apple_x_pos = random.randint(0, 1250)
apple_y_pos = 0

villon = pygame.image.load("C:/Users/bluew/PycharmProjects/pythonProject2/src/vii.png")
villon_size = villon.get_rect().size
villon_width = villon_size[0]
villon_height = villon_size[1]
villon_x_pos = random.randint(0, 1250)
villon_y_pos = 0

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/bluew/PycharmProjects/pythonProject2/src/caa.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

# 이동할 좌표
to_x = 0
to_y = 0

vil_x = 0
vil_y = 0

app_x = 0
app_y = 0

running = True
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= 0.5  # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += 0.5
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= 0.5
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += 0.5

        vil_y += random.choice([0.01, 0.009, 0.025786778786867675657689897846778736457, 0.03, 0.03232323])
        app_y += random.choice([0.01, 0.009, 0.025786778786867675657689897846778736457, 0.03, 0.03232323])

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    apple_x_pos += app_x
    apple_y_pos += app_y

    villon_y_pos += vil_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 700:
        character_y_pos = 700
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    screen.blit(apple, (apple_x_pos, apple_y_pos))

    screen.blit(villon, (villon_x_pos, villon_y_pos))

    pygame.display.update()

# pygame 종료
pygame.quit()
