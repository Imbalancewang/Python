def fib(n):
    fib=[1,1]
    if n==0 or n==1:
        return 1
    else:
        for i in range(2,n):
            fib.append(fib[-1] + fib[-2])
        return fib
n=int(raw_input("please input n\n"))
print(fib(n))