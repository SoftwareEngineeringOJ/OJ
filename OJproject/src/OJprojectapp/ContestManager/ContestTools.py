#coding=utf-8
'''
Created on 2015年12月24日

@author: Rhapsody
'''

from OJprojectapp.models import *
from _ast import Num

class ContestProblemList():
    def __init__(self, Lab, Num, Tit, id):
        self.Lab = Lab
        self.Num = Num
        self.Tit = Tit
        self.id = id

def get_contest_problems_list(contest_id):
    aim = contest.objects.get(id = contest_id)
    List = []
    count = 0
    for problem in aim.list.all():
        Lab = chr(ord('A') + count)
        count += 1
        Num = problem.sojs + '_' + problem.pids
        List.append(ContestProblemList(Lab = Lab, 
                                       Num = Num, 
                                       Tit = problem.titles, 
                                       id = problem.id, 
                                       ))
    return List
