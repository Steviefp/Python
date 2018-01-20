import pygame
import random


pygame.init()
gameState=True
score=0
size=(800,600)
playerSpeed=0.25
screen=pygame.display.set_mode(size)
boxCord=[400-30,300-30]
appleCord=[random.randrange(100,600),random.randrange(100,400)]


while gameState:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: gameState=False

    if appleCord[0] <= boxCord[0]+30 <=appleCord[0]+30 and appleCord[1] <= boxCord[1]+30 <=appleCord[1]+30 or appleCord[0] <= boxCord[0] <=appleCord[0]+30 and appleCord[1] <= boxCord[1] <=appleCord[1]+30:
        score+=1
        appleCord = [random.randrange(100, 600), random.randrange(100, 400)]
        print(score)

    playerControl = pygame.key.get_pressed()

    if playerControl[pygame.K_w]:
        if boxCord[1] >=0:
            boxCord[1]-=playerSpeed
    if playerControl[pygame.K_s]:
        if boxCord[1]<=size[1]-30:
            boxCord[1]+=playerSpeed
    if playerControl[pygame.K_a]:
        if boxCord[0]>=0:
            boxCord[0]-=playerSpeed
    if playerControl[pygame.K_d]:
        if boxCord[0]<=size[0]-30:
            boxCord[0]+=playerSpeed


    screen.fill((0,0,0))#this erases previous box location
    pygame.draw.rect(screen, (255, 255, 255), [boxCord[0], boxCord[1], 30, 30])
    pygame.draw.rect(screen, (255, 0, 0), [appleCord[0], appleCord[1], 30, 30])

    pygame.display.update()