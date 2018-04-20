# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 15:01
# @Author  : Matthew
# @Site    : 
# @File    : changetocsv.py
# @Software: PyCharm
import csv,json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def writeToCsv(path):
    fp=open(path,'rb')
    data=json.load(fp)
    return data
if __name__=="__main__":
    path='/Users/rd/Desktop/Python/crawling/museumIntroduction.json'
    data=writeToCsv(path)
    print data
