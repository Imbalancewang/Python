def determinant(m):
    if len(m) <= 0:
        return None
    if len(m) == 1:
        return m[0][0]
    else:
        s = 0
        for i in range(len(m)):
            n = [[row[a] for a in range(len(m)) if a != i] for row in m[1:]]
            print n,len(m)
            if i % 2 == 0:
                s += m[0][i] * determinant(n)
            else:
                s -= m[0][i] * determinant(n)
        return s
m2 = [ [1,2,3],[3,4,5],[7,8,9]]
print determinant(m2)

