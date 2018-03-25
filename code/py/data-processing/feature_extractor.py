#! python2
#coding=utf8

import sys
from user import *
sys.path.append('..')
from utility.utility import *

BASE_DATA_DIR = u'C:/Users/poore/Desktop/毕设/data/2016-11-01'
FOLDERS = [u'20001_filtered']
FILE_COMMENT = u'moc_comment.txt'
FILE_COURSE = u'moc_course.txt'
FILE_EXAM = u'moc_exam.txt'
FILE_FORUM = u'moc_forum.txt'
FILE_LESSON = u'moc_lesson.txt'
FILE_LESSON_UNIT = u'moc_lesson_unit.txt'
FILE_ME = u'moc_mutual_evaluate.txt'
FILE_MED = u'moc_mutual_evaluate_detail.txt'
FILE_POST = u'moc_post.txt'
FILE_POST_DETAIL = u'moc_post_detail.txt'
FILE_REPLY = u'moc_reply.txt'
FILE_TERM = u'moc_term.txt'
FILE_TEST = u'moc_test.txt'
FILE_USER_TAG_VALUE = u'user_tag_value.txt'
FILE_WDA = u'wda_mooc.txt'

OUTPUT_FOLDER = u'output'

def getcode(wda, term_list):
    for term in term_list:
        if int(wda[0]) >= int(term[2]) and int(wda[0]) <= int(term[3]):
            return term[0]
    else:
        return '-1'

def extract(folder):
    term_list = read_formated_file(folder + FILE_TERM)
    users_list = read_formated_file(folder + FILE_USER_TAG_VALUE)
    user_dict = dict()
    for row in users_list:
        user = User(row[0], row[4], row[5])
        user_dict[user.hash()] = user
        #for term in term_list:
        #    if term[0] == user.termid:
        #        ret.append(load_user_wda(user, term[2], term[3], folder))
        #        break
    
    wdas = read_formated_file(folder + FILE_WDA)
    ttt = []
    for wda in wdas:
        code = getcode(wda, term_list)
        if code == '-1':
            continue
        if code not in ttt:
            ttt.append(code)
        # wda_record = analyse_wda(wda)
        # user_dict[code].update(wda_record)
    print ttt

    """
    fout = open(folder + OUTPUT_FOLDER + '/' + 'features.txt')
    for feature in ret:
        fout.write(feature)
    fout.close()
    """

def main():
    # a = readfile(FOLDERS[0], FILE_EXAM)
    # print a
    for folder in FOLDERS:
        extract(BASE_DATA_DIR + '/' + folder + '/')

if __name__ == '__main__':
    main()

