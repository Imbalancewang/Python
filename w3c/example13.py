def shu(n):
    a=n%10
    b=n/10%10
    c=n/100
    if a**3+b**3+c**3==n:
        return 1
    else:
        return 0
for i in range(100,1000):
    if shu(i)==1:
        print i