'''
    题目：求一个3*3矩阵主对角线元素之和。

    程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
'''
a = []
for i in range(3):
    arr = []
    for j in range(3):
        num = int(input('请输入%s %s位置的数'%(i,j)))
        arr.append(num)
    a.append(arr)

count = 0
for k in range(3):
    count+=a[k][k]
print(count)