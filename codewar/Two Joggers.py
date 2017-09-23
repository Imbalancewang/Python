def gcd(a , b):
    return b if a%b==0 else gcd(b,a%b)
def nbr_of_laps(x, y):
    return [x*y/gcd(x,y)/x,x*y/gcd(x,y)/y]
print nbr_of_laps(6,4)