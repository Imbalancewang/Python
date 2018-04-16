# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 16:18
# @Author  : Matthew
# @Site    : 
# @File    : Simple Fun #132: Number Of Carries.py
# @Software: PyCharm
def number_of_carries(a, b):
    tmpa,tmpb,count,ct=a,b,0,0
    while(tmpa or tmpb):
        ta,tb=tmpa%10,tmpb%10
        tmpa=tmpa/10
        tmpb=tmpb/10
        if(ta+tb+ct>=10):
            ct=1
            count+=1
        else:ct=0
    return count
print number_of_carries(1,9999)
print number_of_carries(1927,6426)
print number_of_carries(1234,5678)
print number_of_carries(543,3456)