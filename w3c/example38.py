a=[]
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(int(raw_input('%d'%(3*i+j))))
for i in range(3):
    for j in range(3):
        print a[i][j],
    print
sum=0
for i in range(3):
    sum+=a[i][i]
print sum