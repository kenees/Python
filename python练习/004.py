#题目：输入某年某月某日，判断这一天是这一年的第几天？
#程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

year = int(input('年'))
month = int(input('月'))
day = int(input('日'))

frb = 28
if(month%400==0 or year%4==0):
    frb = 29
arr = [31,frb,31,30,31,30,31,31,30,31,30,31]
sum = 0
for i in range(12):
    if i<(month-1):
       sum+=arr[i]
    if i ==(month-1):
        sum+=day
print(sum)
