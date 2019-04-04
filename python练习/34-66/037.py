'''
题目：对10个数进行排序。

程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
'''
arr = []
for i in range(10):
    num1 = int(input('请输入第%s个数字'%i))
    arr.append(num1)

for index in range(len(arr)):
    print('第%s个数字是%s'%(index+1,arr[index]))
print('-------------------------')
arr.sort()

for index2 in range(len(arr)):
    print('排序后第%s个数字是%s'%(index2+1,arr[index2]))

print('-------------------------')
arr.sort(reverse=True)

for index3 in range(len(arr)):
    print('排序后2第%s个数字是%s'%(index3+1,arr[index3]))