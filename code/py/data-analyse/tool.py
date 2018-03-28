#! python2
#coding=utf8

import random

def read_formated_file(path = '', ch = '\t'):
    print 'reading file', path
    return [line.strip().split(ch) for line in open(path).readlines()]

def filter_data(data):
    tmp = [line[1:] for line in data if line[1] != '0']
    ret = []
    for line in tmp:
        fline = map(float, line)
        fline[0] = fline[0] // 1000
        fline[4] = fline[4] // 1000
        fline[5] = fline[5] // 1000
        fline[6] = fline[6] // 1000
        fline[7] = fline[7] // 1000
        if fline[0] > 0.0:
            ret.append(fline)
    return ret

def split_data(data, ratio):
    cnt = int(len(data)*ratio)
    train = []
    print data[0:10]
    for i in range(cnt):
        index = random.randint(0, len(data)-1)
        train.append(data[index])
        del(data[index])
    return train, data

def main():
    test = []
    test.append(['1','2','1'])
    test.append(['0','0','0'])
    print filter_data(test)

if __name__ == '__main__':
    main()
