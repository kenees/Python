'''
题目：将一个数组逆序输出。

程序分析：用第一个与最后一个交换。
'''
arr = [3,4,7,2,1,8,9,10]
for i in range(int(len(arr)/2)):
    a = arr[i]
    arr[i] = arr[len(arr)-1-i]
    arr[len(arr)-1-i] = a

print(arr)