def checkchoose(m, n):
    # your code
    max=n/2+1
    sum=1.0
    while sum<m:
        max=max-1
        sum=1.0
        mm, nn = m, n
        for i in range(max):
            sum=sum*mm/nn
            nn-=1
            mm-=1
        if max<1:
            return -1
    return max
print checkchoose(6,4)
