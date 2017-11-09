# written by matthew
import re
def remove_chars(s):
    pattern='[a-zA-Z\s]'
    str=''
    for x in re.findall(pattern,s):
        print x
        str+=x
    return str
print remove_chars('0123456789(.)+,|[]{}=@/~;^$<>?-!*&:#%_')
#re.sub(r'[^A-Za-z\s]','',s)
#re.sub('(?i)[^a-z ]', '', s)