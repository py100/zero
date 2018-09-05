#! python3
#coding=utf8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

import itertools

import pandas as pd
import tensorflow as tf
import numpy as np
import logmanager

tf.logging.set_verbosity(tf.logging.INFO)

COLUMNS = ['hw_cnt', 'hw_ratio_sum', 'hw_ratio_avg',
        'tt_cnt', 'tt_ratio_sum', 'tt_ratio_avg', 'video_cnt', 'video_ratio_sum',
        'video_ratio_avg', 'post_count', 'timemse', 'ex_cnt', 'ex_ratio_avg']

FEATURES = ['hw_cnt', 'hw_ratio_sum', 'hw_ratio_avg',
        'tt_cnt', 'tt_ratio_sum', 'tt_ratio_avg', 'video_cnt', 'video_ratio_sum',
        'video_ratio_avg', 'post_count', 'timemse', 'ex_cnt']

LABEL = 'ex_ratio_avg'

class basic:
    def __init__(self, _dataset, _lm, _cid):
        self.dataset = _dataset
        self.lm = _lm
        self.cid = _cid
        self.result = dict()

    def train(self):
        pass

    def getresult(self):
        return self.result




def get_input_fn(data_set, num_epochs=None, shuffle=True):
      return tf.estimator.inputs.pandas_input_fn(
              x=pd.DataFrame({k: data_set[k].values for k in FEATURES}),
              y=pd.Series(data_set[LABEL].values),
              num_epochs=num_epochs,
              shuffle=shuffle)


class dnn(basic):
    def __init__(self, _dataset, _lm, _cid):
        super(dnn, self).__init__(_dataset, _lm, _cid)


    def train(self):
        training_set, self.test_set = train_test_split(self.dataset[COLUMNS], test_size=0.3)
        feature_cols = [tf.feature_column.numeric_column(k) for k in FEATURES]


        self.regressor = tf.estimator.DNNRegressor(feature_columns=feature_cols,
                hidden_units=[7, 7],
                model_dir=self.lm.modelroot + 'dnn/' + self.cid)

        self.regressor.train(input_fn=get_input_fn(training_set), steps=5000)
        ev = self.regressor.evaluate(
                input_fn=get_input_fn(self.test_set, num_epochs=1, shuffle=False))
        
        self.result = ev
        # pred_y = self.regressor.predict(
        #         input_fn=get_input_fn(self.test_set, num_epochs=1, shuffle=False))
        # print(pred_y)
        # 
        # for a, i in zip(pred_y, self.test_set.index):
        #     print(a)
        #      print(self.test_set.loc[i].values)


class linear(basic):
    def __init__(self, _dataset, _lm, _cid):
        super(linear, self).__init__(_dataset, _lm, _cid)

    def train(self):
        training_set, self.test_set = train_test_split(self.dataset[COLUMNS], test_size=0.3)
        feature_cols = [tf.feature_column.numeric_column(k) for k in FEATURES]

        self.regressor = tf.estimator.LinearRegressor(feature_columns=feature_cols,
                model_dir=self.lm.modelroot + 'linear/' + self.cid)

        self.regressor.train(input_fn=get_input_fn(training_set), steps=5000)

        ev = self.regressor.evaluate(
                input_fn=get_input_fn(self.test_set, num_epochs=1, shuffle=False))

        self.result = ev
        # pred_y = self.regressor.predict(
        #         input_fn=get_input_fn(self.test_set, num_epochs=1, shuffle=False))
        # 
        # for a, i in zip(pred_y, self.test_set.index):
        #     print(a)
        #     print(self.test_set.loc[i].values)
        # print(self.regressor.get_variable_names())


class dnnlinear(basic):
    def __init__(self, _dataset, _lm, _cid):
        super(dnnlinear, self).__init__(_dataset, _lm, _cid)

    def train(self):
        training_set, self.test_set = train_test_split(self.dataset[COLUMNS], test_size=0.3)
        feature_cols = [tf.feature_column.numeric_column(k) for k in FEATURES]

        self.regressor = tf.estimator.LinearRegressor(feature_columns=feature_cols,
                model_dir=self.lm.modelroot + 'combined/' + self.cid)

        self.regressor.train(input_fn=get_input_fn(training_set), steps=5000)

        ev = self.regressor.evaluate(
                input_fn=get_input_fn(self.test_set, num_epochs=1, shuffle=False))

        self.result = ev
        # pred_y = self.regressor.predict(
        #         input_fn=get_input_fn(self.test_set, num_epochs=1, shuffle=False))
        # print(pred_y)
        # 
        # for a, i in zip(pred_y, self.test_set.index):
        #     print(a)
        #      print(self.test_set.loc[i].values)
        # 

