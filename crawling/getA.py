# -*- coding: utf-8 -*-
# @Time    : 2018/4/6 22:06
# @Author  : Matthew
# @Site    :
# @File    : getBasicInformation.py
# @Software: PyCharm
import urllib2,urllib,urlparse,re,xlwt
import sys,time,socket
from bs4 import BeautifulSoup
from datetime import datetime
import json
reload(sys)
sys.setdefaultencoding('utf8')
#socket.setdefaulttimeout(60)
def download(url,user_agent='matthew',num_tries=2):
    """
    :param url: to be determined
    :param user_agent: to consider the ip pour
    :param num_tries: 2
    :return: html
    """
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

def readCreateTheURL(name):
    ff=open(name,'rb')
    MuseumName=ff.readlines()
    basic_url = 'https://baike.baidu.com/item/'
    url=[]
    for i in MuseumName:
        url.append(basic_url+i)
    return url

def getBasicInformation(html):
    """
    dict(zip(key,values))
    to form a json data
    key=dts
    values=dds
    """
    res=[]
    soup=BeautifulSoup(html,'lxml')
    tmpdds,tmpdts=[],[]
    dts=soup.find_all('dt','basicInfo-item name')
    dds=soup.find_all('dd','basicInfo-item value')
    for i in dds:
        #print i.get_text()
        tmpdds.append(i.get_text().replace('\n',''))
    for j in dts:
        #print j.get_text()
        tmpdts.append(j.get_text().replace('\n',''))
   # print tmpdds
    if len(dds)<3:print 'it is blank'
    res.append(dict(zip(tmpdts,tmpdds)))
    return res

def writeToJson(res=[]):
    fp=open('/Users/rd/Desktop/Python/crawling/testt.json','w+')
    json.dump(res,fp,ensure_ascii=False)
    fp.write('\n')
    fp.close()
    return

if __name__=='__main__':
    museumName_location='/Users/rd/Desktop/Python/test.md'
    #url=readCreateTheURL(museumName_location)
    url='https://baike.baidu.com/item/%E6%95%A6%E7%85%8C%E7%A0%94%E7%A9%B6%E9%99%A2'
    html=download(url)
    res=getBasicInformation(html)
    #print res[0]
    writeToJson(res)