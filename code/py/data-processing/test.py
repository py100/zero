#! python2
#coding=utf8

class Test:
    def __init__(self, row, terms):
        self.id = int(row[0])
        if row[5] == '\\N' or int(row[5]) < 0:
            for term in terms:
                if row[3] == term[0]:
                    self.ddl = int(term[3])
        else:
            self.ddl = int(row[5])

