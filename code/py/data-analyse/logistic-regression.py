#! python2
#coding=utf8

from numpy import *
from tool import *

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5: return 1.0
    else: return 0.0

def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = shape(dataMatrix)
    weights = ones(n)   #initialize to all ones
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.0001    #apha decreases with iteration, does not 
            randIndex = int(random.uniform(0,len(dataIndex)))#go to 0 because of the constant
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights

def classifier():
    raw_data = read_formated_file('feature.out')
    data = filter_data(raw_data)
    data_train, data_test = split_data(data, 0.8)
    trainingSet = []; trainingLabels = []

    for line in data_train:
        lineArr =[]
        for i in range(8):
            lineArr.append(float(line[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(line[8]))
    trainWeights = stocGradAscent1(array(trainingSet), trainingLabels, 1000)
    errorCount = 0; numTestVec = 0.0
    for line in data_test:
        numTestVec += 1.0
        lineArr =[]
        for i in range(8):
            lineArr.append(float(line[i]))
        if int(classifyVector(array(lineArr), trainWeights))!= int(line[8]):
            errorCount += 1
    errorRate = (float(errorCount)/numTestVec)
    print "the error rate of this test is: %f" % errorRate
    return errorRate

def main():
    classifier()

if __name__ == '__main__':
    main()
