'''
    https://blog.csdn.net/PengChong521/article/details/79787380
    案例的目的：
    （1）理解面像对像的基本概念。
    （2）掌握类和对象的定义和使用。
    （3）掌握方法的使用
    案例需求： 在全世界风靡的反恐精英是一个以团队合作为主的第一人称射击游戏，简称cs。
    根据面像对象的编程思想，模拟实现一个战士开枪射击敌人的场景。
    在上述的场景中，有战士（玩家），敌人，枪共三个对象，其中枪又包括弹夹，子弹两个对象。
    场景中这几个对象间的关系如下：
    （1）战士和敌人属于人类，他们默认的血量有100.
    （2）战士射击时必须保障所持抢中的弹夹有子弹，并且每发射一次，弹夹中的子弹的数量就会减一；
    （3）战士射出的子弹击中了敌人，敌人由于子弹的杀伤力二出现掉血的现象，即每击中一次，敌人的血量就会减少5.
    流程图如下：
       创建战士对象——>创建弹夹对象———>创建子弹对象——>弹夹上子弹——>创建枪的对象——>枪安装弹夹——>出现敌人——>士兵拿枪——>士兵开枪——>士兵再次开枪
    案例分析 面像对象是最重要的是类的设计，所以对案例分析的时候，首先根据“名词提炼法”，分析业务流程中需要设计的类，然后分析所拥有的属性与方法。
    根 据这个模拟的场景，我们可以分析出来的类具体如下。
    （1）士兵和敌人类 属性：姓名（name），血量（blood），枪（gun）。
    （2）子弹类 属性：杀伤力。 方法：伤害敌人（让敌人掉血）
    （3）弹夹类 属性：容量（子弹储存的在最大值），当前保存的子弹。
             方法：保存子弹（安装子弹），弹出子弹（开枪的时候）。
     （4）枪类 属性：弹夹（默认没有弹夹，需要安装）。
            方法：连接弹夹，射子弹
'''

class Person:
    pass
    def __init__(self,name):
        #姓名
        self.name =  name
        #血量
        self.blood = 100
    #上子弹
    def installBullet(self,clip,bullet):
        clip.saveBullet(bullet)

    #上弹夹
    def installClip(self,gun,clip):
        gun.mountingClip(clip)
    #连接枪
    def takeGun(self,gun):
        self.gun = gun

    #开火
    def fire(self,enemy):
        self.gun.shoot(enemy)

    #显示person
    def __str__(self):
        return self.name+'剩余血量：'+str(self.blood)

    #掉血
    def loseBlood(self,damage):
        self.blood -=damage


#子弹
class Bullet:
    pass
    def __init__(self,damage):
        self.damage = damage

    #子弹伤害方法
    def hurt(self,enemy):
        enemy.loseBlood(self.damage)

#弹夹
class Clip:
    pass

    def __init__(self,capacity):
        #capacity  子弹容量
        self.capacity = capacity
        self.currentList = []

    #安装子弹
    def saveBullet(self,bullet):
        if len(self.currentList)<self.capacity:
            self.currentList.append(bullet)

    #显示弹夹信息
    def __str__(self):
        return '弹夹当前的数量为：'+str(len(self.currentList))+'/'+str(self.capacity)

    #射出子弹
    def shotBullet(self):
        if len(self.currentList)>0:
            bullet =  self.currentList.pop()
            return  bullet
        else:
            return None


#枪
class Gun:
    pass
    def __init__(self):
        self.clip = None

    def __str__(self):
        if self.clip:
            return "枪有弹夹"
        else:
            return "枪木有弹夹"

    #子弹连接弹夹
    def mountingClip(self,clip):
        if not self.clip:
            self.clip = clip


    #射击
    def shoot(self,enemy):
        bullet = self.clip.shotBullet()
        if bullet:
            bullet.hurt(enemy)
        else:
            print('没有子弹了。。。')




soldier = Person('老王')
#创建一个有20容量的弹夹
print("----------创建一个有20发子弹容量的弹夹-------")
clip = Clip(20)
print(clip)
print('-------给弹夹安装子弹-----------')
i = 0
while i<10:
    bullet = Bullet(5)
    clip.saveBullet(bullet)
    i+=1

print(clip)
#创建一把枪
print('--------创建一把枪------')
gun = Gun()
print(gun)
#上弹夹
print('-----给枪上弹夹-------')
soldier.installClip(gun,clip)
print(gun)
#创建一个敌人
print('--------创建一个敌人-------')
enemy = Person('敌人')
print(enemy)

#拿枪
print('-------拿枪------')
soldier.takeGun(gun)
#射击
print('----射击-------')
soldier.fire(enemy)
print(clip)
print(enemy)
print('----射击-------')
soldier.fire(enemy)
print(clip)
print(enemy)
print('----射击-------')
soldier.fire(enemy)
print(clip)
print(enemy)