# -*- coding: utf-8 -*-
# @Time    : 2017/11/19 14:17
# @Author  : Matthew
# @Site    : 
# @File    : Square into Squares. Protect trees!.py
# @Software: PyCharm Community Edition
def find(sign,mark):
    for i in range(len(sign)):
        if sign[i]>=mark and sign[i+1]<mark:
            return sign[i]

def decompose(n):
    sign,mark,res=[],flag,n**2,[],n-1
    for i in range(1,n):
        sign.append(n**2)
    while mark>0:

#??????