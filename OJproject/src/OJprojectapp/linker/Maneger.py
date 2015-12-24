#coding=utf-8
'''
Created on 2015年11月24日

@author: Rhapsody
'''
import CodeManager
import POJ
import HOJ
import HDU
from Queue import Queue
import threading
from OJprojectapp.models import user_status

class Worker(threading.Thread):
    
    def __init__(self, t_name, Q):
        threading.Thread.__init__(self, name = t_name)
        self.Q = Q
        self.pojlinker = POJ.Submit()
        self.hojlinker = HOJ.Submit()
        self.hdulinker = HDU.Submit()
        
    def getOJ(self, oj):
        if (oj == 'POJ'):
            return self.pojlinker
        if (oj == 'HOJ'):
            return self.hojlinker
        if (oj == 'HDU'):
            return self.hdulinker
    
    def run(self):
        while not self.Q.empty():
            T = self.Q.get()
            #print 'Process ', T.username
            code = CodeManager.GetFile(T.id)
            try:
                res = self.getOJ(T.OJ).submit(T.problemID, T.language, code)
            except:
                res = ['Judge Error', '', '']
            print 'res =', res
            rec = user_status.objects.get(id = T.id)
            rec.result = res[0]
            rec.time = res[1]
            rec.memory = res[2]
            rec.save()
            #list.sort(reversed = False)
        print 'All done'

class Judge(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.Q = Queue()
        self.work = Worker('Pro.', self.Q)
        self.work.start()
        
    def setup(self):
        self.work.start()
    
    def isAlive(self):
        return self.work.isAlive()
    
    def push(self, source):
        print 'Push', source.username
        self.Q.put(source)
        if not self.isAlive():
            print source.username, ' has gone '
            self.work = Worker('Pro.', self.Q)
            self.work.start()
    
    def stop(self):
        self.work.stop()
        
    def __def__(self):
        self.work.join()
