# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:39:41 2015

@author: 哲婷
"""
from models import problemslist
import requests
from lxml import etree
import sys


class PojSpider():

    def __init__(self):
        pass

    def save_allpage(self):
        for page_number in range(1, 5): #总页数
            self.save_prolst(page_number)

    def save_prolst(self, page_number):
        reload(sys)
        sys.setdefaultencoding("utf-8")
        url = "http://poj.org/problemlist?volume=%d"%page_number
        html = requests.get(url)
        pro_lst_page = etree.HTML(html.text)
        for i in range(2, 80):
            ID = pro_lst_page.xpath('/html/body/table[2]//tr[%d]/td[1]/text()'%i)
            href = pro_lst_page.xpath('/html/body/table[2]//tr[%d]/td[2]/a/@href'%i)
            title = pro_lst_page.xpath('/html/body/table[2]//tr[%d]/td[2]/a/text()'%i)
            ratio = pro_lst_page.xpath('/html/body/table[2]//tr[%d]/td[3]'%i)
            url = 'http://poj.org/problem?id=%s'%ID[0]
            html = requests.get(url)
            problem_page = etree.HTML(html.text, parser=etree.HTMLParser(encoding='utf-8'))

            time_limit = problem_page.xpath('/html/body/table[2]//tr/td/div[3]/table//tr[1]/td[1]')
            mem_limit = problem_page.xpath('/html/body/table[2]//tr/td/div[3]/table//tr[1]/td[3]')
            description = problem_page.xpath('/html/body/table[2]//tr/td/div[4]')
            _input = problem_page.xpath('/html/body/table[2]//tr/td/div[5]')
            _output = problem_page.xpath('/html/body/table[2]//tr/td/div[6]')
            sample_input = problem_page.xpath('/html/body/table[2]//tr/td/pre[1]/text()')
            sample_output = problem_page.xpath('/html/body/table[2]//tr/td/pre[2]/text()')
            hint = problem_page.xpath('/html/body/table[2]//tr/td/div[7]/text()')
            pic_urls = problem_page.xpath("//center/img/@src")

            pics_addr = ""
            if pic_urls:
                for pic_url in pic_urls:
                    pics_addr += "http://poj.org/" + str(pic_url) + " "
            '''
            if pic_urls:
                i = 0
                for pic_url in pic_urls:
                    purl = "http://poj.org/" + str(pic_url)
                    pic = requests.get(purl)
                    try :
                        fp = open("POJ" + str(SID) + str(i) + pic_url[-4:], "wb")
                        fp.write(pic.content)
                        fp.close()
                    except:
                        print "static/images/POJ" + str(SID) + str(i) + pic_url[-4:]
                    i+=1
            '''
            problem = problemslist(OJ="POJ",
                           SID=ID[0] if ID else "",
                           title=title[0] if title else "",
                           ratio=ratio[0].xpath('string(.)') if ratio else "",
                           time_limit=time_limit[0].xpath('string(.)') if time_limit else "",
                           mem_limit=mem_limit[0].xpath('string(.)') if mem_limit else "",
                           description=description[0].xpath('string(.)') if description else "",
                           inputs=_input[0].xpath('string(.)') if _input else "",
                           output=_output[0].xpath('string(.)') if _output else "",
                           sample_input=sample_input[0] if sample_input else "",
                           sample_output=sample_output[0] if sample_output else"",
                           hint=hint[0] if hint else "",
                           pic=pics_addr)
            problem.save()
            



class HojSpider():

    def __init__(self):
        pass

    def save_allpage(self):
        for page_number in range(1, 5): #总页数
            self.save_prolst(page_number)

    def save_prolst(self, page_number):
        reload(sys)
        sys.setdefaultencoding("utf-8")
        url = "http://acm.hit.edu.cn/hoj/problem/volume?page=%d"%page_number
        html = requests.get(url)
        pro_lst_page = etree.HTML(html.text)
        for i in range(1, 10):
            ID = pro_lst_page.xpath('//*[@id="content"]/table//tr[%d]/td[2]/text()'%i)
            href = pro_lst_page.xpath('//*[@id="content"]/table//tr[%d]/td[3]/a/@href'%i)
            title = pro_lst_page.xpath('//*[@id="content"]/table//tr[%d]/td[3]/a/ins/text()'%i)
            ratio = pro_lst_page.xpath('//*[@id="content"]/table//tr[%d]/td[5]'%i)
            url = 'http://acm.hit.edu.cn/hoj/problem/view?id=%s'%ID[0]
            html = requests.get(url)
            problem_page = etree.HTML(html.text, parser=etree.HTMLParser(encoding='utf-8'))

            time_limit = problem_page.xpath('//*[@id="request"]/table//tr[2]/td[2]')
            mem_limit = problem_page.xpath('//*[@id="request"]/table//tr[2]/td[4]')
            description = problem_page.xpath('//*[@id="problem-detail"]')
            _input = ""
            _output = ""
            sample_input = ""
            sample_output = ""
            hint = ""
            problem = problemslist(OJ="HOJ",
                           SID=ID[0] if ID else "",
                           title=title[0] if title else "",
                           ratio=ratio[0].xpath('string(.)') if ratio else "",
                           time_limit=time_limit[0].xpath('string(.)') if time_limit else "",
                           mem_limit=mem_limit[0].xpath('string(.)') if mem_limit else "",
                           description=description[0].xpath('string(.)') if description else "",
                           inputs=_input,
                           output=_output,
                           sample_input=sample_input,
                           sample_output=sample_output,
                           hint=hint,
                           pic="")
            problem.save()
