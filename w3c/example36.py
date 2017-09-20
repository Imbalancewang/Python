from math import sqrt
def is_prime(n):
    flag=1
    if n>2:
        for i in range(2,n-1):#how
            if n%i==0:
                return ~flag
        return flag
    else:
        return flag

for i in range(2,100):
    if is_prime(i)==1:
        print i