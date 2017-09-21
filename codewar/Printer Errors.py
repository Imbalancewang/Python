def printer_error(s):
    # your code
    flag=26*[0]
    a_m=0
    for i in range(len(s)):
        flag[ord(s[i])-97]+=1
    letter_sum=sum(flag)
    a_m=sum(flag[0:13])
    str='%d'%a_m+'/'+'%d'%letter_sum
    return str