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

def unique_test(actions):
    ret = 0
    tests = set()
    for action in actions:
        if action.type == 2 and action.content not in tests:
            tests.add(action.content)
            ret = ret + 1
    return ret


def max_duration(actions):
    ret = 0
    if len(actions) < 2:
        return ret
    presession = actions[0].session
    pretimestamp = actions[0].timestamp
    for action in actions[1:]:
        if action.session == presession:
            ret = max(ret, action.timestamp - pretimestamp)
        else:
            pretimestamp = action.timestamp
            presession = action.session
    return ret
def cal_avg_interval_ddl(actions, test_list):
    tot, cnt = 0, 0
    for action in actions:
        if action.type == 2:
            for test in test_list:
                if action.content == test.id and action.timestamp < test.ddl:
                    tot = tot + (test.ddl - action.timestamp)
                    cnt = cnt + 1
    if cnt == 0:
        return 0
    else:
        return tot * 1.0 / cnt


class Action:
    def __init__(self, wda_rec):
        self.timestamp = int(wda_rec.timestamp)
        # type = 1: video
        # type = 2: test
        # type = 3: exam
        # type = 10: exam
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
