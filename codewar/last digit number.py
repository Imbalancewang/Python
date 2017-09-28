def last_digit(n1, n2):
    n=n1%10
    if n2==0: return 1
    if n==0 or n==1 or n==5 or n==6:
        return n
    elif n==2 or n==3 or n==7 or n==8: return n**(n2%4+4)%10
    elif n==4 or n==9: return n**(n2%2+2)%10
print last_digit(8785429106637673519580886248798247313189427209066208741672,1216974469715313690100174048115255586827834045132106940316)