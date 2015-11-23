# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:33:44 2015

@author: 哲婷
"""
from models import Problems, ProblemsList
from Spider import Spider


class PojSpider(Spider):

    def __init__(self, max_pagenum):
        Spider.__init__(self)
        self.max_pagenum = max_pagenum

    def save_allpage(self):
        for page_number in range(1, self.max_pagenum+1):
            self.save_prolst(page_number)

    def save_prolst(self, page_number):
        url = 'http://poj.org/problemlist?volume=%d'%page_number
        pro_lst_page = Spider.get_page(url)
        for i in range(2, 102):
            ID = pro_lst_page.xpath('/html/body/table[2]//tr[%d]/td[1]/text()'%i)
            href = pro_lst_page.xpath('/html/body/table[2]//tr[%d]/td[2]/a/@href'%i)
            title = pro_lst_page.xpath('/html/body/table[2]//tr[%d]/td[2]/a/text()'%i)
            ratio = pro_lst_page.xpath('/html/body/table[2]//tr[%d]/td[3]'%i)

            prolst_item = ProblemsList(ID=0,
                                       OJ="POJ",
                                       SID=ID[0] if ID else "",
                                       href=href[0] if href else "",
                                       title=title[0] if title else "",
                                       ratio=ratio[0].xpath('string(.)') if ratio else "")
            prolst_item.save()
            prolst_item.ID = prolst_item.id
            prolst_item.save()

            self.save_problem(str(prolst_item.SID))

    def save_problem(self, proid):
        url = 'http://poj.org/problem?id=%d'%proid
        problem_page = Spider.get_page(url)
        
        title = problem_page.xpath('/html/body/table[2]//tr/td/div[2]/text()')
        time_limit = problem_page.xpath('/html/body/table[2]//tr/td/div[3]/table//tr[1]/td[1]')
        mem_limit = problem_page.xpath('/html/body/table[2]//tr/td/div[3]/table//tr[1]/td[3]')
        description = problem_page.xpath('/html/body/table[2]//tr/td/div[4]')
        _input = problem_page.xpath('/html/body/table[2]//tr/td/div[5]')
        _output = problem_page.xpath('/html/body/table[2]//tr/td/div[6]')
        sample_input = problem_page.xpath('/html/body/table[2]//tr/td/pre[1]/text()')
        sample_output = problem_page.xpath('/html/body/table[2]//tr/td/pre[2]/text()')
        hint = problem_page.xpath('/html/body/table[2]//tr/td/div[7]/text()')

        problem = Problems(ID=0, OJ="POJ",
                           SID=proid,
                           title=title[0] if title else "",
                           time_limit=time_limit[0].xpath('string(.)') if time_limit else "",
                           mem_limit=mem_limit[0].xpath('string(.)') if mem_limit else "",
                           description=description[0].xpath('string(.)') if description else "",
                           _input=_input[0].xpath('string(.)') if _input else "",
                           _output=_output[0].xpath('string(.)') if _output else "",
                           sample_input=sample_input[0] if sample_input else "",
                           sample_output=sample_output[0] if sample_output else"",
                           hint=hint[0] if hint else "")
        problem.save()
        problem.ID = problem.id
        problem.save()
