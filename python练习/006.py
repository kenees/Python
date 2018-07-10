#斐波那契数列
#斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

def num(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return num(n-1)+num(n-2)
# 输出了第10个斐波那契数列
print(num(10))