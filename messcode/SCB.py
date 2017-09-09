a,b=input()
def gcd(a , b):
    return b if a%b==0 else gcd(b,a%b)
print a*b/gcd(a,b)
