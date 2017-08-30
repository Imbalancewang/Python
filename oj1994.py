n,k=raw_input().split(' ')
def JC(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
s=JC(n)
s=str(s)
lenth=len(s)
if lenth<=k: print s
