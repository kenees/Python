'''
    列表排序及连接
    排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。
'''
a = [1,4,3]
b = [4,5,6]
a.sort()
print(a)
a.extend(b)
print(a)