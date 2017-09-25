def sum_for_list(lst):
    prime=[]
    for i in lst:
        j=2
        while 1:
            if i==1 or i==-1:
                break
            else:
                if i%j==0:
                    if j not in prime:
                        prime.append(j)
                        i/=j
                    else:
                        i/=j
                else:
                    j+=1
    prime.sort()
    res=[]
    for x in prime:
        s,every=0,[]
        every.append(x)
        for y in lst:
            if y%x==0:s+=y
            else:pass
        every.append(s)
        res.append(every)
    return res
print sum_for_list([15,30,-45])
