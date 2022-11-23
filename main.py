# -*-coding:utf-8 -*-
import math#引入数学库

print("准备输入初始区间")

a = float(input("a的值"))
b = float(input("b的值"))
Min = float(input("精确度"))



def TryC():
    global a
    global b
    global fc
    c = float((a+b)/2.0)
    x = float(c)
    fc = float(f(c))
    #print(fc)
    return fc

def TryA():#A判断
    global a
    global b
    x = float(a)
    fa = float(f(a))
    if fa < 0 and TryC()>fa and TryC()<0:
        a = float((a+b)/2.0)
    else:
        a=a
    return a,b


def TryB():#b判断
    global a
    global b
    x = b
    fb = float(f(b))
    if fb > 0 and fb>TryC() and TryC()>0:
        b = float((a+b)/2)
    else:
        b = b
    return b,a


def panduan():#继续判断
    global a
    global b
    global Yes
    global h

    h = float(b -a)
    Yes = True

    if h <= Min:#精确度,同时是“误差”产生的原因
        Yes = False
        print("("+str(a)+","+str(b)+")")#输出最终答案
    elif h > Min:
        TryA()
        TryB()
        #print(str(a)+","+str(b))
        

    return Yes


def f(x):
    return 2*x**3 -1 #可修改的解析式

Yes = True
while Yes:#程序循环
   panduan()
pass
