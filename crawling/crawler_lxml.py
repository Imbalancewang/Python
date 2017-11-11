# written by matthew
import lxml.html
import cssselect
import urllib2
def download(url,user_agent='wswp',num_tries=2):
    print 'Downloading:',url
    header={'User_agent':user_agent}
    request=urllib2.Request(url,headers=header)
    try:
        html=urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Downloading error:',e.reason
        html=None
        if num_tries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                return download(url,user_agent,num_tries-1)
    print 'Downloaded'
    return html
row_url='http://example.webscraping.com/places/default/view/Belgium-22'
html=download(row_url)
tree=lxml.html.fromstring(html)
td=tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
area=td.text_content()
print area

