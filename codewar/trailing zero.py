# written by matthew
# modify the primelist to minimize the memory
import math
def isPrime(n):
    return not [i for i in range(2, int(math.sqrt(n)) + 1) if n%i == 0]
def createPrime(n):
    res,num,primelist=(n+1)*[1],range(n+1),[]
    for i in range(2,n+1):
        j=2*i
        while j<=n:
            res[j]=0
            j+=i
    for i in range(2,n+1):
        if res[i]*num[i]:
            primelist.append(res[i]*num[i])
    return primelist
def findfactor(n):
    factor=createPrime(n)
    num,base=len(factor)*[0],n
    for i in range(len(factor)):
        if base<=1:break
        while True:
            if base%factor[i]!=0:break
            else:
                base/=factor[i]
                num[i]+=1
    return num
def trailing_zeros(num, base):
    primeindex,primelist=findfactor(base),createPrime(base)
    res=[]
    for i in range(len(primeindex)):
        n,sign=num,0
        if primeindex[i]>0:
            while n>0:
                n=n/primelist[i]
                sign+=n
            sign=sign/primeindex[i]
            res.append(sign)
    return min(res)
print trailing_zeros(900719925474099100,100)