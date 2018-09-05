#! python3
#coding=utf8

import pandas as pd

SOURCE_ROOT = '/home/poore/data/all/'

SOURCE_COLUMNS = ['uid', 'termid', 'hw_cnt', 'hw_ratio_sum', 'hw_ratio_avg',
        'tt_cnt', 'tt_ratio_sum', 'tt_ratio_avg', 'video_cnt', 'video_ratio_sum',
        'video_ratio_avg', 'post_count', 'timemse', 'ex_cnt', 'ex_ratio_sum', 'ex_ratio_avg']

COLUMNS = ['hw_cnt', 'hw_ratio_sum', 'hw_ratio_avg',
        'tt_cnt', 'tt_ratio_sum', 'tt_ratio_avg', 'video_cnt', 'video_ratio_sum',
        'video_ratio_avg', 'post_count', 'timemse', 'ex_cnt', 'ex_ratio_avg']

X_COLUMNS = ['hw_cnt', 'hw_ratio_sum', 'hw_ratio_avg', 'tt_cnt', 
        'tt_ratio_sum', 'tt_ratio_avg', 'video_cnt', 'video_ratio_sum',
        'video_ratio_avg', 'post_count', 'timemse', 'ex_cnt']

Y_COLUMNS = ['ex_ratio_avg']


class FileInter:
    def __init__(self, id_list):
        self.root = SOURCE_ROOT
        self.paths = dict()
        for cid in id_list:
            self.paths[cid] = self.root + 'feature_' + cid + '.out'

    def getfilenpath(self, cid):
        return self.paths[cid]

    def loadData(self, cid):
        fname = self.getfilenpath(cid)
        data = pd.read_csv(fname, sep='\t',header=None, names=SOURCE_COLUMNS)
        n, m = data.shape
        X = data[X_COLUMNS]
        Y = data[Y_COLUMNS]
        A = data[COLUMNS]
        return X, Y, A

def main():
    data = pd.read_csv('~/data/feature_199001.out', sep='\t',header=None)
    print(data.head())
    n, m = data.shape

if __name__ == '__main__':
    main()

