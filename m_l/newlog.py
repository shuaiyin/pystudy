#coding=utf-8

"""
预测数值型数据：回归

用线性回归找到最佳拟合曲线

优点：结果易于理解，计算上不复杂　　
缺点：对非线性的数据拟合不好　　
适用数据类型: 数值型和标称型数据

回归的一般方法：
(1)收集数据：采用任意方法收集数据
(2)准备数据：回归需要数值型数据，标称型数据将被转换为二值型数据。
(3)分析数据：绘出数据的可视化二维图将有助于对数据做出理解与分析，在采用缩减法得到新回归系数后，可以将新拟合线绘在图上作为对比
(4)训练算法：找出回归系数
(5)测试算法：使用R2或者预测值和数据的拟合度来分析模型的效果
(6)使用算法：使用回归，可以在给定一个输入的时候预测出一个数值，这是对分类算法的提升，因为这样可以预测连续型数据而不仅仅是离散的类别标签
"""

from numpy import * 

import sys 

ls = [[1,2],[3,4]]
# print mat(ls).I
print linalg.det(ls)
sys.exit(0)


def loadDataSet(fileName):
	numFeat = len(open(fileName).readline().split('\t')) -1 
	dataMat = []; labelMat = []
	fr = open(fileName)
	for line in fr.readlines():
		lineArr = []
		curLine = line.strip().split('\t')
		for i in range(numFeat):
			lineArr.append(curLine[i])
		dataMat.append(lineArr)
		labelMat.append(float(curLine[-1]))
	return dataMat,labelMat

def standRegres(xArr,yArr):
	"""
	用来计算最佳拟合直线
	input argument:
		xArr:dataMat
		yArr:labelMat
	"""
	xMat = mat(xArr); yMat = mat(yArr).T
	xTx = xMat.T * xMat
	if linalg.det(xTx) == 0.0:
		print "This matrix is singular,can not do inverse"
		return 
	ws = xTx.I * (xMat.T*yMat)
	return ws

# filePath = './test_data/ex0.txt'
# xArr,yArr = loadDataSet(filePath)
# print yArr

def lwlr(testPoint,xArr,yArr,k=1.0):
	xMat = mat(xArr); yMat = mat(yArr).T 
	m  = shape(xMat)[0]
	weights = mat(eye(m))
	for j in range(m):
		diffMat = testPoint - xMat[j,:]
		weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
	xTx = xMat.T * (weights * xMat)
	if linalg.det(xTx) == 0.0:
		print "this matrix is singular, can not do reverse"
		return 
	ws = xTx.I * (xMat.T * (weights * yMat))#.I操作符实现了矩阵求逆的运算
	return testPoint * ws 
