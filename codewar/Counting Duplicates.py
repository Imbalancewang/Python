def duplicate_count(text):
    # Your code goes here
    string=text.lower()
    num=10*[0]
    letter=26*[0]
    count=0
    for i in range(len(string)):
        if string[i].isalpha():
            letter[ord(string[i])-97]+=1
        else:
            num[ord(string[i])-48]+=1
    for i in range(26):
        if letter[i]>1:
            count+=1
    for i in range(10):
        if num[i]>1:
            count+=1
    return count
print duplicate_count('lklklsss')