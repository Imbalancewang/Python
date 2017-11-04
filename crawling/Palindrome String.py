# written by matthew
def palindrome(n, c):
    return c+(n-2*len(c)+1)*c[-1]+c[1::-1]
string=palindrome(3,'ab')
print string
print len('def palindrome(n,c):return c+(n-2*len(c)+1)*c[-1]+c[1::-1]')