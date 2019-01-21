# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 15:08
# @Author  : Matthew
# @Site    : 
# @File    : function_test.py
# @Software: PyCharm
def strQ2B(ustring): # 全角转半角
    rstring = ''
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288: # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += unichr(inside_code)
    return rstring

if __name__=="__main__":
    print strQ2B(u'2000')