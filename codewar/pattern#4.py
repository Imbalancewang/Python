def pattern(n):
    if n<=0:
        print ''
        return
    else:
        x=1
        for x in range(1,n+1):
            y=x
            for y in range(x,n+1):
                print y,
                y+=1
            print


n=raw_input()
pattern(int(n))
