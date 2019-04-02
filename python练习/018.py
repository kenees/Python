'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
'''

a = int(input('a='))
n = int(input('n='))

sum = 0

def sumNumber(l,length):
    num = 0
    for j in range(length):
        num+=l*10**j
    return num

for i in range(n):
    sum+=sumNumber(a,i+1)

print(sum)

