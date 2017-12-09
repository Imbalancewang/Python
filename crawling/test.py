# -*- coding: utf-8 -*-
# @Time    : 2017/12/3 22:12
# @Author  : Matthew
# @Site    :
# @File    : allplayers.py
# @Software: PyCharm Community Edition
#4613
import urllib2,urllib,urlparse,re,xlwt
import sys,time
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
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
    time.sleep(1)
    return html
if __name__ == '__main__':
    for i in range(1,100):
        url='http://www.stat-nba.com/player/%d.html'%i
        download(url)
