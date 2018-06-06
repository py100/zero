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
        ret = ret + '\t' + str(self.hw_sum)
        ret = ret + '\t' + str(self.hw_avg)
        ret = ret + '\t' + str(self.test_count)
        ret = ret + '\t' + str(self.tt_sum)
        ret = ret + '\t' + str(self.tt_avg)
        ret = ret + '\t' + str(self.video_count)
        ret = ret + '\t' + str(self.video_sum)
        ret = ret + '\t' + str(self.video_avg)
        ret = ret + '\t' + str(self.post_count)
        ret = ret + '\t' + str(self.timemse)
        ret = ret + '\t' + str(self.exam_count)
        ret = ret + '\t' + str(self.exam_ratio_sum*100.0)
        ret = ret + '\t' + str(self.exam_ratio_avg*100.0)
        return ret

    def tostrratio(self):
        ret = self.userID
        ret = ret + '\t' + self.termID
        ret = ret + '\t' + str(self.homework_count)
        ret = ret + '\t' + str(self.hw_ratio_sum*100.0)
        ret = ret + '\t' + str(self.hw_ratio_avg*100.0)
        ret = ret + '\t' + str(self.test_count)
        ret = ret + '\t' + str(self.tt_ratio_sum*100.0)
        ret = ret + '\t' + str(self.tt_ratio_avg*100.0)
        ret = ret + '\t' + str(self.video_count)
        ret = ret + '\t' + str(self.video_ratio_sum*100.0)
        ret = ret + '\t' + str(self.video_ratio_avg*100.0)
        ret = ret + '\t' + str(self.post_count)
        ret = ret + '\t' + str(self.timemse)
        ret = ret + '\t' + str(self.exam_count)
        ret = ret + '\t' + str(self.exam_ratio_sum*100.0)
        ret = ret + '\t' + str(self.exam_ratio_avg*100.0)
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

    def extract_homework(self, fpip):
        single_hw = self.getRSbyActiveName(u'作业记录')
        total_hw = self.getRSbyActiveName(u'作业总分')
        self.homework_count = 0
        self.hw_ratio_sum = 0.0
        self.hw_ratio_avg = 0.0
        self.hw_sum = 0.0
        self.hw_avg = 0.0

        for hw in single_hw:
            if 'score' in hw.js['attribute']:
                self.homework_count = self.homework_count + 1
                self.hw_ratio_sum = self.hw_ratio_sum + fpip.calratio(hw.js, ratio=True)
                self.hw_sum += fpip.calratio(hw.js, ratio=False)

        if self.homework_count != 0:
            self.hw_ratio_avg = self.hw_ratio_sum / self.homework_count
            self.hw_avg = self.hw_sum / self.homework_count

        return len(single_hw), len(total_hw)

    def extract_test(self, fpip):
        single_tt = self.getRSbyActiveName(u'测验记录')
        total_tt = self.getRSbyActiveName(u'测验总分')
        self.test_count = 0
        self.tt_ratio_sum = 0.0
        self.tt_ratio_avg = 0.0

        self.tt_sum = 0.0
        self.tt_avg = 0.0

        for tt in single_tt:
            if 'score' in tt.js['attribute']:
                self.test_count = self.test_count + 1
                self.tt_ratio_sum = self.tt_ratio_sum + fpip.calratio(tt.js,ratio=True)
                self.tt_sum += fpip.calratio(tt.js,ratio=False)

        if self.test_count != 0:
            self.tt_ratio_avg = self.tt_ratio_sum / self.test_count
            self.tt_avg = self.tt_sum / self.test_count

        return len(single_tt), len(total_tt)

    def extract_exam(self, fpip):
        exams = self.getRSbyActiveName(u'考试记录')

        self.exam_count = 0
        self.exam_ratio_sum = 0.0
        self.exam_ratio_avg = 0.0
        self.exam_sum = 0.0
        self.exam_avg = 0.0

        for ex in exams:
            if 'score' in ex.js['attribute']:
                self.exam_count = self.exam_count + 1
                self.exam_ratio_sum = self.exam_ratio_sum + fpip.calratio_exam(ex.js,ratio=True)
                self.exam_sum = self.exam_sum + fpip.calratio_exam(ex.js,ratio=False)
        if self.exam_count != 0:
            self.exam_ratio_avg = self.exam_ratio_sum / self.exam_count
            self.exam_avg = self.exam_sum / self.exam_count
        return len(exams)

    def extract_video(self, fpip):
        videos = self.getRSbyActiveName(u'视频记录')
        self.video_count = 0
        self.video_ratio_sum = 0.0
        self.video_ratio_avg = 0.0
        self.video_sum = 0.0
        self.video_avg = 0.0

        for vi in videos:
            if vi.js['attribute']['operation'] == 'duration':
                self.video_count = self.video_count + 1
                self.video_ratio_sum += fpip.calratio_video(vi.js,ratio=True)
                self.video_sum += fpip.calratio_video(vi.js,ratio=False)

        if self.video_count != 0:
            self.video_ratio_avg = self.video_ratio_sum / self.video_count
            self.video_avg = self.video_sum / self.video_count

    def extract_post(self, fpip):
        posts = self.getRSbyActiveName(u'讨论记录')
        self.post_count = len(posts)

    def extract_msetime(self, fpip):
        terms = fileInter.loadTerm(fpip.om.getDestFolder(fpip.courseID))
        term = terms[0]
        for t in terms:
            if t.term_id == self.termID:
                term = t
        tss = []
        for wda in self.wdas:
            tmp = fpip.caltimestamp(wda, term)
            if tmp != None:
                tss.append(tmp)
        cnt = [0 for x in range(5)]
        for ts in tss:
            cnt[int(ts/20)] += 1
        sum = 0.0
        for i in range(5):
            sum += cnt[i]
        avg = sum / 5.0
        s2 = 0.0
        for i in range(5):
            s2 += (cnt[i] - avg)**2
        self.timemse = s2 / 5

class fpipline:
    def __init__(self, _courseID, _om):
        self.courseID = _courseID
        self.om = _om

    def init(self):
        self.loadUnit()
        self.om.runtimel('finish init unit\ncourse ID: {}\ntotal Unit: {}\n'.format(self.courseID,
            len(self.units)))
        self.touchResearch()
        self.touchWda()
        self.touchTest()
        self.touchExam()
        print('init ok')

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

            # post
            self.units[key].extract_post(self)

            # mse of timestamps
            self.units[key].extract_msetime(self)

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

    def caltimestamp(self, wda, term):
        t = int(wda.logtime)
        start = int(term.start_time)
        end = int(term.end_time)
        if t < start or t > end:
            return None
        else:
            return (t-start) * 100.0 / (end - start)

    def calrate(self):
        positive_units = []
        for key in self.units:
            if self.units[key].hasExam():
                positive_units.append(self.units[key])
        terms = fileInter.loadTerm(self.om.getDestFolder(self.courseID))
        timestamps = []
        for unit in positive_units:
            for wda in unit.wdas:
                for term in terms:
                    if term.term_id == wda.term_id:
                        tmp = self.caltimestamp(wda, term)
                        if tmp != None:
                            timestamps.append(tmp)
        print('*******************')
        print(len(timestamps))
        print('*******************')
        outputFile = self.om.getDestFolder(self.courseID) + 'timestamps.out'
        with open(outputFile, 'w', encoding='utf-8') as f:
            for t in timestamps:
                f.write(str(t))
                f.write('\n')

    def save(self):
        outputFile = self.om.getDestFolder(self.courseID) + 'feature_ratio.out'
        print(outputFile)
        with open(outputFile, 'w', encoding='utf-8') as f:
            for key in self.units:
                if self.units[key].hasExam():
                    f.write(self.units[key].tostrratio() + '\n')
        outputFile = self.om.getDestFolder(self.courseID) + 'feature.out'
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

    def calratio(self, js, ratio=True):
        sc = float(js['attribute']['score'])
        test_id = js['attribute']['test_id']
        if test_id not in self.tests:
            self.om.runtimeEr('test id [{}] not found'.format(test_id))
            return 0.0
        else:
            fullsc = self.tests[test_id].getFullScore()
            if ratio:
                return sc * 1.0 / fullsc
            else:
                return sc * 1.0

    def calratio_exam(self, js,ratio=True):
        sc = float(js['attribute']['score'])
        exam_id = js['attribute']['exam_id']
        if exam_id not in self.exams:
            self.om.runtimeEr('exam id [{}] not found'.format(exam_id))
            return 0.0
        else:
            fullsc = self.exams[exam_id].getFullScore()
            if ratio:
                return sc * 1.0 / fullsc
            else:
                return sc * 1.0

    def calratio_video(self, js,ratio=True):
        duration = float(js['attribute']['value'])
        full = float(js['attribute']['video_duration'])
        if ratio:
            return duration * 1.0 / full
        else:
            return duration * 1.0

