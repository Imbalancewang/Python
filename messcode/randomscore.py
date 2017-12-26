# -*- coding: utf-8 -*-
# @Time    : 2017/12/16 19:32
# @Author  : Matthew
# @Site    : 
# @File    : randomscore.py
# @Software: PyCharm
import smtplib
import xlwt,random,xlrd
import sys
from xlutils.copy import copy
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.utils import parseaddr, formataddr
reload(sys)
sys.setdefaultencoding('utf8')
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))
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
    rb = xlrd.open_workbook('score3.xls')
    rs = rb.sheet_by_index(0)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    for i in range(3,nrows):
        if i!=4 and i!=7 and i!=8 and i!=18 and i!=19 and i!=21 and i!=24:
            for j in range(2,ncols):
                ws.write(i,j,score[i-3][j-2])
    #ws.write(nrows,ncols,'ds')
    wb.save('王天昊金数1501 2015016502.xls')
if __name__ == '__main__':
    #data=Excel_Read('score2.xls')
    file='score3.xls'
    score,nrows,ncols=Excel_Getrandomscore(file)
    Excel_write(file,score,nrows,ncols)
    #print score[1]
    #print nrows,ncols
    #print len(score)
    #print len(score[1])
    from_addr = 'wb2847@163.com'
    password = 'wb284745'
    to_addr = '530514447@qq.com'
    smtp_server = 'smtp.163.com'

    msg = MIMEMultipart()
    msg['From'] = _format_addr(u'Matthew <%s>' % from_addr)
    msg['To'] = _format_addr(u'wong <%s>' % to_addr)
    msg['Subject'] = Header(u'王天昊', 'utf-8').encode()
    msg.attach(MIMEText('send with files', 'plain', 'utf-8'))

    xlsxpart = MIMEApplication(open('/Users/rd/Desktop/Python/messcode/王天昊金数1501 2015016502.xls', 'rb').read())
    xlsxpart.add_header('Content-Disposition', 'attachment', filename='王天昊金数1501 2015016502.xls')
    msg.attach(xlsxpart)

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
