#配置好环境变量
#打开cmd  输入指令 pip install packages
#安装pymysql pip install pymysql

#打开  https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
#download packages
#pip install packages-url

import pygame
#导入pygame中的所有常量
from pygame.locals import  *
white = 255,255,255
blue = 0,0,255


#初始化pygame
pygame.init()

#获取对显示系统的访问，创建一个窗口
screen = pygame.display.set_mode((600,500))
#pygame中使用pygame.font将文本输入到图形窗口，要绘制文本必须要先创建一个字体对象
myfont = pygame.font.Font(None,60)
#myfont = pygame.font.Font(Arial,60)

# myfont.render('文本','抗锯齿字体','颜色')
#textImage 对象是可以使用screen.blit 绘制的平面
textImage = myfont.render('Hello Pygame',True,white)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            exit()
    #screen.fill(blue)
    screen.blit(textImage,(100,100))
    pygame.display.update()



