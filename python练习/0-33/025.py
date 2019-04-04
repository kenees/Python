'''
题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘。
'''
sum = 0
def get(n):
    if n == 1:
        return 1
    else:
        return n*get(n-1)

for i in range(1,21):
    sum+=get(i)

print(sum)