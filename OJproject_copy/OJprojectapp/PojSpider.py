# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:33:44 2015

@author: 哲婷
"""

from Spider import Spider

class PojSpider(Spider):
    def __init__(self):
        Spider.__init__(self)
        self.prolstpage_number = 0
        self.prolstpage
        self.proid
        self.problempage
    
    def _get_prolstpage(self, page_number):
        self.prolstpage_number = page_number
        url = 'http://poj.org/problemlist?volume=%d'%page_number
        self.prolstpage = Spider.get_page(url)
        
    def get_prolst(self, page_number):
        self._get_prolstpage(page_number)
        prolst = []
        for i in range(2, 102):
            ID = self.prolstpage.xpath('/html/body/table[2]//tr[%d]/td[1]/text()'%i)[0]
            href = self.prolstpage.xpath('/html/body/table[2]//tr[%d]/td[2]/a/@href'%i)[0]
            title = self.prolstpage.xpath('/html/body/table[2]//tr[%d]/td[2]/a/text()'%i)[0]
            ratio = self.prolstpage.xpath('/html/body/table[2]//tr[%d]/td[3]'%i)[0].xpath('string(.)')
            
            prolst.append([ID, href, title, ratio])
        return prolst
    
    def _get_proid(self, proid):
        self.proid = proid
        url = 'http://poj.org/problem?id=%d'%proid
        self.problempage = Spider.get_page(url)
        
    def get_problem(self, proid):
        self._get_proid(proid)
        
        title = self.problempage.xpath('/html/body/table[2]//tr/td/div[2]/text()')[0]
        time_limit = self.problempage.xpath('/html/body/table[2]//tr/td/div[3]/table//tr[1]/td[1]')[0].xpath('string(.)')
        mem_limit = self.problempage.xpath('/html/body/table[2]//tr/td/div[3]/table//tr[1]/td[3]')[0].xpath('string(.)')
        description = self.problempage.xpath('/html/body/table[2]//tr/td/div[4]')[0].xpath('string(.)')
        _input = self.problempage.xpath('/html/body/table[2]//tr/td/div[5]')[0].xpath('string(.)')
        _output = self.problempage.xpath('/html/body/table[2]//tr/td/div[6]')[0].xpath('string(.)')
        sample_input = self.problempage.xpath('/html/body/table[2]//tr/td/pre[1]/text()')[0]
        sample_output = self.problempage.xpath('/html/body/table[2]//tr/td/pre[2]/text()')[0]
        hint = self.problempagexpath('/html/body/table[2]//tr/td/div[7]/text()')
        
        problem = [title, time_limit, mem_limit, description, _input, _output, sample_input, sample_output, hint[0] if hint else ""]
        return problem
