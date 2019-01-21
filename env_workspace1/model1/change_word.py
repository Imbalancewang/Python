# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 09:54
# @Author  : Matthew
# @Site    : 
# @File    : change_word.py
# @Software: PyCharm
import codecs

def change_label(filename,label,mark):
    with codecs.open(filename=filename,mode='w',encoding='utf-8') as fp:
        temp=[]
        for line in fp:
            lines = line.split('\t')
            category = lines[0].strip()
            text = lines[1].strip()
            temp.append()
