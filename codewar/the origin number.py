def original_number(s):
    #your code here
    flag,num=26*[0],10*[0]
    for i in range(len(s)):
        flag[ord(s[i])-65]=flag[ord(s[i])-65]+1
    print flag
    num[0]=flag[25]#0z
    num[6]=flag[23]#6x
    num[2]=flag[22]#2w
    num[8]=flag[6]#8g
    num[4]=flag[20]#4u
    num[5]=flag[5]-num[4]#f-4=5
    num[7]=flag[21]-num[5]#v-5=7
    num[3]=flag[7]-num[8]#h-8=3
    num[1]=flag[14]-num[0]-num[2]-num[4]
    num[9]=flag[8]-num[5]-num[6]-num[8]
    res,n='','0123456789'
    print num
    for i in range(10):
        res=res+num[i]*n[i]
    return res
print original_number("NINE")