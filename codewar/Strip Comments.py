def solution(string,markers):
    flag=1
    res=''
    for i in range(len(string)):
        if flag==1 and string[i] not in markers:
            res+=string[i]
        elif string[i] in markers:
            flag=0
        elif string[i:i+2]=='\n':
            flag=1
        else:
            pass
    return res
print solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
#apples, pears\ngrapes\nbananas
