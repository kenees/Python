#题目：暂停一秒输出。并格式化当前时间。

#程序分析：使用 time 模块的 sleep() 函数。

#	time.localtime([secs])
#   接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。

import time
print(time.time())
time.sleep(1)
print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()-10)))