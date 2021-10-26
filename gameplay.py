import pygame
import random
from pygame.locals import *

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
charecterpos = [10, 10]
apples = [[50, 50]]
applecollecters = [[]]
appletimer = 30
appletimer1 = 0
totalapple = 0
villons = [[50, 50]]
villoncollecters = [[]]
villontimer = 1
villontimer1 = 0
game_over = False

backGround = pygame.image.load("src/background.png")
backgroundimg = pygame.transform.scale(backGround, (640, 480))
charecterimg = pygame.image.load("src/caa.png")
appleimg = pygame.image.load("src/appleee.png")
gameoverimg = pygame.image.load("src/end.png")
villonimg = pygame.image.load("src/vii.png")

running = 1
exitcode = 0
while running:
    appletimer -= 1
    villontimer -= 1
    screen.fill(0)
    screen.blit(backgroundimg, (0, 0))
    screen.blit(charecterimg, charecterpos)
    if appletimer == 0:
        apples.append([640, random.randint(20, 470)])
        appletimer = 100 - (appletimer1*2)
        if appletimer1 >= 35:
            appletimer1 = 35
        else:
            appletimer1 += 5
    index = 0
    for apple in apples:
        if apple[0] <- 64:
            apples.pop(index)
        apple[0] -= 1
        AppleRect = pygame.Rect(appleimg.get_rect())
        AppleRect.top = apple[1]
        AppleRect.left = apple[0]

        index1 = 0
        for applecollecter in applecollecters:
            charecterrect = pygame.Rect(charecterimg.get_rect())
            charecterrect.top = charecterpos[1]
            charecterrect.left = charecterpos[0]
            if charecterrect.colliderect(AppleRect):
                totalapple += 1
                apples.pop(index)
            index1 += 1

        index += 1
    for apple in apples:
        screen.blit(appleimg, apple)

    if villontimer == 0:
        villons.append([640, random.randint(20, 470)])
        villontimer = 200 - (villontimer1 % 10)
        if villontimer1 >= 10:
            villontimer1 = 10
        else:
            villontimer1 += 5

    index = 0
    for villon in villons:
        if villon[0] <- 64:
            villons.pop(index)
        villon[0] -= 1
        VillonRect = pygame.Rect(villonimg.get_rect())
        VillonRect.top = villon[1]
        VillonRect.left = villon[0]

        index1 = 0
        for villoncollecter in villoncollecters:
            charecterrect = pygame.Rect(charecterimg.get_rect())
            charecterrect.top = charecterpos[1]
            charecterrect.left = charecterpos[0]
            if charecterrect.colliderect(VillonRect):
                totalapple -= 1
                villons.pop(index)
            index1 += 1
        index += 1
    for villon in villons:
        screen.blit(villonimg, villon)

    font = pygame.font.SysFont('malgungothic', 18)
    survivedtext = font.render('%d'%totalapple+"점", True, (0, 0, 0))
    textRect = survivedtext.get_rect()
    textRect.topright = [635, 5]
    screen.blit(survivedtext, textRect)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0] = False
            elif event.key == K_LEFT:
                keys[1] = False
            elif event.key == K_DOWN:
                keys[2] = False
            elif event.key == K_RIGHT:
                keys[3] = False
    if keys[0]:
        charecterpos[1] -= 1
    if keys[1]:
        charecterpos[0] -= 1
    if keys[2]:
        charecterpos[1] += 1
    if keys[3]:
        charecterpos[0] += 1

    if pygame.time.get_ticks() >= 13000:
        running = 0
        exitcode = 1

    if charecterpos[0] >= 50:
        charecterpos[0] = 50

    if charecterpos[0] <= 0:
        charecterpos[0] = 0

    if charecterpos[1] <= 0:
        charecterpos[1] = 0

    if charecterpos[1] >= 450:
        charecterpos[1] = 450

if exitcode == 1:
    pygame.font.init()
    font = pygame.font.SysFont('malgungothic', 50)
    survivedtext2 = font.render('%d'%totalapple+"점", True, (0, 0, 0))
    textRect = survivedtext2.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery - 40
    screen.blit(gameoverimg, (0, 0))
    screen.blit(survivedtext2, textRect)

    if totalapple > 50:
        survivedtext3 = font.render("이게 가능한건가..?", True, (0, 0, 0))
        texRect = survivedtext3.get_rect()
        texRect.centerx = screen.get_rect().centerx
        texRect.centery = screen.get_rect().centery + 50
        screen.blit(survivedtext3, texRect)
    if totalapple < 20:
        survivedtext4 = font.render("뭐하세요?", True, (0, 0, 0))
        texttRect = survivedtext4.get_rect()
        texttRect.centerx = screen.get_rect().centerx
        texttRect.centery = screen.get_rect().centery + 50
        screen.blit(survivedtext4, texttRect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()