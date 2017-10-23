# written by matthew
def dbl_linear(n):
    res,i,j,length=[1],0,0,1
    while length<=n:
        x,y=2*res[i]+1,3*res[j]+1
        if x<y:
            res.append(x)
            i+=1
            length+=1
        elif x>y:
            res.append(y)
            j+=1
            length+=1
        else:
            res.append(x)
            i,j=i+1,j+1
            length+=1
    return res[n]
print dbl_linear(50)

