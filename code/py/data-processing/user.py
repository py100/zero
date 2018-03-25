#! python

class User:
    def __init__(self, userid, courseid, termid):
        self.userid = userid
        self.courseid = courseid
        self.termid = termid
        learn_video_actions = []
        do_test_actions = []
        learn_text_actions = []
        learn_others_actions = []

    def load_data(self, wda_list):
        pass
    
    def extract_feature(self):
        pass

    def __str__(self):
        pass
    
    def hash(self):
        return self.userid + self.termid
