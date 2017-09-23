def solution(n):
    # TODO convert int to roman string
    item = [(1,'I'), (5, 'V'), (10,'X'), (50,'L'), (100,'C'), (500,'D'), (1000,'M')]
    d = dict(item)
    res,i=[],0
    while n>0:
        flag=n%10
        if flag<=3:
            res.append(flag*d[10**i])
        elif flag==4:
            res.append(d[10**i]+d[5*10**i])
        elif flag==5:
            res.append(d[10**i*5])
        elif flag>5 and flag<=8:
            res.append(d[5*10**i]+(flag-5)*d[10**i])
        elif flag==9:
            res.append(d[10**i]+d[10*i**10])
        else:
            pass
        n=n/10
        i+=1
    str=''
    for x in res[::-1]:
        str+=x
    return str
print solution(1666)