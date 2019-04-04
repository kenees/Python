'''
题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
'''
f1 = open('A','r')
f2 = open('B','r')
f3 = open('C','w')
s1 = f1.read()
s2 = f2.read()

print(s1)
print(s2)
arr = list(s1+s2)
print(arr)
arr.sort()
f3.write(''.join(arr))

f1.close()
f2.close()
f3.close()