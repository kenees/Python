'''
题目：利用递归方法求5!。

程序分析：递归公式：fn=fn_1*4!
'''
def get(n):
    if n == 1:
        return 1
    else:
        return n*get(n-1)

print(get(5))