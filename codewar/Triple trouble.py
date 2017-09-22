def triple_double(num1, num2):
    #code me ^^
    a=10*[0]
    b=10*[0]
    n1,n2=num1,num2
    while(n1):
        a[n1%10]+=1
        n1=n1/10
    while(n2):
        b[n2%10]+=1
        n2=n2/10
    for i in range(10):
        if a[i]>=3 and b[i]>=2:
            return 1
    return 0
print triple_double(1222345, 12345)