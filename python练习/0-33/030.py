'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''


def getInput():
    num = input('请输入五位数：')
    if len(num)!=5 or (not int(num)):
        print('请输5个数字')
        getInput()
    else:
        pass
        for i in range(2):
            if num[i] != num[4-i]:
                print('不是')
                return
        print('是')

getInput()
