
from tkinter import *                           #引用Tk模块
root = Tk()                                     #初始化Tk()


root.title('hello world')                       #设置窗口标题
root.geometry('300x500')                        #设置窗口大小
root.resizable(width=False,height=True)         #设置窗口是否可以变化长 宽#宽不可变, 高可变,默认为True



def printhello():
    t.insert(END,'你是大傻逼\n')

'''
控件
    Label
        标签
        Laber(根对象，[属性列表])
        属性：
            text   要实现的文本
            bg     背景颜色
            font   字体（颜色，大小）
            width  控件宽度
            height 空间高度
    Frame
        在屏幕上创建一块矩形区域,多作为容器来布局窗体
        Frame(根对象, [属性列表])
        
    Entry
        创建单行文本框
        用法：
            创建：lb = Entry(根对象，[属性列表])
            绑定变量 
                var = StringVar()  
                lb=Entry(根对象,textvariable = var)
            
    Text
        创建多行文本框
        用法：
            创建：t = Text(根对象)
            插入：t.insert(mark, 内容)
            删除：t.delete(mark1, mark2)
            mark可以是行号，或者特殊标识，例如：
                        INSERT：光标的插入点CURRENT:鼠标的当前位置所对应的字符位置
                        END:这个Textbuffer的最后一个字符
                        SEL_FIRST:选中文本域的第一个字符，如果没有选中区域则会引发异常
                        SEL_LAST：选中文本域的最后一个字符，如果没有选中区域则会引发 异常
            
            
    Button
        创建按钮
        用法：
          Button(跟对象，[属性列表])
          Button(root,text='press',command=printhello).pack()
    Listbox
        列表控件,可以含有一个或多个文本想,可单选也可多选
        用法：
            创建：
                    lb = ListBox(根对象, [属性列表])
            绑定变量：
                    var=StringVar()    
                    lb=ListBox(根对象, listvariable = var)
            得到列表中的所有值：
                    var.get()
            设置列表中的所有值：
                    var.set((item1, item2, .....))
            添加：
                    lb.insert(item)
            删除:
                    lb.delete(item,...)
            绑定事件: 
                    lb.bind('<ButtonRelease-1>', 函数)
            获得所选中的选项:
                    lbl.get(lb.curselection())
        属性：
            selectmode可以为BROWSE MULTIPL SINGLE
    Scrollbar
    说明每个控件最后要加上pack().否则控件是无法显示的.
'''

#l = Label(root,text='点我啊',bg='blue',font=('Arial',15),width=5,height=5)
#l.pack(side=LEFT)    #side可以为：LEFT RIGHT TOP BOTTOM

#创建一个标签
box = Label(root,text='校训',font=('Arial',15))
box.pack()

frm = Frame(root)#创建一个大容器

frm_L = Frame(frm)#在大容器里创建一个小容器
Label(frm_L,text='厚德',font=('Arial',15)).pack(side=TOP)  #在小容器里创建标签
Label(frm_L,text='博学',font=('Arial',15)).pack(side=BOTTOM)
frm_L.pack(side=LEFT)

frm_R = Frame(frm)#再在大容器里创建一个小容器
Label(frm_R,text='厚德',font=('Arial',15)).pack(side=TOP)  #在小容器里创建标签
Label(frm_R,text='博学',font=('Arial',15)).pack(side=BOTTOM)
frm_R.pack(side=RIGHT)

frm.pack()#显示大容器

#创建一个单行文本狂
var = StringVar()
lb=Entry(root,textvariable = var)
var.set('你丝赛')
lb.pack()

#创建一个多行文本框
t = Text(root)
t.insert(1.0,'你说你是不是一个big sb\n')
t.insert(END,'lalall\n')
t.insert(END,'hahaha')
t.insert(END,'sbsbsb\n')
t.pack()

Button(root,text='猜猜我是谁',font=('Arial',18), command=printhello).pack(side=BOTTOM)


#创建要给listbox



root.mainloop()                                 #进入消息循环