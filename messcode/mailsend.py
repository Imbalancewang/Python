# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 21:47
# @Author  : Matthew
# @Site    : 
# @File    : mailsend.py
# @Software: PyCharm
import smtplib
import urllib,urllib2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'wb2847@163.com'
password = 'wb284745'
to_addr = '530514447@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEMultipart()
msg['From'] = _format_addr(u'Matthew <%s>' % from_addr)
msg['To'] = _format_addr(u'wong <%s>' % to_addr)
msg['Subject'] = Header(u'王滨', 'utf-8').encode()
msg.attach(MIMEText('send with files','plain','utf-8'))


xlsxpart=MIMEApplication(open('/Users/rd/Desktop/Python/messcode/王滨信计1501 2015016503.xls','rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment',filename='王滨信计1501 2015016503.xls')
msg.attach(xlsxpart)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()