

arr = []
file = open('../1.txt','r')
line = file.readline()
print(line)
print('读取完成')
txt = file.read()
print(txt)

file.close()