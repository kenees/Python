'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
Monday Tuesday wednesday thursday friday saturday sunday
'''


s = input('请输入：')
s = s.upper()
if s == "M":
    print('Monday')
elif s == "W":
    print('Wednesday')
elif s == 'F':
    print('friday')
elif s == "T":
    pass
    s2 = input('请输入第二个字母：')
    s2 = s2.upper()
    if s2 == "U":
        print('Tuesday')
    elif s2 == "H":
        print('thursday')
    else:
        print('输入错误')
elif s == "S":
    pass
    s2 = input('请输入第二个字母：')
    s2 = s2.upper()
    if s2 == "U":
        print('sunday')
    elif s2 == "A":
        print('saturday')
    else:
        print('输入错误')
else:
    print('输入错误')