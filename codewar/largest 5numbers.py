def solution(digits):
    digits=str(digits)
    res=digits[:5]
    for i in range(1,len(digits)-4):
        if digits[i]>res[0]:
            res=digits[i:i+5]
        elif digits[i]==res[0]:
            if digits[i+1]>res[1]:
                res=digits[i:i+5]
            elif digits[i+1]==res[1]:
                if digits[i+2]==res[]
    return 0;