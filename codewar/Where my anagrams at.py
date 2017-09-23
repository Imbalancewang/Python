def countword(string):
    res=26*[0]
    for i in range(len(string)):
        res[ord(string[i])-97]+=1
    return res
def anagrams(word, words):
    #your code here
    out=[]
    stand=countword(word)
    for x in words:
        if countword(x)==stand:
            out.append(x)
    return out
print anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])