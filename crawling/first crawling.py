# written by matthew
import csv,re,lxml.html
class ScrapeCallback:
    def __init__(self):
        self.writer=csv.writer(open('contries.csv','w'))
        self.fields=('area','population','iso','country',
                     'capital','continent','tid','currency_code',
                     'currency_name','phone','postal_code_format',
                     'postal_code_regex','language','neighbours')
        self.writer.writerow(self.fields)
    def __call__(self, url,html):
        if re.search('/view/',url):
            tree=lxml.html.fromstring(html)
            row=[]
            for field in self.fields:
                row.append(tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content())
            self.writer.writerow(row)
def link_crawler(url,max_depth=1,scrape_callback=None):