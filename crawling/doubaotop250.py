# -*- coding: utf-8 -*-
# @Time    : 2017/12/1 21:02
# @Author  : Matthew
# @Site    : 
# @File    : doubaotop250.py
# @Software: PyCharm Community Edition
import urllib2,urllib,re,urlparse
from bs4 import BeautifulSoup
def download(url,user_agent='wswp',proxy=None,num_tries=2):
    print 'Downloading:',url
    headers={'User_agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    opener=urllib2.build_opener()
    if proxy:
        proxy_params={urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html=urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Downloading error:',e.reason
        html=None
        if num_tries>0:
            if hasattr(e,'code') and 500<=e.code<=600:
                return download(url,user_agent,num_tries-1)
    return html
def getData(url):
    findLink=re.compile(r'<a href="(.*?)">')#find the link
    findImgSrc=re.compile(r'img.*src="(.*jpg)"',re.S)#find the picture
    findTitle=re.compile(r'<span class="title">(.*)</span>')#find the title
    findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
    findJudge=re.compile(r'<span>(\d*)人评价</span>')
    findInq=re.compile(r'<p class="quote">(.*?)</p>',re.S)
    findBd=re.compile(r'<p class="">(.*?)</p>',re.S)
