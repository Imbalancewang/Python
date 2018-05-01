# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 00:13
# @Author  : Matthew
# @Site    : 
# @File    : geturl.py
# @Software: PyCharm
import urllib2,urllib,urlparse,re,xlwt
import sys,time,socket
from bs4 import BeautifulSoup
from datetime import datetime
import json,xlwt
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

def createSearchUrl():
    fp=open('/Users/rd/Desktop/project_museum/Data/museumName.md','r')
    museumName=fp.readlines()
    fp.close()
    url,basic_url,keyword=[],'http://www.baidu.com/s?wd=','官网'
    for i in range(len(museumName)):
        url.append(basic_url+urllib.quote((museumName[i]+keyword).decode(sys.stdin.encoding).encode('gbk')))
    return url

def getTheOfficalWeb(allurl):
    finalurl,pattern=[],'[1-9a-z.-]+/'
    for i in range(len(allurl)):
        html=download(allurl[i])
        soup=BeautifulSoup(html,'lxml')
        rowurl=soup.find('div','f13').next_element.getText()
        finalurl.append(re.findall(pattern,rowurl))
    return finalurl

def writeToFile(url):
    file=open('/Users/rd/Desktop/project_museum/Data/MuseumURL.md','w+')
    for i in range(len(url)):
        if len(url[i])>0:
            file.write(url[i][0])
        else:
            file.write('')
        file.write('\n')
if __name__=="__main__":
    allurl=createSearchUrl()
    finalurl=getTheOfficalWeb(allurl)
    print finalurl
    writeToFile(finalurl)
    #print allurl[0]