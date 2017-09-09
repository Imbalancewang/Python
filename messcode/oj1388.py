ans=range(1,30)
ans[1]=1
for x in xrange(2,25):
    ans[x]=ans[x-1]*(x*4-2)/(x+1)
while True:
    line=raw_input()
    n=int(line)
    try:
        print ans[n]%10000009    
    except EOFError:
        break
