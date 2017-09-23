def snail(array):
    n,i,j=len(array),0,0
    res,tot=[],1
    sym=[n*[1]]*n
    while tot<n*n:
        while j<n-1 and sym[i][j+1]:
            if sym[i][j]==1:
                res.append(array[i][j])
                sym[i][j]=0
                tot+=1
            j+=1
        print sym
        print res
        while i<n-1 and sym[i+1][j]:
            print 'second'
            if sym[i][j]==1:
                res.append(array[i][j])
                sym[i][j] = 0
                tot+=1
            i+=1
            print 'damn'
        while j>=0 and sym[i][j-1]:
            print 'third'
            if sym[i][j]==1:
                res.append(array[i][j])
                sym[i][j] = 0
                tot+=1
            j-=1
            print j
        while i>=0 and sym[i-1][j]:
            if sym[i][j]==1:
                res.append(array[i][j])
                sym[i][j] = 0
                tot+=1
            i-=1
            print i
    return res
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print snail(array)

