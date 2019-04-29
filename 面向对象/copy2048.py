import pygame,sys,numpy
from pygame.locals import *


def RightAction(matrix):
    pass
    print(matrix)
    m,n = matrix.shape
    print(m,n)
    for i in range(m):
        arr = list(matrix[i])
        arr = [x for x in arr if x != 0]

        while len(arr)<4:
            arr.insert(0,0)
        else:
            print(arr)





class GameInit():
    def __init__(self):
        pass

    def keypassdown(self,keyvalue,Matrix):
        if keyvalue == K_LEFT:
            print('left')
        elif keyvalue == K_RIGHT:
            print('right')
            RightAction(Matrix)
        elif keyvalue == K_UP:
            print('up')
        elif keyvalue == K_DOWN:
            print('down')




def main():
    pygame.init()
    screen = pygame.display.set_mode((100,100),0,32)      #屏幕设置
    gameinit = GameInit()
    Matrix = numpy.zeros([4,4])
    Matrix[1][1] = 1
    Matrix[2][1] = 1
    Matrix[2][2] = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                gameinit.keypassdown(event.key,Matrix)

        pygame.display.update()


if __name__ == '__main__':
    main()