# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 17:39
# @Author  : Matthew
# @Site    : 
# @File    : chomd.py
# @Software: PyCharm
#the dictionary is unchangeable!!!!!
def strchangeint(string):
    s=0
    if('r'in string):s+=4
    if('w'in string):s+=2
    if('x'in string):s+=1
    return str(s)
def chmod_calculator(perm):
    string=''
    if(perm.get('user')==None):string+='0'
    else:string+=strchangeint(perm.get('user'))
    if(perm.get('group')==None):string+='0'
    else:string+=strchangeint(perm.get('group'))
    if(perm.get('other')==None):string+='0'
    else:string+=strchangeint(perm.get('other'))
    return string
    #your code here
print chmod_calculator({"user": 'rwx', "group": 'r-x', "other": 'r-x'})
print chmod_calculator({"group": 'rwx'})
print chmod_calculator({"user": 'r-x', "group": 'r-x', "other": '---'})


def chmod_calculator(perm):
    perms = {"r": 4, "w": 2, "x": 1}
    value = ""
    for permission in ["user", "group", "other"]:
        value += str(sum(perms.get(x, 0) for x in perm.get(permission, "")))

    return value