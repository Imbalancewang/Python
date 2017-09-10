n=int(raw_input('please input n\n'))
a=int(raw_input('please input a\n'))
p=0
su=0
for i in range(1,n+1):
    p=p*10+a
    su=su+p
print su