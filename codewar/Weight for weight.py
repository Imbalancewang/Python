def cal(n):
    he=0
    num=0
    for i in range(len(n)):
        num+=(ord(n[-1+i])-48)*(10**i)
    while num:
        he+=num%10
        num/=10
    return he
def order_weight(string):
    res=''
    str=string.split(' ')
    s=[cal(x) for x in str]
    for i in range(len(str)):
        for j in range(len(str)):
            if cal((str[i]))<cal((str[j])):
                str[i],str[j]=str[j],str[i]
            elif cal((str[i]))==cal((str[j])) and str[i]<str[j]:
                str[i],str[j] = str[j],str[i]
            else:
                pass
    for i in str:
        res=res+i+' '
    return res.strip()
print order_weight("103 123 4444 99 2000")

