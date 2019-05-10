'''
题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
'''

s = input('str:')

file = open('abcc','w')
ss = s.upper()
print(ss)
print(s)
file.write(ss)
file.close()

