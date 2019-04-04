'''
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''
n = int(input('整数n为：'))
m = int(input('向后移m个位置为：'))
arr = []
for i in range(n):
    s = int(input('输入一个数字：'))
    arr.append(s)

print(arr)
arr1 = arr[-m:]
arr2 = arr[:-m]
arr = arr1+arr2
print(arr)