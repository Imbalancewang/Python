def tickets(people):
    a=0
    b=0
    for i in range(len(people)):
        if people[i]==25 and a>=0:
            a+=1
        elif people[i]==50 and a>=0:
            a-=1
            b+=1
        elif people[i]==100 and b<=0:
            a-=3
            if a<0:
                return "NO"
        elif people[i]==100 and b>=1:
            b-=1
            a-=1
            if a<0:
                return "NO"
        else:
            return "NO"
    if a>=0 and b>=0:
        return "YES"
    else:
        return "NO"
print tickets([25,50,50,100,25])
