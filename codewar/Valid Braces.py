# -*- coding: utf-8 -*-
# @Time    : 2018/1/24 19:37
# @Author  : Matthew
# @Site    : 
# @File    : Valid Braces.py
# @Software: PyCharm
def validBraces(string):
    res=[]
    for x in range(len(string)):
        if(string[x]=='(' or string[x]=='[' or string[x]=='{'):
            res.append(string[x])
        else:
            if(len(res)==0):return False;
            elif(string[x]==')' and res.pop()=='('):pass;print res
            elif (string[x] == ']' and res.pop() == '['):pass;print res
            elif (string[x] == '}' and res.pop() == '{'):pass;print res
            else:print res;return False
    return (True if len(res)==0 else False)
print(validBraces("[({})](]"))
"""
def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0  
    
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s=='//got the point
  """