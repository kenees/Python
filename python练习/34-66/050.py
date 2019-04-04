'''
输出一个随机数。
程序分析：使用 random 模块。
'''
import random
#生成随机浮点数(0,1)
a = random.random()
print(a)
#生成随机1-10之间的整数
b = random.randint(1,10)
print(b)

#随机生成0-20之间的偶数
print ("randrange:", random.randrange(0,21,2))

#随机生成0-20之间的浮点数
print("uniform:", random.uniform(0,20))

#从列表序列中随机取一个数
li = [1,2,3,4,5,6,7,8,9]
print ("choice list:", random.choice(li))
print ("choice string:", random.choice("abcdef"))