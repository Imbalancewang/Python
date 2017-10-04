def solve_runes(runes):
    equal=runes.index('=')
    sym='+-*'
    if '+' in runes:flag=0
    if '-' in runes:flag=1
    if '*' in runes:flag=2
    for i in range(0,10):
        if str(i) not in runes:
            test=runes.replace('?',str(i))
            if runes.index(sym[flag])!=1 and test[0]=='0':pass
            elif test[equal+1]=='0' and len(test[equal+1:])!=1:pass
            elif test[runes.index(sym[flag])+1]=='0' and len(test[runes.index(sym[flag])+1:equal])!=1:pass
            else:
                if str(eval(test[:equal]))==test[equal+1:]:
                    return i
    return -1
print solve_runes('?*32=?')