def coun(a):
    s=0
    while a>0:
       s=s+a%2
       a=a/2
    return s
#a=input()
p=coun(a)
print p
