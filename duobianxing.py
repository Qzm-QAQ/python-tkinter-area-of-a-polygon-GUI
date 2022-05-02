import numpy as np
import tkinter as tk
from setuptools import Command
windows = tk.Tk()
windows.geometry('800x600')
windows.resizable(0,0)#大小不可改变
windows.title("秦梓茗的多边形面积计算器")
ls1=tk.StringVar
ls2=tk.StringVar
Entry1=tk.Entry(windows,textvariable=ls1)
Entry1.pack()
Entry2=tk.Entry(windows,textvariable=ls2)
Entry2.pack()
Entry1.place(height = 35,width = 100,x = 84,y = 82)
Entry2.place(height = 35,width = 100,x = 84,y = 159)
Label1=tk.Label(windows,text = "请输入多边形点x的坐标列 请用英文输入法 输入用例:X1,X2,...,Xn")
Label1.place(height = 16,width = 400,x = 81,y = 58)
Label2=tk.Label(windows,text = "请输入多边形点y的坐标列 请用英文输入法 输入用例:Y1,Y2,...,Yn")
Label2.place(height = 16,width = 400,x = 81,y = 144)

lstx=[]
lsty=[]
def chuli():  
    a=Entry1.get()
    b=Entry2.get()
    lstx = a.split(',')
    lstx = [float(lstx[i]) for i in range(len(lstx))]
    lsty = b.split(',')
    lsty = [float(lsty[i]) for i in range(len(lsty))]
    area=PolyArea(lstx,lsty)
    windows2 = tk.Tk()
    windows2.geometry('400x300')
    Label1=tk.Label(windows2,text = "结果是"+str(area))
    Label1.place(height = 16,width = 300,x = 51,y = 58)
    
     
Button2=tk.Button(windows,text="计算",font=35,command =chuli)
Button2.place(height = 60,width = 148,x = 316,y = 400)



def PolyArea(lstx,lsty):
    return 0.5*np.abs(np.dot(lstx,np.roll(lsty,1))-np.dot(lsty,np.roll(lstx,1))) #鞋带定理

"""

lstx=[0,1,0.5]
lsty=[0,0,1]
lstx=[0,1,1,0]
lsty=[0,0,1,1]

def PolyArea(lstx,lsty):
    return 0.5*np.abs(np.dot(lstx,np.roll(lsty,1))-np.dot(lsty,np.roll(lstx,1))) #鞋带定理
area=PolyArea(lstx,lsty)
print(area)

"""
windows.mainloop()