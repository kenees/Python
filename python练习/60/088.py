'''
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
'''
i = 0
while i<7:
    num = int(input('请输入1-50的整数:\n'))
    if num >50 or num<0:
        pass
    else:
        i+=1
        print('*'*num)