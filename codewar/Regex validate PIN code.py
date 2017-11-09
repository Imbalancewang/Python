# written by matthew
import re
def validate_pin(pin):
    #return true or false
    if len(re.findall('^[0-9]{4}$|^[0-9]{6}$',pin)):return True
    else:return False
print validate_pin('123456')
#return bool(re.match(r'^(\d{4}|\d{6})$', pin))