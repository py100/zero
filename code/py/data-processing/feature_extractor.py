#! python2
#coding=utf8

import sys
from user import *
from test import *
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
            return wda[1] + term[0]
    else:
        return '-1'

def extract(folder):
    term_list = read_formated_file(folder + FILE_TERM)
    users_list = read_formated_file(folder + FILE_USER_TAG_VALUE)
    user_dict = dict()
    for row in users_list:
        # User(userid, courseid, termid)
        user = User(row[0], row[4], row[5])
        user_dict[user.hash()] = user
    print 'total dict len is', len(users_list)

    wdas = read_formated_file(folder + FILE_WDA)
    lessons = read_formated_file(folder + FILE_LESSON)
    raw_tests = read_formated_file(folder + FILE_TEST)
    tests = [Test(row) for row in raw_tests]
    # for key in user_dict:
    #     print key

    for row_wda in wdas:
        code = getcode(row_wda, term_list)
        # print code
        if code == '-1':
            continue
        if code in user_dict:
            wda = Wda(row_wda)
            user_dict[code].update(wda)

    print len(user_dict)
    counter = 0
    for key in user_dict:
        if user_dict[key].__str__() != '':
            # print user_dict[key]
            counter = counter + 1
    print counter
    out = open('feature.out', 'w')
    for key in user_dict:
        ret = map(str, user_dict[key].generate_feature(tests))
        out.write(str(user_dict[key].userid) + '\t' + '\t'.join(ret) + '\n')
    out.close()

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

