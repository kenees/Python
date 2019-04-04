'''
题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

程序分析：999999 / 13 = 76923。
'''
num = int(input('输入奇数：'))

index = 1
while True:
    num2 = 0
    for i in range(index):
        num2+=9*10**i
    else:
        if num2%num ==0:
            print(index)
            break
        else:
            index+=1