# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 15:13
# @Author  : Matthew
# @Site    : 
# @File    : StripComments.py
# @Software: PyCharm
"""
Strip Comments
"""
import re
def solution(string,markers):
    result=[]
    seq=''
    for x in markers:seq+=x+'|'
    seq=seq[:-1]
    return re.split(seq,string)
    #your code here

if __name__=="__main__":
    pass

