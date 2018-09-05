#! python3
#coding=utf8

import pandas
import logmanager
import sk
import tff

X_COLUMNS = ['hw_cnt', 'hw_ratio_sum', 'hw_ratio_avg', 'tt_cnt', 
        'tt_ratio_sum', 'tt_ratio_avg', 'video_cnt', 'video_ratio_sum',
        'video_ratio_avg', 'post_count', 'timemse', 'ex_cnt']

class ModelInterface:
    def __init__(self, _x, _y, _dataset, _lib, _tp, _lm, _cid, mk=None):
        self.x = _x
        self.y = _y
        self.dataset = _dataset
        self.lib = _lib
        self.tp = _tp
        self.lm = _lm
        self.cid = _cid
        self.mk = mk
        if mk != None:
            tmp = []
            for i in range(len(X_COLUMNS)):
                if ((mk>>i)&1) == 1:
                    tmp.append(X_COLUMNS[i])
            self.x = self.x[tmp]


    def init(self):
        if self.lib == 'sk' and self.tp == 'linear':
            self.model = sk.linear(self.x, self.y)
        elif self.lib == 'sk' and self.tp == 'ridge':
            self.model = sk.ridge(self.x, self.y)
        elif self.lib == 'sk' and self.tp == 'elasticnet':
            self.model = sk.elasticnet(self.x, self.y)
        elif self.lib == 'tf' and self.tp == 'dnn':
            self.model = tff.dnn(self.dataset, self.lm, self.cid)
        elif self.lib == 'tf' and self.tp == 'linear':
            self.model = tff.linear(self.dataset, self.lm, self.cid)
        elif self.lib == 'tf' and self.tp == 'comb':
            self.model = tff.dnnlinear(self.dataset, self.lm, self.cid)
        else:
            self.model = sk.linear(self.x, self.y, self.cid)

    def run(self):
        self.model.train()
        if self.lib == 'sk':
            self.model.evaluate()

    def showresult(self, save=False):
        res = self.model.getresult()
        res['course_id'] = self.cid
        res['dataset_size'] = len(self.dataset)
        if save == True:
            self.lm.runtimel('===========================')
            self.lm.runtimel('@using lib : {}'.format(self.lib))
            self.lm.runtimel('@model type : {}'.format(self.tp))
            for key in res:
                self.lm.runtimel('@@ {} : {}'.format(key, res[key]))
        else:
            print('===========================')
            print('@using lib : {}'.format(self.lib))
            print('@model type : {}'.format(self.tp))
            for key in res:
                print('@@ {} : {}'.format(key, res[key]))
        if self.mk != None:
            self.lm.runtimee('{} {}'.format(self.mk, res['mse']))
