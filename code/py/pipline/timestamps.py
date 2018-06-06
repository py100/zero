#! python3
#coding=utf8

DIR = 'd:/dataroot/new/'
COURSE_LIST = [ u'21016', u'20001', u'85001', u'199001', u'46016', u'9004' ]

import numpy as np  
import matplotlib.pyplot as plt

def load(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        ret = []
        for l in f.readlines():
            ret.append(float(l))
        return ret

def cal(index):
    data = load(DIR + 'timestamps_' + COURSE_LIST[index] + '.out')
    ret = [0 for i in range(100)]
    for ts in data:
        ret[int(ts)] += 1
    
    for i in range(1,100):
        ret[i] += ret[i-1]
    for i in range(100):
        ret[i] = ret[i] * 100.0 / len(data)
    return ret


def main():
    cnt = []
    for i in range(4):
        cnt.append(cal(i))

    tot = []
    for i in range(100):
        tot.append((cnt[0][i] + cnt[1][i] + cnt[2][i] + cnt[3][i])/4.0)
    x=np.linspace(0.0,100.0,100,endpoint=True)  
    plt.plot(x,cnt[0])  
    plt.plot(x,cnt[1])
    plt.plot(x,cnt[2])
    plt.plot(x,cnt[3])
    # plt.plot(x,tot)
    plt.show()

if __name__ == '__main__':
    main()

