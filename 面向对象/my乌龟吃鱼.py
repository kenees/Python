import random
class Turtle:
    def __init__(self):
        self.power=100 #体力
        self.x = random.randint(0,10)
        self.y = random.randint(0,10)

    def __str__(self):
        return '位置（{},{}）'.format (self.x,self.y)

    def move(self):
        newx =self.x + random.choice([-2,-1,1,2])
        newy =self.y + random.choice([-2,-1,1,2])

        if newx<0:
            pass
            print('向左移动超界',newx)
            self.x = 0-newx
        elif newx>10:
            pass
            print('向右移动超界',newx)
            self.x = 10-(newx-10)
        else:
            self.x = newx

        if newy<0:
            pass
            print('向上移动超界',newy)
            self.y = 0-newy
        elif newy>10:
            pass
            print('向下移动超界',newy)
            self.y = 10-(newy-10)
        else:
            self.y = newy

        self.power -=1

    def eat(self):
        pass
        self.power+=20
        if self.power>100:
            self.power  = 100

class Fish:
    pass
    def __init__(self):
        self.x = random.randint(0,10)
        self.y = random.randint(0,10)

    def move(self):
        newx =self.x + random.choice([-1,1])
        newy =self.y + random.choice([-1,1])

        if newx<0:
            pass
            print('向左移动超界')
            self.x = 0-newx
        elif newx>10:
            pass
            print('向右移动超界')
            self.x = 10-(newx-10)
        else:
            self.x = newx

        if newy<0:
            pass
            print('向左移动超界')
            self.y = 0-newy
        elif newy>10:
            pass
            print('向右移动超界')
            self.y = 10-(newy-10)
        else:
            self.y = newy


turtle  = Turtle()
fishs = []
for i in range(10):
    fish = Fish()
    fishs.append(fish)

while True:
    pass
    if turtle.power<0:
        print('game over  饿死了')
        break
    if len(fishs)==0:
        print('game over  没鱼了')
        break

    turtle.move()
    print(turtle)
    for f in fishs:
        f.move()
        if turtle.x == f.x and turtle.y == f.y:
            fishs.remove(f)
            turtle.eat()
            print('死了一只鱼')
            print('乌龟的体力：',turtle.power)

