'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律
'''

sum = 0
def getUp(n):
    if n == 0:
        return 2
    elif n == 1:
        return 3
    else:
        return getUp(n-2)+getUp(n-1)

def getDown(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return getDown(n-2)+getDown(n-1)

for i in range(20):
    num = (getUp(i)/getDown(i))
    print(num)
    sum+=num

print(sum)