# written by matthew
import re,urllib2,urllib,itertools,urlparse
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
res=[]
pattern='<td class="w2p_fw">[0-9,]+ square kilometres</td>'#second read missing?
for pages in range(1,3):#itertools.count(1)
    url = 'http://example.webscraping.com/places/default/view/%d'%pages
    html=download(url)
    print url
    if html is None:break
    else:
        res.append(re.findall(pattern,html)[0])