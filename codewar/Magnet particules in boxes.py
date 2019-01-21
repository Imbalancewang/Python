# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 15:48
# @Author  : Matthew
# @Site    : 
# @File    : Magnet particules in boxes.py
# @Software: PyCharm

# 精度有问题？？？
import math
from decimal import *
getcontext().prec=20
def cal_v(k,n):
    return Decimal(1.0/(k*pow(n+1,2*k)))
def doubles(maxk, maxn):
    # your code
    s=Decimal(0.0)
    for i in range(1,maxk+1):
        for j in range(1,maxn+1):
            s=(math.fsum([s,cal_v(i,j)]))
    return s

if  __name__=="__main__":
    print doubles(20,10000)