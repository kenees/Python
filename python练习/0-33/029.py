'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

程序分析：学会分解出每一位数。
'''

num = int(input('请输入一个数：'))

s = str(num)
l = len(s)
print('num是%s位数'%l)
for i in range(l):
    print(s[l-i-1])
