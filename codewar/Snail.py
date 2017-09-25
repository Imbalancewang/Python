def snail(array):
    n,i,j=len(array),0,0
    res,tot=[],1
   # sym=[n*[1]]*n the wrong point!!!!!!!
    sym=[]
    for i in range(n):
        new=[]
        for j in range(n):
            new.append(1)
        sym.append(new)
    print sym
    i,j=0,0
    while tot<=n*n:
        while j+1<n and (sym[i][j+1] or tot==n*n):
            res.append(array[i][j])
            sym[i][j]=0
            j+=1
            tot+=1
        while i+1<n and (sym[i+1][j] or tot==n*n):
            res.append(array[i][j])
            sym[i][j]=0
            i+=1
            tot+=1
        while j-1>=0 and (sym[i][j-1] or tot==n*n):
            res.append(array[i][j])
            sym[i][j]=0
            j-=1
            tot+=1
        while i-1>=0 and (sym[i-1][j] or tot==n*n):
            res.append(array[i][j])
            sym[i][j]=0
            i-=1
            tot+=1
    return res
array = [[1,2,3,0],
         [4,5,6,10],
         [7,8,9,11],
         [12,13,14,15]]
print snail(array)
# time limited

