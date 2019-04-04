#题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
# 1 1 2 3 5 8  13


num = int(input('请输入月份：'))

def sumfun(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return sumfun(n-1)+sumfun(n-2)

print(sumfun(num))