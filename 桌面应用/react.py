import pygame,sys,numpy
# import time
# import random
# pygame.init()
# screencaption=pygame.display.set_caption('hello world')
# screen=pygame.display.set_mode([640,480])
# screen.fill([255,255,255])
#
# zhijing=random.randint(0,100)
# width=random.randint(0,255)
# height=random.randint(0,100)
# top=random.randint(0,400)
# left=random.randint(0,500)
# pygame.draw.circle(screen,[0,0,0],[top,left],zhijing,1)
# pygame.draw.rect(screen,[255,0,0],[left,top,width,height],3)
#
# pygame.display.update()
# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             sys.exit()

Matrix = numpy.zeros([2,4])
for i in range(2):
    for j in range(4):
        Matrix[i][j] = i*1+j+1
print('---Matrix-------')
print(Matrix)
print('----Matrix2------')
# print(Matrix.copy()[:,::-1])

Matrix2 = numpy.zeros([4,2])
for ii in range(4):
    for jj in range(2):
        Matrix2[ii][jj] = ii+jj+1

print(Matrix2)
print('------Matrix.T---转置-------')
print(Matrix.T)
print('------Matrix.T.T 转置----------')
print(Matrix.T.T)
print('---Matrix * Matrix2-- 相乘---')
print(Matrix.dot(Matrix2))