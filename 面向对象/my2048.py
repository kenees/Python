import numpy,sys,random,pygame
from pygame.locals import *

Size = 4                                          #4*4行列
Block_WH = 110                                    #每个块的长度宽度
BLock_Space = 10                                  #两个块之间的间隙
Block_Size = Block_WH*Size+(Size+1)*BLock_Space   #窗口宽度
Matrix = numpy.zeros([Size,Size])                 #初始化矩阵4*4的0矩阵
#print(Matrix)
Screen_Size = (Block_Size,Block_Size+110)         #窗口宽高
Title_Rect = pygame.Rect(0,0,Block_Size,110)      #设置标题矩形的大小
Score = 0

Block_Color = {
    0:(150,150,150),
    2:(255,255,255),
    4:(255,255,128),
    8:(255,255,0),
    16:(255,220,128),
    32:(255,220,0),
    64:(255,190,0),
    128:(255,160,0),
    256:(255,130,0),
    512:(255,100,0),
    1024:(255,70,0),
    2048:(255,40,0),
    4096:(255,10,0),
}                                                     #数块颜色
class UpdateNew(object):
    def __init__(self,matrix):
        super(UpdateNew,self).__init__()
        self.matrix = matrix
        self.score = 0
        self.zerolist = []

    def combineList(self,rowlist):
        # print(rowlist)
        start_num = 0
        end_num = Size - rowlist.count(0) - 1  #    去掉为零的个数  1，2，0，0  即左边有数字的个数
        while start_num < end_num:
            #只有不够4个才进行计算，有四个就不进行计算
            if rowlist[start_num] == rowlist[start_num+1]:
                #合并左右一样的数字
                rowlist[start_num] *= 2
                #计分
                self.score += int(rowlist[start_num])
                rowlist[start_num+1:] = rowlist[start_num+2:] #去掉合并后多余的一个位置
                rowlist.append(0)
            start_num += 1
        return rowlist

    def removeZero(self,rowlist):
        while True:
            mid = rowlist[:]
            try:
                #移除所有0，末尾追加0  -相当于所有数据左移
                rowlist.remove(0)
                rowlist.append(0)
            except:
                pass
            if rowlist == mid:
                break;
        return self.combineList(rowlist)

    def toSequence(self,matrix,gameInit):
        lastmatrix = matrix.copy()
        m,n = matrix.shape
        for i in range(m):
            #去掉右边的0，合并左边的数，不足补0，并计分
            newList = self.removeZero(list(matrix[i]))
            matrix[i] = newList
            # 倒叙遍历0的位置
            for k in range(Size-1,Size-newList.count(0)-1,-1):
                self.zerolist.append((i,k))   #添加所有为0的位置
        if matrix.min() == 0 and (matrix!=lastmatrix).any():
            gameInit.initData(Size,matrix,self.zerolist)
        return matrix

class LeftAction(UpdateNew):
    def __init__(self,matrix):
        super(LeftAction,self).__init__(matrix)

    def handleData(self,gameInit):
        matrix = self.matrix.copy()                               #获得一份矩阵的复制
        newmatrix = self.toSequence(matrix,gameInit)
        return newmatrix,self.score

class RightAction(UpdateNew):
    def __init__(self,matrix):
        super(RightAction,self).__init__(matrix)

    def handleData(self,gameInit):
        #将二维数组左右数据颠倒
        matrix = self.matrix.copy()[:,::-1]
        newmatrix = self.toSequence(matrix,gameInit)
        return newmatrix[:,::-1],self.score


class UpAction(UpdateNew):
    def __init__(self,matrix):
        super(UpAction,self).__init__(matrix)

    def handleData(self,gameInit):
        matrix = self.matrix.copy().T
        newmatrix = self.toSequence(matrix,gameInit)
        return newmatrix.T,self.score

class DownAction(UpdateNew):
    def __init__(self,matrix):
        super(DownAction,self).__init__(matrix)

    def handleData(self,gameInit):
        matrix = self.matrix.copy()[::-1].T
        newmatrix = self.toSequence(matrix,gameInit)
        return newmatrix.T[::-1],self.score

class GameInit(object):
    def __init__(self):
        super(GameInit, self).__init__() #TODO??

    def getRandomLocal(self,zerolist = None):
        if zerolist == None:
            a = random.randint(0,Size-1)
            b = random.randint(0,Size-1)
        else:
            a,b = random.sample(zerolist,1)[0]  ## 从list中随机获取1个元素，作为一个片断返回

        return a,b

    def getNewNum(self):     #随机返回2或者4
        n = random.random()
        if n > 0.8:
            n = 4
        else:
            n = 2
        return n


    def initData(self,Size,matrix = None,zerolist = None):
        if matrix is None:
            matrix = Matrix.copy()        #如果martix为空，则拷贝一份初始矩阵
        a,b = self.getRandomLocal(zerolist)  #zerolist空任意返回(x,y)位置，否则返回任意一个0元素位置
        n = self.getNewNum()
        matrix[a][b] = n
        return matrix                       #返回初始化任意位置为2或者4的矩阵


    def drawSurface(self,screen,matrix,score):
        #绘制头部
        pygame.draw.rect(screen,(255,255,255),Title_Rect)
        # rect（Surface，color，Rect，width = 0） - > Rect
        # width参数是绘制外边缘的粗细。如果width(线宽)为零，则填充矩形。
        font1 = pygame.font.SysFont('simsn',48)
        font2 = pygame.font.SysFont(None,32)
        #从文件创建一个新的Font对象

        screen.blit(font1.render('Score:',True,(255,127,0)),(20,25))
        screen.blit(font1.render('%s' % score,True,(255,127,0)),(170,25))
        screen.blit(font2.render('up',True,(255,127,0)),(350,15))
        screen.blit(font2.render('left down right',True,(255,127,0)),(300,55))
        #在新Surface上绘制文本 render(文本，抗锯齿，颜色，背景=无) -> Surface
        #将许多图像绘制到另一个 blit（source，dest，area = None，special_flags = 0） - > Rect
        #dest 可以是表示源左上角的坐标时
        a,b = matrix.shape
        for i in range(a):
            for j in range(b):
                self.drawBlock(screen,i,j,Block_Color[matrix[i][j]],matrix[i][j])

    def drawBlock(self,screen,row,colum,color,blocknum):
        font = pygame.font.SysFont('stxingkai',80)
        w = colum*Block_WH+(colum+1)*BLock_Space
        h = row*Block_WH+(row+1)*BLock_Space+110
        pygame.draw.rect(screen,color,(w,h,110,110))  #绘制矩形
        if blocknum!=0:
            fw,fh = font.size(str(int(blocknum)))
            screen.blit(font.render(str(int(blocknum)),True,(0,0,0)),(w+(110-fw)/2,h+(110-fh)/2))

    def keyDownPressed(self,keyvalue,matrix):
        if keyvalue == K_LEFT:
            return LeftAction(matrix)
        elif keyvalue == K_RIGHT:
            return RightAction(matrix)
        elif keyvalue == K_UP:
            return UpAction(matrix)
        elif keyvalue == K_DOWN:
            return DownAction(matrix)

    def gameOver(self,matrix):
        testmatrix = matrix.copy()
        a,b = testmatrix.shape
        for i in range(a):
            for j in range(b-1):
                if testmatrix[i][j] == testmatrix[i][j+1]:
                    print('游戏没有结束')
                    return False
        for i in range(b):
            for j in range(b-1):
                if testmatrix[i][j] == testmatrix[j+1][i]:
                    print('游戏没有结束')
                    return False
        print('游戏结束')
        return True

def main():
    pygame.init()   #初始化pygame
    screen = pygame.display.set_mode(Screen_Size,0,32)   #初始化窗口或屏幕以进行显示
    #screen.fill([255,255,255])  #默认黑底，可设置
    # set_mode（resolution =（0,0），flags = 0，depth = 0） - > Surface
    # resolution参数是一对表示宽度和高度的数字。flags参数是其他选项的集合。depth参数表示用于颜色的位数。
    gameInit = GameInit()
    matrix = gameInit.initData(Size)
    #获取一个任意位置为2or4的初始化矩阵
    # print(martix)
    currentscore = 0       #计分
    gameInit.drawSurface(screen,matrix,currentscore)
    pygame.display.update()
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                actionObject = gameInit.keyDownPressed(event.key,matrix)
                matrix,score = actionObject.handleData(gameInit)
                currentscore += score
                gameInit.drawSurface(screen,matrix,currentscore)
                if matrix.min() != 0:
                    gameInit.gameOver(matrix)
        pygame.display.update()

if __name__ == '__main__':
    main()

