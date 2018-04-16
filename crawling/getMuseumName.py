# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 22:16
# @Author  : Matthew
# @Site    : 
# @File    : getMuseumName.py
# @Software: PyCharm
import urllib2,urllib,urlparse,re,xlwt
import sys,time,socket
from bs4 import BeautifulSoup
from datetime import datetime
#reload(sys)
#sys.setdefaultencoding('utf8')
#socket.setdefaulttimeout(60)
def download(url,user_agent='matthew',num_tries=2):
    print 'Downloading:',url
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    headers={'User_agent':user_agent}
    request=urllib2.Request(url)
    try:
        html=urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Downloading error:',e.reason
        html=None
        if num_tries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                return download(url,user_agent,num_tries-1)
    print 'Downloaded!'
    return html

def getTheName(html):
    soup=BeautifulSoup(html,'lxml')
    trs=soup.find_all('tr')
    ui=[]
    for tr in trs:
        for td in tr:
            ui.append(td.string)
    while None in ui:
        ui.remove(None)
    """
    for i in ui:
        if len(i)<=3:
            ui.remove(i）
    """
    return ui

def writeToFile(ui):
    file=open('/Users/rd/Desktop/Python/op.md','w')
    for i in ui:
        file.write(i.encode('utf-8'))
        file.write('\n')

if __name__=='__main__':
    url='https://baike.baidu.com/item/国家一级博物馆/1372604?fr=aladdin'
    html=download(url)
    ui=getTheName(html)
    writeToFile(ui)

