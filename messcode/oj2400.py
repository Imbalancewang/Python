n=input()
cnt=0
last=1
while(n):
    t=n
    while(t%5==0):
        t=t/5
        cnt=cnt+1
    last=last*n
    while(last%10==0):
        last=last/10
    last=last%10000
    n=n-1
last=last%10
print last,cnt
        
