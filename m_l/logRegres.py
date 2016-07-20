#coding=utf-8
"""
"""
import sys 
from math import exp
from numpy import mat

def loadDataSet():
	"""
	生成初始测试数据集
	打开文件读取数据，每行的前2个值分别是X1和X2，第三个值是数据对应的类别标签。次外，为了方便计算，该函数还将X0的值设置为1.0
	"""
	dataMat = []; labelMat = []
	fr = open('./test_data/testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat,labelMat


def sigmoid(inX): 
	return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn,classLabels):
	"""
	梯度上升算法
	"""
	dataMatrix = mat(dataMatIn)#将一个list转换为矩阵
	labelMat = mat(classLabels).transpose()
	m,n = shape(dataMatrix)
	alpha = 0.001
	maxCycles = 500
	weights = ones((n,1))
	for k in range(maxCycles):
		h = sigmoid(dataMatrix*weights)
		error = (labelMat - h)
		weights = weights + alpha * dataMatrix.transpose()*error
	return weights



mat = mat([1,2,3])
print mat,type(mat),mat.transpose(),mat.shape
# loadDataSet()

