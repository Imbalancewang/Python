import itertools
def permutations(string):
    #your code here
    str=list(itertools.permutations(string, len(string)))
    res=[]
    for x in str:
        res.append(''.join(x))
    res=list(set(res))
    return res
print permutations('aabb')