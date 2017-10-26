# written by matthew
def gcd(a,b):
    if b==0: return a
    else:return gcd(b,a%b)
def solution(a):
    if len(a)==1:return a[0]
    elif len(a)==2:return gcd(a[0],a[1])*2
    else:
        y=gcd(a[0],a[1])
        for n in range(2,len(a)):
            if y==1:return len(a)
            elif a[n]%y==0:pass
            elif y%a[n]==0:y=a[n]
            else:y=gcd(y,a[n])
    return y*len(a)
print solution([36,39,21,24])