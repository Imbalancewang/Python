# written by matthew
def get_array(limit,*args):
    res=[]
    for i in range(len(str(max(args)))):
        for j in range(len(args)):
            if i>len(str(args[j]))-1:pass
            else:
                if int(str(args[j])[i]) not in res:
                    res.append(int(str(args[j])[i]))
    print res[:]
    return res[:limit]
def permutation(n,m):
    res=1
    for i in range(m):
        res=res*n
        n=n-1
    return res
def gta(limit, *args):
    res=get_array(limit,*args)
    sum_res=0
    for i in range(1,limit+1):
        sum_res+=sum(res)*permutation(limit,i)*i/len(res)
    return sum_res
print gta(8, 12348, 47, 3639)
