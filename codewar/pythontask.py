# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 11:30
# @Author  : QiWenjin
# @Site    : 
# @File    : pythontask.py
# @Software: PyCharm
import math
import numpy as np
def transpose(m):
    res=[]
    nrow,ncol=len(m),len(m[0])
    for i in range(nrow):
        tmp=[]
        for j in range(ncol):
            tmp.append(m[j][i])
        res.append(tmp)
    return res
def determinant(m):
    if len(m)!=len(m[0]):
        print 'make sure what you input is a square matrix'
    if len(m) <= 0:
        return None
    if len(m) == 1:
        return m[0][0]
    else:
        s=0
        for i in range(len(m)):
            n=[[row[a] for a in range(len(m)) if a != i] for row in m[1:]]
            #print n,len(m)
            if i % 2 == 0:
                s+= m[0][i]*determinant(n)
            else:
                s-= m[0][i]*determinant(n)
    return s
def trace(m):
    if len(m)!=len(m[0]):
        print 'make sure what you input is a square matrix'
    trace=0
    for i in range(len(m)):
        trace+=m[i][i]
    return trace
def add(m,n):
    res=[]
    if len(m)!=len(n) and len(m[0])!=len(n[0]):
        print 'make sure the matrices are addable'
    for i in range(len(m)):
        tmp=[]
        for j in range(len(m[0])):
            tmp.append(m[i][j]+n[i][j])
        res.append(tmp)
    return res
def multiply(m,n):
    #compute the multiply of m,n
    #m*n
    res=[]
    if len(m[0])!=len(n):
        print 'make sure two matrices are multipliable'
    for i in range(len(m)):
        tmp=[]
        for j in range(len(n[0])):
            s=0
            for k in range(len(m[0])):
               s+=m[i][k]*n[k][j]
            tmp.append(s)
        res.append(tmp)
    return res
def conv(m,n):
    res=[]
    if len(m[0])!=len(n[0]) and len(m)!=len(n):
        print 'make sure two matrices are convable'
    for i in range(len(m)):
        tmp=[]
        for j in range(len(m[0])):
            tmp.append(m[i][j]*n[i][j])
        res.append(tmp)
    return res
m2 = [ [1,2,3],[3,4,5],[7,8,9]]
matrix=np.mat(m2)
'''
the size of a matrix
the determinant of a matrix
the transpose of a matrix
the trace of a matrix
'''
print matrix.shape
print determinant(m2)
print np.linalg.det(m2)
print matrix.T
print transpose(m2)
print matrix.trace()
print trace(m2)
"""
the opertion of two matrices
add 
multiplt
conv
"""
m1=[[1,2,3],[2,3,4]]
n1=[[1,2],[3,4],[5,6]]
#print multiply(m1,n1)
#print conv(m1,n1)
#print trace(m2)

