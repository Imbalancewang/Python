def green(n):
    res=[1,5,6]
    m,q=5,6
    while len(res)<=n:
        i=1
        while True:
            coefm=10**(len(str(m)))
            sm=m+coefm*i
            if sm**2%10**(len(str(sm)))==sm:
                break
            i=i+1
        j=1
        while True:
            coefq=10**(len(str(q)))
            sq=q+coefq*j
            if sq**2%10**(len(str(sq)))==sq:
                break
            j=j+1
        if sm<sq:
            res.append(sm)
            m=sm
        else:
            res.append(sq)
            q=sq
    return res
print green(10)