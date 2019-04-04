'''
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''
s = input('str:')

def printStr(ss,i):
    if i>=0:
        print(ss[i])
        printStr(ss,i-1)
    
printStr(s,len(s)-1)