from sys import stdout
n = int(raw_input("input number:\n"))
print "n = %d" % n

for i in range(2,n + 1):
    while n != i:
        if n % i == 0:
            stdout.write(str(i))
            stdout.write("*")
            n = n / i
        else:
            break
print "%d" % n