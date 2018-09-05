#! python3
#coding=utf8

import datetime
import os

DATAFOLDER = '/home/poore/data/'
LOGROOT = '/home/poore/runtime/'

class logManager:
    def __init__(self):
        self.root = LOGROOT + datetime.datetime.now().strftime('%d-%H-%M-%S') + '/'
        self.logroot = self.root + 'log/'
        self.modelroot = self.root + 'model/'
        os.makedirs(self.logroot)
        os.makedirs(self.modelroot)
        self.runtimelog = open(self.logroot + 'runtime.log', 'w', encoding = 'utf-8')
        self.runtimeerr = open(self.logroot + 'runtime.err', 'w', encoding = 'utf-8')

    def __del__(self):
        self.runtimelog.close()
        self.runtimeerr.close()

    def runtimel(self, str):
        self.runtimelog.write(datetime.datetime.now().strftime('[%H-%M-%S]'))
        self.runtimelog.write(str + '\n')

    def runtimee(self, str):
        # self.runtimeerr.write(datetime.datetime.now().strftime('[%H-%M-%S]'))
        self.runtimeerr.write(str + '\n')



def main():
    lm = logManager()
    lm.runtimel('test')
    lm.runtimee('error')

if __name__ == '__main__':
    main()

