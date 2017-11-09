import re
def find_codwars(url):
    #your code here
    pattern='(?!=codewar.com)(\.|//)codwars\.com'
    if len(re.findall(pattern,url)):return True
    else:return False
print find_codwars("codewars.com.codwars.com")
