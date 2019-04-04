'''
按相反的顺序输出列表的值。

b = a[i:j:s] 
s表示步进，缺省为1
so:
    a[i:j:1]相当于 a[i:j]
    当s<0时，i缺省时默认为-1，j缺省时默认为-len(a)-1   ,-len(a)-1是因为包左不包右
    所以
        a[::-1] 相当于 a[-1:-len(a)-1:-1]
'''
a = ['one','two','three','four','five','six','seven','eight','nine','ten']
print(a)
print(a[::-1])
print(a[8:4:-1])
print(a[8:1:-2])

print(a[-1:-len(a)-1:-1])