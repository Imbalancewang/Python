while 1:
    a,b=raw_input().split(' ')
    a=int(a)
    b=int(b)
    if a or b:
        print abs(a-b)
    else:
        break
