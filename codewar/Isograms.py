def is_isogram(string):
    # your code here
    flag = 26 * [0]
    str = string.lower()
    for i in range(len(str)):
        flag[ord(str[i]) - 97] += 1
    for i in range(26):
        if flag[i] > 1:
            return False
    return True
