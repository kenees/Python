from pymouse import PyMouse
from ctypes import *

windll = CDLL('/Users/eme/Desktop/X86/b001/windll.dll')

#引入winapi
gdi32 = windll.gdi32
user32 = windll.user32
#获取句柄
hdc = user32.GetDC(None)
c = gdi32.GetPixel(hdc,100,50)
print(hex(c))

m = PyMouse()
print(m.position())
m.move(100,50)
# m.click(0,0,1)

