# -*- coding: utf-8 -*-
# @Time    : 2017/12/16 19:32
# @Author  : Matthew
# @Site    : 
# @File    : randomscore.py
# @Software: PyCharm
import xlwt,random,xlrd
import sys
from xlutils.copy import copy
reload(sys)
sys.setdefaultencoding('utf8')
def Excel_Read(file='score.xls'):
    try:
        data=xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
def Excel_Getrandomscore(file,name='matthew.xls'):
    data=Excel_Read(file)
    table=data.sheet_by_index(0)
    nrows=table.nrows
    ncols=table.ncols
    score=[]
    for i in range(1,nrows):
        temp=[]
        for j in range(0,4):
            temp.append(random.randint(16,19))
        for k in range(0,2):
            temp.append(random.randint(8,10))
        full=sum(temp)
        temp.append(full)
        score.append(temp)
    return score,nrows,ncols
def Excel_write(file,score,nrows,ncols):
    rb = xlrd.open_workbook('score2.xls')
    rs = rb.sheet_by_index(0)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    for i in range(3,nrows):
        if i!=9 and i!=10 and i!=23:
            for j in range(2,ncols):
                ws.write(i,j,score[i-3][j-2])
    #ws.write(nrows,ncols,'ds')
    wb.save('贾昌民信计1501 2015016523.xls')
if __name__ == '__main__':
    #data=Excel_Read('score2.xls')
    file='score2.xls'
    score,nrows,ncols=Excel_Getrandomscore(file)
    Excel_write(file,score,nrows,ncols)
    #print score[1]
    #print nrows,ncols
    #print len(score)
    #print len(score[1])
