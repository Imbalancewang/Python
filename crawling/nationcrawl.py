# written by matthew
import re,urlparse,urllib2
from bs4 import BeautifulSoup
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
url='http://example.webscraping.com/places/default/view/United-Kingdom-239'
html=download(url)
soup=BeautifulSoup(html,"html.parser")
tr=soup.find(attrs={'id':'places_area__row'})
print tr

