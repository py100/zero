#coding=utf8
file = open('../../../data/2016-11-01/20001/wda_mooc/wda_mooc_20001_sample.txt')
for line in file.readlines():
    print '------------------'
    print len(line.decode('utf-8').split('\t'))
    print '------------------'
    print line.decode('utf-8').split('\t')[16]
    print '------------------'
    for word in line.decode('utf-8').split(chr(1)):
       print word,
    print '------------------'

