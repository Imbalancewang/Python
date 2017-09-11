def reverse_number(n):
    length=len(n)
    for i in range(length):
        if n[i]!=n[length-1-i]:
            return False
    return True
str=raw_input('please input the number\n')
if reverse_number(str):
    print 'reverse number'
else:
    print 'none'