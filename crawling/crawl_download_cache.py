# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 00:12
# @Author  : Matthew
# @Site    : 
# @File    : crawl_download_cache.py
# @Software: PyCharm
import lxml,re,urllib,urllib2
class Downloader:
    def __init__(self,delay=5,
                 user_agent='matthew',proxies=None,
                 num_retries=1,cache=None):
        self.throttle=