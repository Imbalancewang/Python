ans=range(1,10002)
ans[1]=1
for x in xrange(2,10001):
    ans[x]=ans[x-1]*(x*4-2)/(x+1)
T=input()
while T:
    line=raw_input()
    n=int(line)
    T=T-1
    print ans[n]%10000009   

