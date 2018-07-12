#乌龟吃鱼
import random
#乌龟类
class Turtle:
    def __init__(self):
        self.power=100 #体力
        #乌龟坐标
        self.x=random.randint(0,10)
        self.y=random.randint(0,10)
    #乌龟移动的方法：移动方向均随机 第四条
    def move(self):
        #计算移动后的新位置（只有四种可能）
        new_x=self.x+random.choice([1,2,-1,-2])
        new_y=self.y+random.choice([1,2,-1,-2])
        #判断移动后是否超出边界
        if new_x<0:
            self.x=0-new_x
        elif new_x>10:
            self.x=10-(new_x-10)
        else:
            #不越界则移动乌龟的位置
            self.x=new_x
        if new_y<0:
            self.y=0-new_y
        elif new_y>10:
            self.y=10-(new_y-10)
        else:
            #不越界则移动乌龟的位置
            self.y=new_y
        self.power-=1 #乌龟每移动一次，体力消耗1
    def eat(self):
        self.power+=20 #乌龟吃掉鱼，乌龟体力增加20
        if self.power>100:
            self.power=100 #乌龟体力100（上限）

#鱼类
class Fish:
    def __init__(self):
        #鱼坐标
        self.x=random.randint(0,10)
        self.y=random.randint(0,10)
    def move(self):
        #计算移动后的新位置（只有四种可能）
        new_x=self.x+random.choice([1,-1])
        new_y=self.y+random.choice([1,-1])
        #判断移动后是否超出边界
        if new_x<0:
            self.x=0-new_x
        elif new_x>10:
            self.x=10-(new_x-10)
        else:
            #不越界则移动鱼的位置
            self.x=new_x
        if new_y<0:
            self.y=0-new_y
        elif new_y>10:
            self.y=10-(new_y-10)
        else:
            #不越界则移动鱼的位置
            self.y=new_y


#开始测试数据
tur=Turtle() #生成1只乌龟
fish=[] #生成10条鱼
for item in range(10):
    fish.append(Fish()) #把生成的鱼放到鱼缸里
i = 0
while True:
    #判断游戏是否结束：当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
    i+=1
    if tur.power<0:
        print("Game Over ~乌龟饿死了")
        break
    if  len(fish)==0:
        print("Game Over ~鱼没了")
        break
    #游戏开始
    #首先乌龟迈出第一步
    #print(tur.x,tur.y) #乌龟移动前
    tur.move()
    print(i,tur.x,tur.y) #乌龟移动后
    #鱼移动一步
    for item in fish:
        item.move()
        if item.x==tur.x and item.y==tur.y:
            tur.eat()
            fish.remove(item)
            print("死了一只鱼")
            print("乌龟最新体力值为 %d"%tur.power)