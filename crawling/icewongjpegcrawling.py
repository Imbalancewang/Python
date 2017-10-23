# written by matthew
#http please
import urllib2,re,itertools
def download(url,user_agent='wswp',num_retries=2):
    print 'Downloading:',url
    headers={'User_agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'url is wrong',e.reason
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                return download(url,user_agent,num_retries-1)
    return html
def crawl_sitemap(url):
    sitemap=download(url)
    links=re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        print link
        html=download(link)
crawl_sitemap('http://example.webscraping.com/sitemap.xml')