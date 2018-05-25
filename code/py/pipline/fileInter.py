#! python3
#coding=utf8

import json

class Term:
    def __init__(self, line):
        tmp = line.strip().split('\t')
        self.term_id = tmp[0]
        self.course_id= tmp[1]
        self.start_time = tmp[2]
        self.end_time = tmp[3]
        self.qualified_count = tmp[4]
        self.excellent_count = tmp[5]
        self.enroll_count = tmp[6]

    def inTerm(self, t):
        if int(t) >= int(self.start_time) and int(t) <= int(self.end_time):
            return True
        else:
            return False

class User:
    def __init__(self, line):
        tmp = line.strip().split('\t')
        self.user_id = tmp[0]
        self.sex = tmp[1]
        self.region = tmp[2]
        self.last_action = tmp[3]
        self.course_id = tmp[4]
        self.term_id = tmp[5]
        self.select_time = tmp[6]

class Research:
    def __init__(self, line):
        self.js = json.loads(line)
        self.user_id = self.js['member_id']
        self.term_id = self.js['term_id']
        self.active_name = self.js['active_name']

    def hash(self):
        return self.user_id + self.term_id

class Test:
    def __init__(self, line):
        tmp = line.strip().split('\t')
        self.test_id = tmp[0]
        self.test_time = tmp[1]
        self.test_type = tmp[2]
        self.term_id = tmp[3]
        self.chapter_id = tmp[4]
        self.deadline = tmp[5]
        self.sub_total_score = tmp[6]
        self.obj_total_score = tmp[7]
        self.avg_score = tmp[8]
        self.exam_id = tmp[9]
    
    def useful(self):
        tp = int(self.test_type)
        if tp > 1 and tp < 6:
            return True
        else:
            return False
    def getFullScore(self):
        return float(self.sub_total_score) + float(self.obj_total_score)

class Exam:
    def __init__(self, line):
        tmp = line.strip().split('\t')
        self.exam_id = tmp[0]
        self.term_id = tmp[1]
        self.avg_score = tmp[2]
        self.total_score = tmp[3]
        self.submit_count = tmp[4]
    
    def getFullScore(self):
        return float(self.total_score)

class Wda:
    def __init__(self, line):
        tmp = line.strip().split('\t')
        self.logtime = tmp[0]
        self.user_id = tmp[1]
        self.session_id = tmp[2]
        self.ip = tmp[3]
        self.region = tmp[4]
        self.url = tmp[5]
        self.refer = tmp[6]

    def setTermID(self, terms):
        self.term_id = '-1'
        for term in terms:
            if term.inTerm(self.logtime):
                self.term_id = term.term_id
        return self

    def hash(self):
        return self.user_id + self.term_id


def loadTerm(folder):
    with open(folder + 'moc_term', 'r', encoding='utf-8') as f:
        ret = []
        for line in f.readlines():
            ret.append(Term(line))
        return ret

def loadUser(folder):
    with open(folder + 'user_tag_value', 'r', encoding='utf-8') as f:
        ret = []
        for line in f.readlines():
            ret.append(User(line))
        return ret

def loadTest(folder):
    with open(folder + 'moc_test', 'r', encoding='utf-8') as f:
        ret = []
        for line in f.readlines():
            ret.append(Test(line))
        return ret

def loadExam(folder):
    with open(folder + 'moc_exam', 'r', encoding='utf-8') as f:
        ret = []
        for line in f.readlines():
            ret.append(Exam(line))
        return ret

def loadResearch(folder):
    with open(folder + 'mooc_research', 'r', encoding='utf-8') as f:
        ret = []
        for line in f.readlines():
            ret.append(Research(line))
        return ret

def loadWda(folder, terms):
    with open(folder + 'wda_mooc', 'r', encoding='utf-8') as f:
        ret = []
        for line in f.readlines():
            ret.append(Wda(line).setTermID(terms))
        return ret

