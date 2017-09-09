a,b=input()
import math
if a > b:
    a, b = b, a
p = b / a
for i in range(1, int(math.sqrt(p)) + 1):
    if p % i == 0:
        f1, f2 = i, p / i
print f1 * a, f2 * a

