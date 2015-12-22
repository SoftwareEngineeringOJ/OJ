# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:39:41 2015

@author: 哲婷
"""
from models import problemslist
import requests
from lxml import etree
import sys
import re
import xml.dom.minidom

class PojSpider():

    def __init__(self):
        pass

    def save_allpage(self):
        for page_number in range(1, 20): #总页数
            self.save_prolst(page_number)

    def save_prolst(self, page_number):
        reload(sys)
        sys.setdefaultencoding("utf-8")
        url = "http://poj.org/problemlist?volume=%d"%page_number
        html = requests.get(url)
        pro_lst_page = etree.HTML(html.text)
        for i in range(2, 70):
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
        for page_number in range(1, 20): #总页数
            self.save_prolst(page_number)

    def save_prolst(self, page_number):
        reload(sys)
        sys.setdefaultencoding("utf-8")
        url = "http://acm.hit.edu.cn/hoj/problem/volume?page=%d"%page_number
        html = requests.get(url)
        pro_lst_page = etree.HTML(html.text,parser=etree.HTMLParser(encoding='utf-8'))

        if pro_lst_page:
            for i in range(1, 70):
                SID = pro_lst_page.xpath('//*[@id="content"]//tr[%d]/td[2]/text()'%i)
                title = pro_lst_page.xpath('//*[@id="content"]/table//tr[%d]/td[3]/a/ins/text()'%i)
                ratio = pro_lst_page.xpath('//*[@id="content"]/table//tr[%d]/td[5]/text()'%i)
                if SID:
                    page_url = "http://acm.hit.edu.cn/hoj/problem/view?id=%s"%SID[0]
                    page_html = requests.get(page_url)
                    problem_page = etree.HTML(page_html.text)
                    if problem_page:
                        source = problem_page.xpath('//*[@id="request"]/table//tr[1]/td[2]/a/text()')
                        time_limit = problem_page.xpath('//*[@id="request"]/table//tr[2]/td[2]/text()')
                        memory_limit = problem_page.xpath('//*[@id="request"]/table//tr[2]/td[4]/text()')
                        text = problem_page.xpath('//*[@id="problem-detail"]')

                        problem = problemslist(OJ = "HOJ",
                                               SID = SID[0],
                                               title = title[0] if title else "",
                                               ratio = ratio[0] if ratio else "",
                                               #source = source[0] if source else "",
                                               time_limit = time_limit[0] if time_limit else "",
                                               mem_limit = memory_limit[0] if memory_limit else "",
                                               description = text[0].xpath("string(.)") if text else "",
                                               inputs = "", output = "", sample_input = "",
                                               sample_output = "", hint = "", pic = "")
                        problem.save()

class HDUSpider():

    def __init__(self):
        pass

    def save_allpage(self):
        reload(sys)
        sys.setdefaultencoding("utf-8")

        for i in range(1000,1500):
            SID = str(i)
            page_url = "http://acm.hdu.edu.cn/showproblem.php?pid=%d"%i
            page_html = requests.get(page_url)
            problem_page = etree.HTML(page_html.text, parser=etree.HTMLParser(encoding='utf-8'))
            if problem_page:
                title = problem_page.xpath('/html/body/table//tr[4]/td/h1/text()')
                limit = problem_page.xpath('/html/body/table//tr[4]/td/font/b/span/text()[1]')#这个格式很乱，稍微整理一下下
                pre_ratio = problem_page.xpath('/html/body/table//tr[4]/td/font/b/span/text()[2]')#同上，重新比例

                description = problem_page.xpath('/html/body/table/tbody/tr[4]/td/div[2]')#string
                _input = problem_page.xpath('/html/body/table//tr[4]/td/div[5]')#string
                _output = problem_page.xpath('/html/body/table//tr[4]/td/div[8]')
                sample_input = problem_page.xpath('/html/body/table//tr[4]/td/div[11]')
                sample_output = problem_page.xpath('/html/body/table//tr[4]/td/div[14]/pre/div')
                source = problem_page.xpath('/html/body/table/tbody/tr[4]/td/div[17]/a/text()')

                time_limit = re.findall(r'Time Limit: \S+ MS', limit[0]) if limit[0] else ""
                mem_limit = re.findall(r'Memory Limit: \S+ K',limit[0]) if limit[0] else ""

                if pre_ratio:
                    x = re.findall(r'\d+', pre_ratio[0])
                    ratio = str(x[1]) + "/ " + str(x[0])
                else:
                    ratio = ""

                problem = problemslist(OJ = "HDU",
                                       SID = SID,
                                       title = title[0] if title else "",
                                       ratio = ratio,
                                       #source = source[0] if source else "",
                                       time_limit = time_limit[0] if time_limit else "",
                                       mem_limit = mem_limit[0] if mem_limit else "",
                                       description = description[0].xpath("string(.)") if description else "",
                                       inputs = _input[0].xpath("string(.)") if _input else "",
                                       output = _output[0].xpath("string(.)") if _output else "",
                                       sample_input = sample_input[0].xpath("string(.)") if sample_input else "",
                                       sample_output = sample_output[0].xpath("string(.)") if sample_output else "",
                                       hint = "", pic = "")
                problem.save()

'''
class GetNews():
    def __init__(self):
        self.News = []
        reload(sys)
        sys.setdefaultencoding("utf-8")
        url = "http://contests.acmicpc.info/contests.rss"
        html = requests.get(url)

        f = open("test.xml",'w')
        f.write(str(html.text))

    def get_news(self):
        dom_tree = xml.dom.minidom.parse("test.xml")
        collection = dom_tree.documentElement

        items = collection.getElementsByTagName("item")

        for item in items:
            temp = news(title=(item.getElementsByTagName("title"))[0].childNodes[0].data,
                       link=(item.getElementsByTagName('link')[0]).childNodes[0].data,
                       description=(item.getElementsByTagName('description')[0]).childNodes[0].data,
                       date=((item.getElementsByTagName('pubDate')[0]).childNodes[0].data)[:-5],
                       guid=(item.getElementsByTagName('guid')[0]).childNodes[0].data)

        self.News.append(temp)
        return self.News
'''
