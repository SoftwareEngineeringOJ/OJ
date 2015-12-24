#coding=utf-8
'''
Created on 2015年11月24日

@author: Rhapsody
'''
import os
import POJ
import HOJ
from OJprojectapp.models import code_files

def GetOJ(oj):
    print 'oj =', oj
    if oj == 'POJ':
        return POJ.Submit()
    if oj == 'HOJ':
        return HOJ.Submit()

def SaveFile(Code, RunID):
    count = 0
    buffer = ""
    for c in Code:
        count += 1
        buffer = buffer + c
        if count == 100:
            code_files(runID = RunID, 
                       code = buffer).save()
            count = 0
            buffer = ""
    if count > 0:
        code_files(runID = RunID, 
                   code = buffer).save()
        count = 0
        buffer = ""
    
def GetFile(RunID):
    codes = code_files.objects.filter(runID = RunID).order_by('id')
    Ans = ""
    for code in codes:
        Ans = Ans + code.code
    return Ans