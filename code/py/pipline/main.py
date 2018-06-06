#! python3
#coding=utf8

import output_manager as OM
import ut
import helper
from feature_pipline import fpipline

# MODE = 'develop'
# MODE = 'test'
MODE = 'run'

SOURCE_FOLDER = u'd:/BaiduYunDownload/课程源数据/'
RESEARCH_FILE = SOURCE_FOLDER + 'mooc_research.txt'
om = OM.output_manager(MODE)
hp = helper.Helper(om)

def datapipline(folder, courseID):
    om.runtimel('ready to start data-pipline for ' + courseID)
    ut.columnFilter(folder, om)
    om.runtimel('finish column filter for ' + courseID)
    hp.loadCourseTerm(courseID)
    om.runtimel('successful load Course Term Mapping for ' + courseID)
    # ut.fillMissing(folder, om)
    # om.runtimel('successful filling missing columns for ' + courseID)
    om.runtimel('successful finish data-pipline for ' + courseID)

def featurepipline(courseID):
    om.runtimel('ready to start feature-pipline for ' + courseID)
    fpip = fpipline(courseID, om)
    fpip.init()
    fpip.extract()
    fpip.calrate()
    fpip.save()
    om.runtimel('successful finish feature-pipline for ' + courseID)


def main():
    om.runtimel('main start')
    folderToProcess = ut.get_folder_names(SOURCE_FOLDER)

    folderToProcess = [u'21016', u'85001', u'46016', u'9004', u'20001', u'199001']

    om.runtimel('{} folders to be processed:\n{}'.
            format(len(folderToProcess), folderToProcess.__str__()))

    if MODE == 'develop':
        folderToProcess = folderToProcess[0:1]
    elif MODE == 'test':
        folderToProcess = folderToProcess[0:2]

    for folder in folderToProcess:
        datapipline(SOURCE_FOLDER + folder, folder)

    if MODE != 'develop':
        ut.splitResearch(RESEARCH_FILE, folderToProcess, om, hp)
        om.runtimel('finish split research file')

    for courseID in folderToProcess:
        featurepipline(courseID)

    om.runtimel('main end')


if __name__ == '__main__':
    main()

