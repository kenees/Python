'''
题目：八进制转换为十进制
'''
# num = input('num:')
# all = 0
# num = num[::-1]
# for v in range(len(num)):
#     print(v)
#     all+=int(num[v])*(8**v)
#
# print(all)

if __name__ == '__main__':
    n = 0
    p = input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
        print(n)
    print(n)