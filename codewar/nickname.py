# written by matthew
import re
def nickname_generator(name):
    if len(name)<4:return "Error: Name too short"
    pattern='^[A-Z][a-z][aeiou][a-z]|^[A-Z][a-z]{2}'
    return re.findall(pattern,name)[0]
print nickname_generator('Kimberly')

