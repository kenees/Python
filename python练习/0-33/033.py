'''
按逗号分隔列表。
即将列表的每项通过逗号组合成字符串
'''
arr = [1,2,3,4,5,6]
print(arr)
s = ','.join(str(n) for n in arr)
print(s)
print(str(n) for n in arr)

arr2 = ['1','2','3','4']
ss = ','.join(arr2)
print(ss)