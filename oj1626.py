while 1:
    n=input()
    s=1
    if n==-1: break
    else:
        for i in range(1,n+1):
            s=s*i
        ch=str(s)
        ch=ch.replace('0',' ')
        ch=ch.strip()
        ch=ch.replace(' ','0')
        ch=int(ch)%(10**18)
        ch=str(ch)
        lenth=len(ch)
        k=18-lenth
        ch=int(ch)
        if lenth==18: print ch
        else:
            print ' '*(k)+'%d'%ch
