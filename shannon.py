# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 16:13
# @Author  : Matthew
# @Site    : 
# @File    : shannon.py
# @Software: PyCharm
from math import log
def calcShannonEnt(dataset):
    numEntries=len(dataset)
    labelCounts={}
    for featVec in dataset:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
    #print labelCounts
    return shannonEnt

def createdataset():
    dataset=[
        [1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']
    ]
    label=['no surfacing','flippers']
    return dataset,label

def splitDataset(dataset,axis,value):
    retDataset=[]
    for featVec in dataset:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataset.append(reducedFeatVec)
    return retDataset

def chooseBestFeature(dataset):
    numFeatures=len(dataset[0])-1
    baseEntroy=calcShannonEnt(dataset)
    bestInforGain=0.0
    bestFeature=-1
    for i in range(numFeatures):
        featlist=[example[i] for example in dataset]
        #print featlist
        uniquevals=set(featlist)
        newEntroy=0.0
        for value in uniquevals:
            subdataset=splitDataset(dataset,i,value)
            #print value,i,subdataset
            prob=len(subdataset)/float(len(dataset))
            newEntroy+=prob*calcShannonEnt(subdataset)
            print value,i,subdataset,prob,newEntroy,calcShannonEnt(subdataset)
            #print newEntroy
        infoGain=baseEntroy-newEntroy
        if infoGain>bestInforGain:
            bestInforGain=infoGain
            bestFeature=i
    return bestFeature

if __name__=='__main__':
    mydat,label=createdataset()
    #print calcShannonEnt(mydat)
    #print splitDataset(mydat,0,1)
    print chooseBestFeature(mydat)
