#coding=utf-8
from numpy import * 

FILE_PATH = './test_data/testSet2.txt'


def loadDataSet(fileName):
	dataMat = []
	fr = open(fileName)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fitLine = map(float,curLine)
		dataMat.append(fltLine)
	return dataMat


print loadDataSet(FILE_PATH)



