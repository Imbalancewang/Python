def solution(roman):
    item=[('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000)]
    d=dict(item)
    s=0
    for i in range(len(roman)):
        if i==len(roman)-1 or d[roman[i]]>=d[roman[i+1]]:
            s+=d[roman[i]]
        else:
            s-=d[roman[i]]
    return s
print solution('IX')
