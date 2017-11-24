# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 15:05
# @Author  : Matthew
# @Site    : 
# @File    : The million fibs.py
# @Software: PyCharm Community Edition
import time
def multi(a,b):
    c=[[0,0],[0,0]]
    c[0][0]=a[0][0]*b[0][0]+a[0][1]*b[1][0]
    c[1][0]=a[1][0]*b[0][0]+a[1][1]*b[1][1]
    c[0][1]=a[0][0]*b[0][1]+a[0][1]*b[1][1]
    c[1][1]=a[1][0]*b[0][1]+a[1][1]*b[1][1]
    return c
def fib(n):
    base=[[1,1],[1,0]]
    ans=[[1,0],[0,1]]
    while n:
        if n%2==1:
            ans=multi(ans,base)
        base=multi(base,base)
        n/=2
    return ans[0][1]
a=time.time()
print fib(6)
b=time.time()
print b-a