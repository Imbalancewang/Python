def prime(n):
    for i in range(2,n/2+1):
        if n%i==0:
            return 1
    else:
        return 0
for i in range(100,201):
    if prime(i)==0:
        print i
