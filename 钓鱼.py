
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from ctypes import *

from PIL import ImageGrab,Image
import time
# img = ImageGrab.grab((0,0,100,100))
# img.save('1.png')
# img1 = Image.open('1.png')

# color = img.getpixel((10,0))
# print(color)
# color1 = img.getpixel((10,50))
# print(color1)


m = PyMouse()
k = PyKeyboard()
# print(m.position())
# m.move(10,50)

# m.click(0,0,1)

# k.press_key('k.alt_key')
while True:
    pass
    img = ImageGrab.grab((0,0,100,100))  #获取截图
    color1 = img.getpixel((10,50))        #获取10，50位置的颜色
    #m.move(10,50)                       #移动到10，50
    if color1[0] == 183 and color1[1] == 39 and color1[2]==18:      #获取的颜色为钓鱼成功后的颜色
        print('鱼上钩了，点击收取')
        #m.click(10,50)  #F键的位置，点击收鱼
        k.press_key('F')
        k.release_key('F')
        time.sleep(2)
        print('撒鱼饵')
        #m.click(10,80)  #鱼饵快捷键的位置点击钓鱼
        k.press_key('R')
        k.release_key('R')
    else:
        print('鱼未上钩')

    time.sleep(3)
    print(time.time())