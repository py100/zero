#! python2
#coding=utf-8

from numpy import *
from tool import *

FILES = [\
        u'20001_filtered.out',\
        u'21011_filtered.out',\
        u'43002_filtered.out',\
        u'45002_filtered.out'
        ]

def main():
    for f in FILES:
        raw_data = read_formated_file(f)
        num_reg = len(raw_data)
        has_actions = filter_data(raw_data)
        num_act = len(has_actions)
        num_exam = 0
        for line in raw_data:
            if line[9] == '1':
                num_exam = num_exam + 1
        print num_reg, num_act, num_exam, num_exam*100.0/num_act




if __name__ == '__main__':
    main()
