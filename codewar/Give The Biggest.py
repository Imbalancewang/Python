import math
def is_prime(m):
    for i in range(2,int(math.sqrt(m)+1)):
        if m%i==0:
            return 0
    return 1
def big_primefac_div(n):
    if isinstance(n,float) and n!=int(n):
        return "The number has a decimal part. No Results"
    num,flag,sign=int(abs(n)),1,1
    if is_prime(num):
        return []
    factor=[]
    while True:
        for i in range(2,num/2+1):
            if num%i==0:
                factor.append(i)
                num=num/i
                break
        if is_prime(num):
            factor.append(num)
            break
    big_div=1
    for x in factor:
        big_div=big_div*x
    big_div=big_div/factor[0]
    for x in factor[::-1]:
        if is_prime(x):
            big_prime=x
            break
    return [big_prime,big_div]
print big_primefac_div( 8398653)

