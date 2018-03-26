#! python2
#coding=utf8

from wda import *

class Action:
    def __init__(self, wda_rec):
        self.timestamp = int(wda_rec.timestamp)
        self.type = int(wda_rec.type)
        self.content = int(wda_rec.content)
        self.session = wda_rec.session
    
    def __cmp__(self, s):
        if self.timestamp < s.timestamp:
            return -1
        elif self.timestamp > s.timestamp:
            return 1
        else:
            return 0
