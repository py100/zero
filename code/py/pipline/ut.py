#! python3
#coding=utf8
import os
import output_manager
import json

wdaconfig = [0, 16, 17, 21, 22, 39, 40]
# 0:logtime 16:uid 17:sid 21:ip 22:region 39:url 40:refer

config = {
        # 'moc_announcement':[],
        'moc_comment':[0, 7, 9, 14, 15],
        # 0:course_id 7:start_time 9:end_time 14:video_id 15:train_id
        # 'moc_course':[],
        'moc_exam':[0, 6, 9, 10, 12],
        # 0:exam_id 6:term_id 9:avg_score 10:total_score 12:submit_count
        'moc_forum':[0, 5, 6, 8],
        # 0:forum_id 5:term_id 6:parent_id 8:type
        'moc_lesson':[0, 6, 7, 8, 9],
        # 0:lesson_id 6:term_id 7:chapter_id 8:content_type 9: content_id
        # 'moc_lesson_content_learn':[],
        'moc_lesson_unit':[0, 5, 6, 7, 8, 9],
        # 0:lesson_unit_id 5:lesson_id 6:chapter_id 7:term_id 8:content_type 9:content_id
        'moc_mutual_evaluate':[0, 3, 4, 5, 6, 8],
        # 0:mutual_evaluate_id 3:evaluator_id 4:test_answerer_id 5:test_id 6:anserform_id 8:orig_score
        'moc_mutual_evaluate_detail':[0, 3, 4],
        # 0:mmed_id 3:test_id 4:evaluate
        'moc_post':[0, 3, 4, 5, 6, 7, 8, 9, 19, 20, 21],
        # 0:post_id 3:type 4:lesson_unit_id 5:forum_id
        # 6:root_forum_id 7:term_id 8:poster_id 9:post_time
        # 19:count_browse 20:count_reply 21:count_vote
        'moc_post_detail':[0, 3],
        # 0:post_detail_id 3:content
        'moc_reply':[0, 3, 6, 7, 8, 14, 15],
        # 0:reply_id 3:replyer_id 6:content 7:count_vote
        # 8:count_comment 14:forum_id 15:term_id
        'moc_term':[0, 3, 4, 6, 23, 24, 25],
        # 0:term_id 3:course_id 4:start_time 6:end_time
        # 23:qualified_count 24:excellent_count 25:enroll_count
        'moc_test':[0, 6, 10, 11, 12, 13, 14, 15, 18, 19],
        # 0:test_id 6:test_time 10:test_type 11:term_id
        # 12:chapter_id 13:deadline 14:sub_total_score
        # 15:obj_total_score 18:avg_score 19:exam_id
        'user_tag_value':[0, 3, 4, 5, 6, 7, 8]
        # 0:user_id 3:sex 4:region 5:last_action 6:course_id
        # 7:term_id 8:select_time
        }

def get_folder_names(path):
    ret = []
    for d in os.listdir(path):
        if os.path.isdir(path+d):
            ret.append(d)
    return ret

def readSingle(file):
    ch = '\t'
    if not file.endswith('.txt'):
        ch = chr(1)
    ret = []
    print(file)
    with open(file, encoding='utf-8') as f:
        for line in f.readlines():
            ret.append(line.strip().split(ch))
    return ret

def readMerge(folder, om):
    files = [f for f in os.listdir(folder) if not f.endswith('.omi')]
    data = []
    for f in files:
        data.extend(readSingle(folder + '/' + f))
    om.runtimel('finish read and merge ' + folder)
    return data


def columnFilter(folder, om):
    om.runtimel('starting filtering ' + folder)
    courseID = folder.split('/')[-1]
    om.setDestFolder(courseID)
    for key in config:
        cf = config[key]
        print(folder)
        data = readMerge(folder + '/' + key, om)
        with open(om.getDestFolder(courseID) + key, 'w', encoding='utf-8') as f:
            for line in data:
                tmp = []
                for index in cf:
                    tmp.append(line[index])
                f.write('\t'.join(tmp) + '\n')

    wdafile = folder + '/wda_mooc_' + courseID + '.txt'
    data = []
    with open(wdafile, encoding='utf-8') as f:
        for line in f.readlines():
            l = line.strip().split('\t')
            tmp = []
            for index in wdaconfig:
                tmp.append(l[index])
            data.append('\t'.join(tmp))

    with open(om.getDestFolder(courseID) + 'wda_mooc', 'w', encoding='utf-8') as f:
        for line in data:
            f.write(line+'\n')


RS_TYPE = [
        u'测验记录',
        u'测验总分',
        u'登录行为',
        u'点赞记录',
        u'进出课程',
        u'考试记录',
        u'视频记录',
        u'讨论记录',
        u'用户总评',
        u'作业记录',
        u'作业总分'
        ]

def splitResearch(rs_file, courses, om, hp):
    om.createResearch(courses)
    with open(rs_file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            d = json.loads(line)
            om.writeRS(hp.getCourseID(d['term_id']), line)
    om.closeResearch()


def main():
    print(get_folder_names(u'd:/BaiduYunDownload/课程源数据/'))
    print(config)
if __name__ == '__main__':
    main()
