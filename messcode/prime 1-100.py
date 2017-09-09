def checkS(num,s):
    f = 0
    for i in range(len(s)):
        if(num % s[i] == 0):
            f = 1
            break
        if(s[i]*s[i] > num):
            break
    if(f == 0):
        s.append(num)

N = 100
s = [2,]
#print(s)
#N = int(input('请输入需要产生的素数的个数: '))
#从3开始，到N-1，逐一比较，调用checkS
for i in range(3,N,2):
    checkS(i,s)
#print(s)
print(' '.join(str(k) for k in s)) 
