from math import sqrt
n=1
while 1:
    if sqrt(n+100)==int(sqrt(n+100)) and sqrt(n+268)==int(sqrt(n+268)):
        print n
        break
    else:
        n=n+1