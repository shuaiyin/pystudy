#coding=utf-8
import matplotlib.pyplot as plt 
from numpy import mat

def plotBestFit(wei):
	"""
	"""
	import matplotlib.pyplot as plt 
	weights = wei.getA()
	dataMat,labelMat = loadDataSet()
	dataArr = array(dataMat)
	n = dataArr.shape[0]
	xcord1 = []; ycord1 = []
	xcord2 = []; ycord2 = []
	for i in range(n):
		if int(labelMat[i]) == 1:
			xcord1.append(dataArr[i,1])
			ycord1.append(dataArr[i,2])
		else:
			xcord2.append(dataArr[i,1])
			ycord2.append(dataArr[i,2])
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xcord1,ycord1,s=30,c='red',maker='s')
	ax.scatter(xcord2,ycord2,s=30,c='green')
	x = arange(-3.0,3.0,0.1)
	y = (-weights[0]-weights[1]*x)/weights[2]
	ax.plot(x,y)
	plt.xlabel('X1')
	plt.xlabel('X2')
	plt.show()

