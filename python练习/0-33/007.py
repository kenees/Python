#题目：将一个列表的数据复制到另一个列表中。

#程序分析：使用列表[:]。

list = [1,2,3,4,5,6,7]

list2 = list[:]

print(id(list))
print(id(list2))