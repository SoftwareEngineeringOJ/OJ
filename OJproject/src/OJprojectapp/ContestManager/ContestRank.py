#coding=utf-8
'''
Created on 2015年12月24日

@author: Rhapsody
'''

import datetime
from django.db.models.lookups import Second

class Node():
    def __init__(self, username, num):
        print 'Add user =', username
        self.username = username
        self.status = [0] * num
        self.show = ["+"] * num
        self.ac = [False] * num
        self.rank = 0
        self.each = [datetime.timedelta()] * num
        self.score = 0
        self.time = datetime.timedelta()
    
    def submit(self, id, result, time):
        print 'Submit = %d', id, result, time
        if not self.ac[id]:
            self.each[id] += time
            self.status[id] -= 1
            if result:
                self.ac[id] = True
                self.score += 1
                self.status[id] = '+%d' % (-self.status[id])
                self.time += self.each[id]
        for status in self.status:
            print status,
        print '\n'

class Tree():
    def __init__(self, m, ProblemsList):
        self.labels = []
        self.num = m
        self.flag = [False] * m
        for i in range(m):
            self.labels.append(chr(ord('A') + i))
        self.usernames = []
        self.users = []
        self.problems = ProblemsList
    
    def adduser(self, username):
        self.usernames.append(username)
        self.users.append(Node(username, self.num))
    
    def mycmp(self, a, b):
        if a.score != b.score:
            return a.score < b.score
        return a.time > b.time
    
    def accepted(self, status):
        id = -1
        for p in self.problems:
            print 'cmp', status.OJ + '_' + status.problemID, p.Num
            if (status.OJ + '_' + status.problemID) == p.Num:
                id = ord(p.Lab) - ord('A')
        result = False
        if status.result == 'Accepted' or status.result == 'accepted':
            result = True
        return id, result
    
    def judge(self, status, BeginTime, EndTime):
        print 'Begin judge:'
        if status.username not in self.usernames:
            self.adduser(status.username)
        if (status.submit_time < BeginTime or status.submit_time > EndTime):
            print 'Time Error'
            print status.submit_time, BeginTime, EndTime
            return
        if (status.result == 'Judge Error'):
            return
        id, result = self.accepted(status)
        print 'find =', id, result
        if (id < 0):
            return
        for man in self.users:
            if man.username == status.username:
                man.submit(id, result, status.submit_time - BeginTime)
        for i in range(len(self.users)):
            for j in range(i):
                if self.mycmp(self.users[j], self.users[i]):
                    self.users[j], self.users[i] = self.users[i], self.users[j]
        for i in range(len(self.users)):
            self.users[i].rank = i + 1

def GeneratorRank(ProblemsList, StatusList, BeginTime, EndTime):
    m = len(ProblemsList) #题目数量
    judge = Tree(m, ProblemsList)
    for status in StatusList:
        judge.judge(status, BeginTime, EndTime)
    
    return judge
