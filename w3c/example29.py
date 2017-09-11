num=raw_input('please input the number')
l=len(num)
list=[]
for i in range(l):
    list.append(num[l-i-1])
print l,list