s=0.0
a=2.0
b=1.0
for i in range(1,21):
    s+=a/b
    c=a
    a=a+b
    b=c
print s