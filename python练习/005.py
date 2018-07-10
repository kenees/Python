#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# x = int(input('x:'))
# y = int(input('y:'))
# z = int(input('z:'))
#
# if x>y:
#     a = x
#     x = y
#     y = a
# if y>z:
#     a = y
#     y = z
#     z = a
# print(x,y,z)


arr =[]

for i in range(3):
    j = int(input('x:'))
    arr.append(j)
arr.sort()
print(arr)

