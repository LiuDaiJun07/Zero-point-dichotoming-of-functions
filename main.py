# -*-coding:utf-8 -*-
import math#������ѧ��

print("׼�������ʼ����")

a = float(input("a��ֵ"))
b = float(input("b��ֵ"))
Min = float(input("��ȷ��"))



def TryC():
    global a
    global b
    global fc
    c = float((a+b)/2.0)
    x = float(c)
    fc = float(f(c))
    #print(fc)
    return fc

def TryA():#A�ж�
    global a
    global b
    x = float(a)
    fa = float(f(a))
    if fa < 0 and TryC()>fa and TryC()<0:
        a = float((a+b)/2.0)
    else:
        a=a
    return a,b


def TryB():#b�ж�
    global a
    global b
    x = b
    fb = float(f(b))
    if fb > 0 and fb>TryC() and TryC()>0:
        b = float((a+b)/2)
    else:
        b = b
    return b,a


def panduan():#�����ж�
    global a
    global b
    global Yes
    global h

    h = float(b -a)
    Yes = True

    if h <= Min:#��ȷ��,ͬʱ�ǡ���������ԭ��
        Yes = False
        print("("+str(a)+","+str(b)+")")#������մ�
    elif h > Min:
        TryA()
        TryB()
        #print(str(a)+","+str(b))
        

    return Yes


def f(x):
    return 2*x**3 -1 #���޸ĵĽ���ʽ

Yes = True
while Yes:#����ѭ��
   panduan()
pass
