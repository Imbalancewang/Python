# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 16:25
# @Author  : Matthew
# @Site    : 
# @File    : Rectangle Rotation.py
# @Software: PyCharm
import math

def cal_k_b(x1,x2):
    k=1.0*(x1[1]-x2[1])/(x1[0]-x2[0])
    b=k*(-1)*x1[0]+x1[1]
    return (k,b)

def rectangle_rotation(a, b):
    x1=[math.sqrt(2)/4*(b-a),math.sqrt(2)/4*(b+a)]
    x2=[math.sqrt(2)/4*(b+a),math.sqrt(2)/4*(b-a)]
    x3=[-math.sqrt(2)/4*(b-a),-math.sqrt(2)/4*(b+a)]
    x4=[-math.sqrt(2)/4*(b+a),-math.sqrt(2)/4*(b-a)]
    boundx1=math.ceil(x2[0])
    boundx2=math.floor(x4[0])
    boundy1=math.ceil(x1[1])
    boundy2=math.floor(x3[1])
    s=0
    kb12=cal_k_b(x1,x2)
    kb23=cal_k_b(x2,x3)
    kb34=cal_k_b(x3,x4)
    kb41=cal_k_b(x4,x1)
    for i in range(int(boundx2),int(boundx1)+1):
        for j in range(int(boundy2),int(boundy1+1)):
            if j<=i*kb12[0]+kb12[1] and j>=i*kb23[0]+kb23[1] and j>=i*kb34[0]+kb34[1] and j<=i*kb41[0]+kb41[1]:
                s+=1
    return s

if __name__=="__main__":
    print cal_k_b([1,2],[2,1])
