def iq_test(numbers):
    #your code here
    str=numbers.split(' ')
    a=[0]*len(str)
    for i in range(len(str)):
        if int(str[i])%2:
            a[i]=1
    if a[0]!=a[1] and a[0]!=a[2]:
        return 1
    elif a[0]!=a[1] and a[0]==a[2]:
        return 2
    elif a[len(str)-1]!=a[len(str)-2] and a[len(str)-1]!=a[len(str)-3]:
        return len(str)
    elif a[len(str)-1]!=a[len(str)-2] and a[len(str)-1]==a[len(str)-3]:
        return len(str)-1
    else:
        for i in range(1,len(str)):
            if a[i]!=a[i-1] and a[i]!=a[i+1]:
                return i+1



