'''
题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
     每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
'''
num = int(input('请输入四位数字：'))
s1 = int(num/1000)
s2 = int((num%1000)/100)
s3 = int((num%1000%100)/10)
s4 = int(num%1000%100%10)

def addPass(n):
    return (n+5)%10

s1 = addPass(s1)
s2 = addPass(s2)
s3 = addPass(s3)
s4 = addPass(s4)

s = s1
s1 = s4
s4 = s
s = s2
s2 = s3
s3 = s
print(s1,s2,s3,s4)