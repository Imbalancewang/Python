# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 14:43
# @Author  : Matthew
# @Site    : 
# @File    : Download.py
# @Software: PyCharm
import urllib2,urlparse

def download(url,headers=None,proxy=None,num_tries=2,data=None):
    print 'Downloading:',url
    request=urllib2.Request(url,data,headers)
    opener=urllib2.build_opener()
    if proxy:
        proxy_params={urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        response=opener.open(request)
        html=response.read()
        code=response.code
    except urllib2.URLError as e:
        print 'Download error:',e.reason
        html=None
        if hasattr(e,'code'):
            code=e.code
            if num_tries>0 and 500<=code<600:
                return download(url,headers,proxy,num_tries-1,data)
            else:code=None
    return html