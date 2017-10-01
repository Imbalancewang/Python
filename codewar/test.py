import sys
def prime(n):
    flag = [1]*(n+2)
    p,res=2,[]
    while(p<=n):
        res.append(p)
        for i in xrange(2*p,n+1,p):
            flag[i] = 0
        while 1:
            p += 1
            if(flag[p]==1):
                break
    return res[-1]
print prime(2799553)