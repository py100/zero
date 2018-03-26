#! python2
#coding=utf8

from wda import *

def cal_time(actions):
    tot = 0
    if len(actions) < 2:
        return tot
    presession = actions[0].session
    pretimestamp = actions[0].timestamp
    for action in actions[1:]:
        if action.session == presession:
            tot = tot + (action.timestamp - pretimestamp + 1)
        pretimestamp = action.timestamp
        presession = action.session
    return tot

class Action:
    def __init__(self, wda_rec):
        self.timestamp = int(wda_rec.timestamp)
        self.type = int(wda_rec.type)
        self.content = int(wda_rec.content)
        self.session = wda_rec.sid
    
    def __cmp__(self, s):
        if self.timestamp < s.timestamp:
            return -1
        elif self.timestamp > s.timestamp:
            return 1
        else:
            return 0
