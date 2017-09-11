def factorial(n):
    s=1
    if n==0 or n==1:
        return 1
    else:
        for i in range(1,n+1):
            s=s*i
    return s
a=0
for i in range(21):
    a+=factorial(i)
print a