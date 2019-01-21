# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 10:00
# @Author  : Matthew
# @Site    : 
# @File    : Binomial Expansion.py
# @Software: PyCharm
import operator
import string
def combination(n,k):
    return reduce(operator.mul, range(n - k + 1, n + 1)) /reduce(operator.mul, range(1, k +1)) if k>0 else 1
def expand(expr):
    all_letters=string.letters
    x=filter(lambda y:y in all_letters,expr)
    n=int(expr[expr.index('^')+1:])
    if n == 0: return '1'
    ta=(expr[expr.index('(')+1:expr.index(x)])
    if ta=='':
        a=1
    elif ta=='-':
        a=-1
    else:
        a=int(ta)
    b=int(expr[expr.index(x)+1:expr.index(')')])
    res=''
    if combination(n,0)*a**n!=1 and a**n!=-1:
        res+=str(combination(n,0)*a**n)
    if a**n==-1:
        res+='-'
    if n!=1:
        res = res + x + '^' + str(n)
    else:
        res=res+x
    for i in range(n-1,0,-1):
        temp=combination(n,i)*b**(n-i)*a**i
        if temp > 0 and i != n: res += '+'
        if temp==0:continue
        res+=str(temp)
        if i!=1:
            res=res+x+'^'+str(i)
        else:
            res+=x
    if n>=1 and b**n>0:res+='+'
    if b!=0:res+=str(b**n)
    return res
    pass

#8x^3-36x^2+54x-27
if __name__=="__main__":
    print expand('(-s-1)^2')
