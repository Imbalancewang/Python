# -*- coding: utf-8 -*-
# @Time    : 2017/11/11 14:32
# @Author  : Matthew
# @Site    : 
# @File    : datadig.py
# @Software: PyCharm Community Edition
import itertools
new_iter=itertools.ifilter(lambda x:x%2==0,[1,2,3,4,5])
for i in new_iter:
    print i,