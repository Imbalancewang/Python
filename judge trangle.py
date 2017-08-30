#a,b,c=input()
def judge(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        print 'YES'
    else:
        print 'NO'
judge(a,b,c)
