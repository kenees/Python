'''
题目：字符串排序。
'''

arr = []

str1 = input("string:")
str2 = input("string:")
str3 = input("string:")

arr.append(str1)
arr.append(str2)
arr.append(str3)

arr.sort()

for i in arr:
    print(i)