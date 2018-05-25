#! python3
#coding=utf8

import datetime
import os

BASE = u'd:/dataroot/'

class output_manager:
    def __init__(self, mode):
        self.mode = mode
        if self.mode == 'develop':
            self.root = BASE + 'develop/'
            self.logroot = self.root + 'log/'
            self.runtimelog = open(self.logroot + 'runtimelog.txt', 'w')
            self.destfolders = dict()
        else:
            self.root = BASE + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '/'
            os.makedirs(self.root)
            self.logroot = self.root + 'log/'
            os.makedirs(self.logroot)
            self.runtimelog = open(self.logroot + 'runtimelog.txt', 'w')
            self.destfolders = dict()

    def __del__(self):
        self.runtimelog.close()
        print('cal del func')

    def createResearch(self, courses):
        self.rsfilestreams = dict()
        for cid in courses:
            self.rsfilestreams[cid] = open(self.root + cid + '/mooc_research', 'w', encoding='utf-8')

    def closeResearch(self):
        for cid in self.rsfilestreams:
            self.rsfilestreams[cid].close()
        self.rsfilestreams = dict()

    def writeRS(self, cid, line):
        if cid in self.rsfilestreams:
            self.rsfilestreams[cid].write(line.strip()+'\n')

    def runtimel(self, str):
        self.runtimelog.write(datetime.datetime.now().strftime('[%H-%M-%S]'))
        self.runtimelog.write(str + '\n')

    def runtimeEr(self, str):
        self.runtimelog.write(datetime.datetime.now().strftime('[%H-%M-%S][Error]'))
        self.runtimelog.write(str + '\n')

    def setDestFolder(self, cid):
        self.destfolders[cid] = self.root + cid + '/'
        if self.mode != 'develop':
            os.makedirs(self.destfolders[cid])

    def getDestFolder(self, cid):
        return self.destfolders[cid]

