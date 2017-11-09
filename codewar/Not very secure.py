# written by matthew
import re
def alphanumeric(string):
    if len(string)==0:return False
    if len(re.findall('[^0-9a-zA-Z]',string)):return False
    else:return True
print alphanumeric("Pfds)")