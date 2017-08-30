c=min(a,b)
s=0
for i in range(1,c+2):
    if a%i==0 and b%i==0:
        s=s+1
    if i==c+1:
        print s 

