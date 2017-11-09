# written by matthew
def elder_age(m,n,l,t):
    return (m-1)*(m-2*l)/2*n%t
print elder_age(5,45,3,1000007)