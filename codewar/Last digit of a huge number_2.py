# -*- coding: utf-8 -*-
# @Time    : 2018/10/19 10:18
# @Author  : Matthew
# @Site    : 
# @File    : Last digit of a huge number_2.py
# @Software: PyCharm
def cal_one(n1,n2):
    if n1==0 and n2==0:return 1
    n=n1%10
    if n2==0: return 1
    if n==0 or n==1 or n==5 or n==6:
        return n
    elif n==2 or n==3 or n==7 or n==8: return n**(n2%4+4)%10
    elif n==4 or n==9: return n**(n2%2+2)%10
def last_digit(lst):
    # Your Code Here
    if len(lst)==0:return 1
    temp = lst[-1]
    for i in range(len(lst)-2,-1,-1):
        temp=cal_one(lst[i],temp)
    return temp