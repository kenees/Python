'''
    打印出杨辉三角10行
    1 
    1 1 
    1 2 1 
    1 3 3 1 
    1 4 6 4 1 
    1 5 10 10 5 1 
    1 6 15 20 15 6 1 
    1 7 21 35 35 21 7 1 
    1 8 28 56 70 56 28 8 1 
    1 9 36 84 126 126 84 36 9 1
'''


a = []
for i in range(10):
    a.append([])
    for j in range(10):
       a[i].append(0)

    a[i][0]=1
    a[i][i]=1

for n in range(2,10):
    for m in range(1,n+1):
        a[n][m] = a[n-1][m]+a[n-1][m-1]

for s in range(10):
    for ss in range(0,s+1):
        print(a[s][ss],end=" ")
    print("")

