def fibs(n):
    fib=[1,1]
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        for i in range(3,n+1):
            fib.append(fib[-1]+fib[-2])
        return sum(fib)
n=int(raw_input("please"))
print(fibs(n))
