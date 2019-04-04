'''
题目：模仿静态变量的用法。
'''

def varfunc():
    num = 0
    print('num=%d'%num)
    num+=1

for i in range(3):
    varfunc()


class static:
    staticNum = 0
    def add(self):
        self.staticNum+=1
        print(self.staticNum)


a = static()

a.add()
a.add()
a.add()
