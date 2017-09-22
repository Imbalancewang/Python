def dig_pow(n, p):
    # your code
    num_len=len(str(n))
    num_sum=0
    num,k=n,num_len
    for i in range(num_len):
        num_sum+=(num%10)**(k+p-1)
        k-=1
        num/=10
        #print num_sum
    if num_sum%n==0:
        return num_sum/n
    else:
        return -1
print dig_pow(2,3)