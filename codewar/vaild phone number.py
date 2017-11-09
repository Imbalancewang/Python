# written by matthew
import re
def validPhoneNumber(phoneNumber):
    return bool(re.match(r'\(\d{3}\) \d{3}-\d{4}',phoneNumber))
print validPhoneNumber('(124)  900-2345')