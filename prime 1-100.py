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
#N = int(input('��������Ҫ�����������ĸ���: '))
#��3��ʼ����N-1����һ�Ƚϣ�����checkS
for i in range(3,N,2):
    checkS(i,s)
#print(s)
print(' '.join(str(k) for k in s)) 
