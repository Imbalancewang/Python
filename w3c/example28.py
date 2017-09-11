def cal(n):
    if n==1:
        return 10
    else:
        return cal(n-1)+2
print cal(5)