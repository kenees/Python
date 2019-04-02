#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

a = input('请输入：')
letters = 0
space = 0
number = 0
others = 0

for i in a:
    c = i
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        number+=1
    else:
        others+=1

print('字母有{}个，空格有{}个，数字有{}个，其他字符有{}个'.format(letters,space,number,others))
'''
ssss
'''
str ="""
大法师带饭的
是s
"""
print(str)
