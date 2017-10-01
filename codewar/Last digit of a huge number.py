def last_digit1(n1, n2):
    n=n1%10
    if n2==0: return 1
    if n==0 or n==1 or n==5 or n==6:
        return n
    elif n==2 or n==3 or n==7 or n==8: return n**(n2%4+4)%10
    elif n==4 or n==9: return n**(n2%2+2)%10
def last_digit(lst):
    for i in range(len(lst)-1,0,-1):
        lst[i-1]=last_digit1(lst[i-1],lst[i])
    return lst
print last_digit([2,4])