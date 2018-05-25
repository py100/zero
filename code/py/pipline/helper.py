#! python3
#coding=utf8

import os
import output_manager as OM
import ut
import fileInter

class Helper:
    def __init__(self, _om):
        self.om = _om
        self.CourseTerm = dict()

    def loadCourseTerm(self, courseID):
        self.CourseTerm[courseID] = []
        terms = fileInter.loadTerm(self.om.getDestFolder(courseID))
        for term in terms:
            self.CourseTerm[courseID].append(term.term_id)

        for d in self.CourseTerm:
            print(d)
            print(self.CourseTerm[d])

    def getCourseID(self, termID):
        for cid in self.CourseTerm:
            if termID in self.CourseTerm[cid]:
                return cid
