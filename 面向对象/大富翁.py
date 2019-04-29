import random

#棋盘类,依据当前步数判断活动
class Checkerboard:
    def __init__(self):
        print('生成棋盘')

    def checkStep(self,count,player):
        print('count:',count)
        print('player:',player)
        if count == 2 or count == 8 or count == 15 or count == 25:
            print('恭喜活动加速前进3步')
            player.go(3,self)
            print('---------------------')
        elif count == 4 or count == 17 or count == 31 or count == 38:
            print('心情不好退后2步')
            player.go(-2,self)
            print('---------------------')
        elif count == 3 or count == 12 or count == 21 or count == 27:
            print('恭喜活动加速前进1步')
            player.go(1,self)
            print('---------------------')
        elif count == 7 or count == 11 or count == 26 or count == 40:
            print('恭喜活动加速前进5步')
            player.go(5,self)
            print('---------------------')
        elif count == 6 or count == 23 or count == 29 or count == 44:
            print('心情不好退后5步')
            player.go(-5,self)
            print('---------------------')
        elif count == 9 or count == 19 or count == 33 or count == 49:
            print('心情不好退后4步')
            player.go(-4,self)
            print('---------------------')

#骰子
class Dice:
    def count(self):
        return random.randint(1,6)

#玩家
class PlayUser:
    pass
    def __str__(self):
        return self.name

    def __init__(self,name):
        self.name = name  #名字
        self.fra = 0      #分数

    def play(self,dice,checkerboard):
        print('开始投掷骰子...')
        count = dice.count()
        print('投掷结束：%d' % count)
        print('开始走棋...')
        self.fra+=count
        checkerboard.checkStep(self.fra,self)

    def go(self,count,checkerboard):
        self.fra +=count
        if self.fra < 0:
            self.fra = 0
        checkerboard.checkStep(self.fra,self)

    def getNowStep(self):
        return self.fra

#创建用户
user1 = PlayUser('user1')
user2 = PlayUser('user2')
#创建棋盘
checkerboard = Checkerboard()
#创建骰子
dice = Dice()
#开始投掷
t = 1
while True:
    print('第%d局'%t)
    if user1.getNowStep()>50:
        print('user1赢了')
        break
    elif user2.getNowStep()>50:
        print('user2赢了')
        break
    else:
        user1.play(dice,checkerboard)
        user2.play(dice,checkerboard)
        t+=1


