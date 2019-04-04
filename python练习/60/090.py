'''
题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
'''

filename = input('文件ming:')
fp = open(filename,'w')
ch = input('输入字符串：\n')
while ch != "#":
    fp.write(ch)
    ch = input('输入字符串：\n')
fp.close()