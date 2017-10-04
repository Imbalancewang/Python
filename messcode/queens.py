def conflict(state,nextx):
    nexty=len(state)
    for i in range(nexty):
        if abs(state[i]-nextx) in (0,nexty-i):
            return True
    return False #understood
def queens(num=8,state=()):
    for pos in range(num):#the last position
        if not conflict(state,pos):
            if len(state)==num-1:
                yield (pos,)
            else:
                for result in queens(num,state+(pos,)):#tuple type
                    yield (pos,)+result
print len(list(queens(11)))