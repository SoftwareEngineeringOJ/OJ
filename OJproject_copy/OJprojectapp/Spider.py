# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:39:41 2015

@author: 哲婷
"""
import sys
import requests
from lxml import etree

class Spider():
    
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding("utf-8")
        
    def get_page(self, url):
        html = requests.get(url)
        page = etree.HTML(html.text, parser=etree.HTMLParser(encoding='utf-8'))
        return page
    
            