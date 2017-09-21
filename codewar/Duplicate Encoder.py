def duplicate_encode(word):
    #your code here
    #string=word.lower()
    symbol=300*[0]
    result=''
    for i in range(len(word)):
        symbol[ord(word[i])]+=1
    for i in range(len(word)):
        if symbol[ord(word[i])]>1:
            result+=')'
        else:
            result+='('
    return result
print duplicate_encode('Success')
