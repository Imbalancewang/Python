def grade(n):
    if n>=90:
        return 'A'
    elif n>=60 and n<90:
        return 'B'
    else:
        return 'C'
score=int(raw_input('please input the score\n'))
print grade(score)