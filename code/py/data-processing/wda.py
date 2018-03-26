#! python2
#coding=utf8

def get_wda_type(str):
    if 'content?type=detail&id=' in str:
        str = str.split('content?type=detail&id=')[1]
        ret = ''
        for ch in str:
            if ch >= '0' and ch <= '9':
                ret = ret + ch
            else:
                break
        return '1', ret
    elif 'quiz?id=' in str:
        str = str.split('quiz?id=')[1]
        ret = ''
        for ch in str:
            if ch >= '0' and ch <= '9':
                ret = ret + ch
            else:
                break
        return '2', ret
    elif 'examSubjective?eid=' in str:
        str = str.split('examSubjective?eid=')[1]
        ret = ''
        for ch in str:
            if ch >= '0' and ch <= '9':
                ret = ret + ch
            else:
                break
        return '3', ret
    else:
        return '-1', '-1'

class Wda:
    def __init__(self, row_wda):
        self.timestamp = row_wda[0]
        self.uid = row_wda[1]
        self.sid = row_wda[2]
        self.url = row_wda[5]
        # type 1 : video
        # type 2 : test
        # type 3 : exam
        # type 10 : other
        self.type, self.content = get_wda_type(self.url)
        if self.content == '':
            print 'vvvvvvvvvvvvvvvvvvvvv'
            print self.url
            print '^^^^^^^^^^^^^^^^^^^^^'

