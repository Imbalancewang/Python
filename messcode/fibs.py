def fibs(n):
    fibs=[1,1]
    for i in range(1,n-1):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
while 1:
    m=input()
    n=10001
    if m!=0:
        a=fibs(n)
        print a[m-1]
    else:
        break
