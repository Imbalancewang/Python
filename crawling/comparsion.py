# written by matthew
import urllib2,cssselect,lxml.html,re,urlparse,time
from bs4 import BeautifulSoup
FIELDS={'area','population','iso','country','capital',
        'continent','tld','currency_code','currency_name',
        'phone','postal_code_format','postal_code_regex',
        'languages','neighbours'}
def download(url,user_agent='wswp',num_tries=2):
    print 'Downloading:',url
    headers={'User_agent':user_agent}
    request=urllib2.Request(url,headers=headers)
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
def re_scraper(html):
    result={}
    for field in FIELDS:
        result[field]=re.search('<tr id=class"places_%s__row">.*?<td class="w2p_fw">(.*?)</td>'%field,html).group()[0]
    return result
def bs_scraper(html):
    soup=BeautifulSoup(html,'html.parser')
    result={}
    for field in FIELDS:
        result[field]=soup.find('table').find('tr',id='places_%s__row'%field).find('td',class_='w2p_fw').text
    return result
def lxml_scraper(html):
    tree=lxml.html.fromstring(html)
    result={}
    for field in FIELDS:
        result[field]=tree.cssselect('table > tr#places_%s__row > td.w2p_fw'%field)[0].text_content()
    return result
num_iterations=10
html=download('http://example.webscraping.com/places/default/view/Belgium-22')
for name ,scraper in [('Regular expressions',re_scraper),('BeautifulSoup',bs_scraper),('Lxml',lxml_scraper)]:
    start= time.time()
    for i in range(num_iterations):
        if scraper==re_scraper:
            re.purge()
        result=scraper(html)
        assert(result['area']=='30,510 square kilometres')
    end=time.time()
    print '%s:%.2f seconds'%(name,end-start)
#lazy do not wat to correct