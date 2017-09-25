# function for pentagonal numbers
def pent (n):     return int((0.5*n)*((3*n)-1))

# function for generalized pentagonal numbers
def gen_pent (n): return pent(int(((-1)**(n+1))*(round((n+1)/2))))
exp_sums = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
def exp_sum (k):
    if k<0:return 0
    else:
        if (k < len(exp_sums)): return exp_sums[k]
        total, sign, i = 0, 1, 1
        while (k - gen_pent(i)) >= 0:
            sign= (-1)**(int((i-1)/2))
            total+= sign*(exp_sum(k - gen_pent(i)))
            i+=1
        exp_sums.insert(k,total)
        return total
print exp_sum(-1)
