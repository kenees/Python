'''
编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''
def peve(n):
    pass
    num = 0
    for i in range(1,int(n/2)+1):
        num+=(1/(2*i))
    else:
        return num

def podd(n):
    pass
    num = 0
    for i in range(1,int((n+1)/2)+1):
        num+=(1/(2*i-1))
    else:
        return num

def sum(n):
    if n%2 == 0:
        pass
        print(peve(n))
    else:
        print(podd(n))

stt = int(input('请输入数字：'))
sum(stt)