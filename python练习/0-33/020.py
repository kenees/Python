'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
sh = 100
indx = 0
s = 100
while indx<10:
    indx+=1
    if indx == 9:
        s+=sh/2
    else:
        s+=sh
    sh/=2
    print('index:%s,sh:%s'%(indx,sh))

print(s)
print(sh)
