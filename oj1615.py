ans=range(1,10003)
ans[1]=1
ans[2]=1
for x in range(3,10002):
    ans[x]=ans[x-1]+ans[x-2]
while True:
    m=raw_input()
    n=int(m)
    if n==0:
        break
    else:
        print '%d \n'%ans[n]
