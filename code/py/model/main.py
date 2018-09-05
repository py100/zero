#! python3
#coding=utf8

import logmanager as LM
import pandas
import fileInter as FI
from modelPipline import *

COURSE_LIST = [
        u'21016',
        u'20001',
        u'85001',
        u'199001',
        u'46016',
        u'9004',
        u'000000'
        ]

lm = LM.logManager()

SK_MEANS = ['linear', 'ridge', 'elasticnet']
TF_MEANS = ['linear', 'dnn', 'comb']

processing = [0,1,2,3]

MASK = False

def main():
    fi = FI.FileInter(COURSE_LIST)

    for index in processing:
        x, y, A = fi.loadData(COURSE_LIST[index])
        for mean in SK_MEANS:
            if not mean.startswith('#'):
                if MASK == True:
                    for i in range(1, 2**12):
                        mf = ModelInterface(x, y, A, 'sk', mean, lm, COURSE_LIST[index], mk=i)
                        mf.init()
                        mf.run()
                        mf.showresult(save=True)
                else:
                    mf = ModelInterface(x, y, A, 'sk', mean, lm, COURSE_LIST[index])
                    mf.init()
                    mf.run()
                    mf.showresult(save=True)


        for mean in TF_MEANS:
            if not mean.startswith('#'):
                mf = ModelInterface(x, y, A, 'tf', mean, lm, COURSE_LIST[index])
                mf.init()
                mf.run()
                mf.showresult(save=True)


if __name__ == '__main__':
    main()

