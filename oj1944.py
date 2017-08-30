a,b,k,n,m= raw_input().split(' ')
a = (int)(a)
b = (int)(b)
k=(int)(k)
n=int(n)
m=int(m)
s=1
def JC(k,n):
    p=1
    for i in range(1,n+1):
        p=p*k/i
        k=k-1
    return p
s=JC(k,n)*b**(n)*a**(k-n)%10007
print s

