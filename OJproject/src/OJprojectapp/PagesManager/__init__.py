#coding=utf-8
'''
Created on 2015年12月23日

@author: Rhapsody
'''
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
class PagesManager(object):
    '''
    classdocs
    '''


    def __init__(self, name, now, data, segment):
        '''
        Constructor
        '''
        self.name = name
        self.now = now
        self.segment = segment
        data_list = data
        paginator = Paginator(data_list, segment)
        try:
            contacts = paginator.page(now)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        self.show_list = contacts
        page = paginator.page(now)
        self.begin = page.start_index()
        self.end = page.end_index()
        self.total = len(data)
        self.previous = now - 1
        if now == 1:
            self.previous = now
        self.next = now + 1
        self.totalpages = paginator.num_pages
        if now == paginator.num_pages:
            self.next = now
        self.first_gap = False
        self.first = []
        if now > 6:
            self.first_gap = True
            self.first.append(1)
            self.first.append(2)
        self.second = []
        for i in range(4):
            if now - 4 + i > 0:
                self.second.append(now - 4 + i)
        for i in range(5):
            if now + i <= paginator.num_pages:
                self.second.append(now + i)
        self.second_gap = False
        self.third = []
        if now < paginator.num_pages - 6:
            self.second_gap = True
            self.third.append(paginator.num_pages - 1)
            self.third.append(paginator.num_pages)
