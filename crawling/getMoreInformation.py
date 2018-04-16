# -*- coding: utf-8 -*-
# @Time    : 2018/4/7 23:58
# @Author  : Matthew
# @Site    : 
# @File    : getMoreInformation.py
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

def getMoreInformation(html):
    """
    introduction:find('div','lemma-summary).get_text()
    education(dict):{
        key=level2[0].previous_element.previous_element.get('name')
        loop for to find
        }
    object(dict){
        key=level2[0].previous_element.previous_element.get('name')
        loop for to find
    }
    museumStudy(dict){
        key=level2[0].previous_element.previous_element.get('name')
        loop for to find
    }
    :param html:
    :return:
    """
    soup = BeautifulSoup(html, 'lxml')
    keyname,education,museumObject,museumStudy,=[],'','',''
    level2=soup.find_all('div','para-title level-2')
    if level2==[]:
        print 'the page is too simple!'
        return {}
    #print len(level2)
    for i in range(len(level2)):
        keyname.append(level2[i].previous_element.previous_element.get('name'))
    flag=-1
    ##############introduction####################
    """
    introduction=soup.find('div','lemma-summary')
    if introduction==[]:
        return {'简要介绍','空'}
    return dict(zip(['简要介绍'],[introduction.get_text().replace("\n","")]))
    """
    ###############education#####################
    """
    for i in range(len(level2)):
        if u'教育活动'  in keyname[i] or u'文化活动' in keyname[i]:
            flag=i
    if flag==-1:
        return {'教育活动':'空'}
    test=level2[flag]
    if flag==len(level2):
        print 'beyond'
        return {'cccc':'dsds'}
    while test.next_sibling!=level2[flag+1]:
        education+=str(test)
        test=test.next_sibling
    res=BeautifulSoup(education,'lxml')
    result=res.get_text().replace("\n","")
    return dict(zip([keyname[flag]],[result]))
    """
    #################object##################
    for i in range(len(level2)):
        if u'珍品' in keyname[i] or u'藏品' in keyname[i] or u'展品' in keyname[i] or u'文物' in keyname[i]:
            flag=i
    if flag==-1:
        return {'经典藏品信息':'空'}
    if flag==len(level2):
        return{'beyond':'need to be modified'}
    test=level2[flag]
    while test.next_sibling!=level2[flag+1]:
        museumObject+=str(test)
        test=test.next_sibling
    res=BeautifulSoup(museumObject,'lxml')
    result=res.get_text().replace("\n","")
    return dict(zip([keyname[flag].decode('utf-8')],[result.decode('utf-8')]))
    ################study################
    """
    for i in range(len(level2)):
        if u'科研文化' in keyname[i] or u'研究成果' in keyname[i]:
            flag=i
    if flag==-1:
        return {'学术研究信息':'空'}
    if flag==len(level2):
        return {'beyond': 'need to be modified'}
    test=level2[flag]
    while test.next_sibling!=level2[flag+1]:
        museumStudy+=str(test)
        test=test.next_sibling
    res=BeautifulSoup(museumStudy,'lxml')
    result=res.get_text().replace("\n","")
    return dict(zip([keyname[flag]],[result]))
    """

def writeToFile(res=[]):
    #fp=open('/Users/rd/Desktop/Python/crawling/museumIntroduction.json','w+')
    #fp=open('/Users/rd/Desktop/Python/crawling/museumEducation.json','w+')
    fp=open('/Users/rd/Desktop/Python/crawling/museumObject.json','w+')
    #fp=open('/Users/rd/Desktop/Python/crawling/museumResearch.json','w+')
    for i in res:
        json.dump(i,fp,ensure_ascii=False,default=set_default)
        fp.write('\n')
    fp.close()
    return

def readCreateTheURL(name):
    ff=open(name,'rb')
    MuseumName=ff.readlines()
    basic_url = 'https://baike.baidu.com/item/'
    url=[]
    for i in MuseumName:
        url.append(basic_url+i)
    return url

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def writeToCsv(name):
    fp=open('/Users/rd/Desktop/Python/museumName.md','rb')
    mname=fp.readlines()
    museumname=[]
    for i in mname:
        museumname.append(museumname)
    fp.close()
    datalist=[]
    datalist.append(museumname)
    col=['MuseumName']
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet=book.add_sheet('NBA-data',cell_overwrite_ok=True)
    for i in range(len(col)):
        sheet.write(0, i, col[i])
    for i in range(len(col)):
        for j in range(len(datalist[0])):
            print datalist[i][j]
            #sheet.write(i + 1, j, datalist[i][j])
    book.save(name)

if __name__=='__main__':
    #museumName_location='/Users/rd/Desktop/Python/museumName.md'
    name='mylove.xlsx'
    writeToCsv(name)
    """
    url='https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E8%87%AA%E7%84%B6%E5%8D%9A%E7%89%A9%E9%A6%86/2002464?fr=aladdin#5'
    html=download(url)
    print getMoreInformation(html)
    """
    """
    url=readCreateTheURL(museumName_location)
    result=[]
    for each_url in url:
        html=download(each_url)
        temp=getMoreInformation(html)
        result.append(temp)
    #print result
    writeToFile(result)
    """