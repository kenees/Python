#输出指定格式的日期。
#python中与时间相关的一个模块是time模块，datetime模块可以看为是time模块的高级封装。

import time
import datetime


#用来获取时间戳，表示的结果为从1970年1月1日开始计算到现在时间之间的秒数。如：
print('时间戳：time.time() ->{}'.format(time.time()))

#获取当前时间信息。包含年月日时分秒等等。返回结果以元组的形式返回。如：
print('当前时间信息：time.localtime() ->{}'.format(time.localtime()))

#将localtime()中获取的时间元组转换为自定义的日期时间格式进行。如：
tstr = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(tstr)

#可以将时间秒转换为日期时间，此时日期和时间表示的是标准时间，北京时间为标准时间加上8个小时。不传入参数代表当前时间即转换time()函数的结果。如：
print(time.gmtime())
#当传入参数时。如：
print(time.gmtime(1403127843))

#asctime()和ctime()  两个都会返回固定格式的当前日期和时间（Wed Oct 11 21:35:28 2017）
#asctime()接收的是元组格式的日期时间，而ctime()接收的是秒
print(time.ctime(1403127843))
print(time.asctime(time.localtime()))

#mktime()
print(time.time())


#关于datetime模块，使用的时候建议仅使用当中的now()方法。如
print(datetime.datetime.now())