'''
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
'''

arr = []
def getMax(array):
    maxN = array[0]
    index = 0
    for i in range(1,len(array)):
        if array[i]>maxN:
            maxN = array[i]
            index = i
    # return maxN,index
    else:
        str = arr[0]
        arr[0] = arr[index]
        arr[index] = str

def getMin(array):
    minN = array[0]
    index = 0
    for i in range(1,len(array)):
        if array[i]<minN:
            minN = array[i]
            index = i
    else:
        str = arr[-1]
        arr[-1] = arr[index]
        arr[index] = str


def getInput():
    for i in range(6):
        s = int(input('输入第%d个数字：'%i))
        arr.append(s)

    getMax(arr)
    getMin(arr)
    print(arr)

getInput()
