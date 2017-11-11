# written by matthew
from bs4 import BeautifulSoup
import urllib2
def download(url,user_agent='wswp',num_tries=2):
    print 'Downloading:',url
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
row_url='http://example.webscraping.com/places/default/view/Belgium-22'
html=download(row_url)
soup=BeautifulSoup(html,'lxml')#'lxml'is necessary?
tr=soup.find(attrs={'id':'places_area__row'})
td=tr.find(attrs={'class':'w2p_fw'})
area=td.text
print area
# read thr html code
# tr is the father class
# td is the child