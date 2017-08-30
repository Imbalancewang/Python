flag = 1
for i in range(-10000,10001):
    if i * (a - i) == b:
        print "Yes"
        flag = 0
        break
if flag == 1: 
    print "No
