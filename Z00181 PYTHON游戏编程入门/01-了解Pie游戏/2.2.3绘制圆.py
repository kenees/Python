import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('Drawing Circles')  #设置当前窗口标题

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            exit()

    screen.fill((0,0,0))  #背景填充色

    #draw a circle
    color = 0,0,50    #绘制颜色
    position = 300,250  #位置
    radius = 70  #半径
    width = 50  #线宽
    pygame.draw.circle(screen,color,position,radius,width)
    pygame.display.update()
