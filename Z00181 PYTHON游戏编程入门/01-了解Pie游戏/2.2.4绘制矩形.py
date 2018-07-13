import pygame
from pygame.locals import *

pygame.init()
sceen = pygame.display.set_mode((200,300))
pygame.display.set_caption('Drawing Rectangles')  #设置标题

pos_x = 150
pos_y = 150
ver_x = 2
ver_y = 1
index = 0
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            exit()
    index +=1
    if index%5550==0:
        sceen.fill((0,0,0))
        #move the rectang
        pos_x += ver_x
        pos_y += ver_y

        #keep the rectang on the screen
        if pos_x >=200 or pos_x<=0:
            ver_x = -ver_x
        if pos_y >=300 or pos_y<=0:
            ver_y = -ver_y

        #draw the rectang
        color = 255,255,0
        width = 0
        pos = pos_x,pos_y,100,100
        pygame.draw.rect(sceen,color,pos,width)
        pygame.display.update()



