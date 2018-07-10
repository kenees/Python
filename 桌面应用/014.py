from tkinter import *

def run():
    dic={0:'',1:'足球',2:'篮球',3:'游泳',4:'田径'}
    chknum=[CheckVar1.get(),CheckVar2.get(),CheckVar3.get(),CheckVar4.get()]
    s=''
    for i in chknum:
        s =dic.get(i)
    if s=='':
        s='您没有选择任何爱好项目'
    else:
        s='您选择了'+s

    lb2.config(text=s)

def all():
    ch1.select()
    ch2.select()
    ch3.select()
    ch4.select()

def invert():
    ch1.toggle()
    ch2.toggle()
    ch3.toggle()
    ch4.toggle()

def cancel():
    ch1.deselect()
    ch2.deselect()
    ch3.deselect()
    ch4.deselect()

root=Tk()
lb1=Label(root,text='请选择您的爱好项目：')
lb1.pack()


CheckVar1=IntVar()
CheckVar2=IntVar()
CheckVar3=IntVar()
CheckVar4=IntVar()

ch1=Checkbutton(root,text='足球',variable=CheckVar1,onvalue=1,offvalue=0)
ch1.pack()

ch2=Checkbutton(root,text='篮球',variable=CheckVar2,onvalue=2,offvalue=0)
ch2.pack()

ch3=Checkbutton(root,text='游泳',variable=CheckVar3,onvalue=3,offvalue=0)
ch3.pack()

ch4=Checkbutton(root,text='田径',variable=CheckVar4,onvalue=4,offvalue=0)
ch4.pack()

btninvert=Button(root,text='反选',command=invert)
btninvert.pack(side=RIGHT)

btnall=Button(root,text='全选',command=all)
btnall.pack(side=RIGHT)

btncancel=Button(root,text='重置',command=cancel)
btncancel.pack()

btn=Button(root,text='确认',command=run)
btn.pack()

lb2=Label(root,text='')
lb2.pack()

root.mainloop()