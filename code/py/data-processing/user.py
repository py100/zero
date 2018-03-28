#! python2
#coding=utf8

from wda import *
from action import *
from test import *

class User:
    def __init__(self, userid, courseid, termid):
        self.userid = userid
        self.courseid = courseid
        self.termid = termid
        self.learn_video_actions = []
        self.do_test_actions = []
        self.do_exam_actions = []
        self.other_actions = []

    def update(self, wda):
        if wda.type == '1':
            self.learn_video_actions.append(wda)
        elif wda.type == '2':
            self.do_test_actions.append(wda)
        elif wda.type == '3':
            self.do_exam_actions.append(wda)
        else:
            self.other_actions.append(wda)

    def load_data(self, wda_list):
        pass
    
    def generate_feature(self, test_list):
        video_action = [Action(wda) for wda in self.learn_video_actions]
        video_action.sort()
        test_action = [Action(wda) for wda in self.do_test_actions]
        test_action.sort()
        exam_action = [Action(wda) for wda in self.do_exam_actions]
        exam_action.sort()
        other_action = [Action(wda) for wda in self.other_actions]
        other_action.sort()
        all_action = video_action + test_action + exam_action + other_action
        all_action.sort()
        # generate feature
        # x1 : total time spend on mooc
        x1 = cal_time(all_action)
        # x2 : unique tests tried
        x2 = unique_test(test_action)
        # x3 : count of tests submit
        x3 = len(test_action)
        # x4 : avg submit of test
        if x2 != 0:
            x4 = x3 * 1.0 / x2
        else:
            x4 = 0
        # x5 : max duration of study
        x5 = max_duration(all_action)
        # x6 : total time spend on videos
        x6 = cal_time(video_action)
        # x7 : total time spend on other resources
        x7 = cal_time(other_action)
        # x8 : avg time between test_ddl and submit time
        x8 = cal_avg_interval_ddl(test_action, test_list)
        # x0 : 0 for drop out, 1 for finish
        x0 = 0
        if len(exam_action):
            x0 = 1
        else:
            x0 = 0
        ret = []
        ret.append(x1)
        ret.append(x2)
        ret.append(x3)
        ret.append(x4)
        ret.append(x5)
        ret.append(x6)
        ret.append(x7)
        ret.append(x8)
        ret.append(x0)
        return ret

    def __str__(self):
        if len(self.do_exam_actions) == 0:
            return ""
        return 'user id[{}]\n\
                video_cnt[{}]\n\
                test_cnt[{}]\n\
                exam_cnt[{}]\n\
                other_cnt[{}]'.format(\
                self.userid,\
                len(self.learn_video_actions),\
                len(self.do_test_actions),\
                len(self.do_exam_actions),\
                len(self.other_actions)\
                )
    
    def hash(self):
        return self.userid + self.termid

