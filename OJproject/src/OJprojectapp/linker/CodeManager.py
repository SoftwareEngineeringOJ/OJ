#coding=utf-8
'''
Created on 2015年11月24日

@author: Rhapsody
'''
import os
import POJ
import HOJ

def GetOJ(oj):
    print 'oj =', oj
    if oj == 'POJ':
        return POJ.Submit()
    if oj == 'HOJ':
        return HOJ.Submit()

def SaveFile(Code, RunID):
    output = open(os.getcwd() + '\\code\\%s.code' % RunID, 'wb')
    output.write(Code.encode('utf-8'))
    output.close()
    
def GetFile(RunID):
    path = os.getcwd() + '\\code\\%s.code' % RunID
    f = open(path, 'r')
    code = f.read()
    f.close()
    return code