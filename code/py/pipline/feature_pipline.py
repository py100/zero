#! python3
#coding=utf8

import output_manager
import fileInter

class Unit:
    def __init__(self, _uid, _tid):
        self.userID = _uid
        self.termID = _tid
        self.rss = []
        self.wdas = []

    def tostr(self):
        ret = self.userID
        ret = ret + '\t' + self.termID
        ret = ret + '\t' + str(self.homework_count)
        ret = ret + '\t' + str(self.hw_ratio_sum)
        ret = ret + '\t' + str(self.hw_ratio_avg)
        ret = ret + '\t' + str(self.test_count)
        ret = ret + '\t' + str(self.tt_ratio_sum)
        ret = ret + '\t' + str(self.tt_ratio_avg)
        ret = ret + '\t' + str(self.video_count)
        ret = ret + '\t' + str(self.video_ratio_sum)
        ret = ret + '\t' + str(self.video_ratio_avg)
        ret = ret + '\t' + str(self.exam_count)
        ret = ret + '\t' + str(self.exam_ratio_sum)
        ret = ret + '\t' + str(self.exam_ratio_avg)
        return ret

    def hasExam(self):
        if self.exam_count > 0:
            return True
        else:
            return False

    def hash(self):
        return self.userID+self.termID

    def addRS(self, _rs):
        self.rss.append(_rs)

    def addWda(self, _wda):
        self.wdas.append(_wda)

    def getRSbyActiveName(self, name):
        ret = []
        for rs in self.rss:
            if rs.active_name == name:
                ret.append(rs)
        return ret

    def getWdabyType(self, _type):
        ret = []
        for wda in self.wdas:
            if wda.type == name:
                ret.append(wda)
        return ret

    def extract_homework(self, fpip):
        single_hw = self.getRSbyActiveName(u'作业记录')
        total_hw = self.getRSbyActiveName(u'作业总分')
        self.homework_count = 0
        self.hw_ratio_sum = 0.0
        self.hw_ratio_avg = 0.0

        for hw in single_hw:
            if 'score' in hw.js['attribute']:
                self.homework_count = self.homework_count + 1
                self.hw_ratio_sum = self.hw_ratio_sum + fpip.calratio(hw.js)

        if self.homework_count != 0:
            self.hw_ratio_avg = self.hw_ratio_sum / self.homework_count

        self.total_homework_score = '0'
        if len(total_hw) == 1:
            for hw in total_hw:
                self.total_homework_score = hw.js['attribute']['score']
        return len(single_hw), len(total_hw)

    def extract_test(self, fpip):
        single_tt = self.getRSbyActiveName(u'测验记录')
        total_tt = self.getRSbyActiveName(u'测验总分')
        self.test_count = 0
        self.tt_ratio_sum = 0.0
        self.tt_ratio_avg = 0.0

        for tt in single_tt:
            if 'score' in tt.js['attribute']:
                self.test_count = self.test_count + 1
                self.tt_ratio_sum = self.tt_ratio_sum + fpip.calratio(tt.js)

        if self.test_count != 0:
            self.tt_ratio_avg = self.tt_ratio_sum / self.test_count

        self.total_test_score = '0'
        if len(total_tt) == 1:
            for tt in total_tt:
                self.total_test_score = tt.js['attribute']['score']
        return len(single_tt), len(total_tt)

    def extract_exam(self, fpip):
        exams = self.getRSbyActiveName(u'考试记录')

        self.exam_count = 0
        self.exam_total = 0.0
        self.exam_ratio_sum = 0.0
        self.exam_ratio_avg = 0.0

        for ex in exams:
            if 'score' in ex.js['attribute']:
                self.exam_count = self.exam_count + 1
                self.exam_total = self.exam_total + float(ex.js['attribute']['score'])
                self.exam_ratio_sum = self.exam_ratio_sum + fpip.calratio_exam(ex.js)
        if self.exam_count != 0:
            self.exam_ratio_avg = self.exam_ratio_sum / self.exam_count
        return len(exams)

    def extract_video(self, fpip):
        videos = self.getRSbyActiveName(u'视频记录')
        self.video_count = 0
        self.video_ratio_sum = 0.0
        self.video_ratio_avg = 0.0

        for vi in videos:
            if vi.js['attribute']['operation'] == 'duration':
                self.video_count = self.video_count + 1
                self.video_ratio_sum += fpip.calratio_video(vi.js)

        if self.video_count != 0:
            self.video_ratio_avg = self.video_ratio_sum / self.video_count


class fpipline:
    def __init__(self, _courseID, _om):
        self.courseID = _courseID
        self.om = _om

    def init(self):
        self.loadUnit()
        self.om.runtimel('finish init unit\ncourse ID: {}\ntotal Unit: {}\n'.format(self.courseID,
            len(self.units)))
        self.touchResearch()
        # self.touchWda()
        self.touchTest()
        self.touchExam()
        print('touchWda ok')

    def extract(self):
        self.om.runtimel('start extracting feature')

        tracker_hw_s = dict()
        tracker_hw_t = dict()

        tracker_tt_s = dict()
        tracker_tt_t = dict()

        tracker_exam = dict()

        for key in self.units:
            # homework
            s, t = self.units[key].extract_homework(self)
            if s not in tracker_hw_s:
                tracker_hw_s[s] = 0
            tracker_hw_s[s] = tracker_hw_s[s] + 1
            if t not in tracker_hw_t:
                tracker_hw_t[t] = 0
            tracker_hw_t[t] = tracker_hw_t[t] + 1

            # test
            s, t = self.units[key].extract_test(self)
            if s not in tracker_tt_s:
                tracker_tt_s[s] = 0
            tracker_tt_s[s] = tracker_tt_s[s] + 1
            if t not in tracker_tt_t:
                tracker_tt_t[t] = 0
            tracker_tt_t[t] = tracker_tt_t[t] + 1

            # video
            self.units[key].extract_video(self)

            # exam
            s = self.units[key].extract_exam(self)
            if s not in tracker_exam:
                tracker_exam[s] = 0
            tracker_exam[s] = tracker_exam[s] + 1

        print('------tracker info of homework------')
        print(tracker_hw_s)
        print(tracker_hw_t)
        print('----------------end-----------------')
        print('--------tracker info of test--------')
        print(tracker_tt_s)
        print(tracker_tt_t)
        print('----------------end-----------------')
        print('--------tracker info of exam--------')
        print(tracker_exam)
        print('----------------end-----------------')
        self.om.runtimel('finish extracting feature')

    def save(self):
        outputFile = self.om.getDestFolder(self.courseID) + 'feature.out'
        print(outputFile)
        with open(outputFile, 'w', encoding='utf-8') as f:
            for key in self.units:
                if self.units[key].hasExam():
                    f.write(self.units[key].tostr() + '\n')
        self.om.runtimel('save feature [' + self.courseID + '] ok')

    def loadUnit(self):
        self.units = dict()
        users = fileInter.loadUser(self.om.getDestFolder(self.courseID))
        for user in users:
            tmp = Unit(user.user_id, user.term_id)
            self.units[tmp.hash()] = tmp

    def touchResearch(self):
        researches = fileInter.loadResearch(self.om.getDestFolder(self.courseID))
        for rs in researches:
            if rs.hash() in self.units:
                self.units[rs.hash()].addRS(rs)

    def touchWda(self):
        terms = fileInter.loadTerm(self.om.getDestFolder(self.courseID))
        wdas = fileInter.loadWda(self.om.getDestFolder(self.courseID), terms)
        print(len(wdas))
        for wda in wdas:
            if wda.hash() in self.units:
                self.units[wda.hash()].addWda(wda)

    def touchTest(self):
        temp = fileInter.loadTest(self.om.getDestFolder(self.courseID))
        self.tests = dict()
        for t in temp:
            if t.useful():
                if t.test_id in self.tests:
                    self.om.runtimeEr('touch test error, find same test id of {}'.format(t.test_id))
                self.tests[t.test_id] = t

    def touchExam(self):
        temp = fileInter.loadExam(self.om.getDestFolder(self.courseID))
        self.exams = dict()
        for e in temp:
            if e.exam_id in self.exams:
                self.om.runtimeEr('touch exam error, find same exam id of {}'.format(e.exam_id))
            self.exams[e.exam_id] = e

    def calratio(self, js):
        sc = float(js['attribute']['score'])
        test_id = js['attribute']['test_id']
        if test_id not in self.tests:
            self.om.runtimeEr('test id [{}] not found'.format(test_id))
            return 0.0
        else:
            fullsc = self.tests[test_id].getFullScore()
            return sc * 1.0 / fullsc

    def calratio_exam(self, js):
        sc = float(js['attribute']['score'])
        exam_id = js['attribute']['exam_id']
        if exam_id not in self.exams:
            self.om.runtimeEr('exam id [{}] not found'.format(exam_id))
            return 0.0
        else:
            fullsc = self.exams[exam_id].getFullScore()
            return sc * 1.0 / fullsc

    def calratio_video(self, js):
        duration = float(js['attribute']['value'])
        full = float(js['attribute']['video_duration'])
        return duration * 1.0 / full

