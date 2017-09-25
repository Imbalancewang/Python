def exp_sum(n):
    if n < 0:
        return 0
    dp=[1]+[0]*n
    for num in xrange(1,n+1):
        for i in xrange(num,n+1):
            dp[i] += dp[i-num]
    print dp
   # return dp[-1]
print exp_sum(5)