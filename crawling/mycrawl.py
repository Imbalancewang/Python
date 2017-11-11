# written by matthew
import re,urllib2,urllib,itertools
def download(url,user_agent='wswp',num_retries=2):
    print 'Downloading:',url
    headers={'User_agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'something is wrong',e.reason
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                return download(url,user_agent,num_retries-1)
    return html
pattern='<td class="w2p_fw">[0-9,]+ square kilometres</td>'#second read missing?
res=[]
for pages in range(1,3):#itertools.count(1)
    url = 'http://example.webscraping.com/places/default/view/%d'%pages
    html=download(url)
    print url
    if html is None:break
    else:
        res.append(re.findall(pattern,html)[0])
'''
url_raw='http://example.webscraping.com/places/default/view/3'
content=what(url_raw)
s=re.findall(pattern,content)
'''
print res

