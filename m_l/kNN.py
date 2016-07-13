#coding=utf-8
from numpy import * 
import operator 

DATING_FILE_PATH = './net_date/datingTestSet.txt'

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

# createDataSet()
def classify0(inX,dataSet,labels,k):
	"""
	该函数有4个输入参数： 
	用于分类的输入向量是inX,输入的训练样本集为dataSet,标签向量为labels  最后的参数k表示用于选择最近邻居的数目
	其中标签向量的元素数目和矩阵dataSet的行数相同

	#steps 
	对未知类别属性的数据集中的每个点依次执行以下操作：
	(1)计算已知类别数据集中的点与当前点之间的距离
	(2)按照距离递增次序排序  
	(3)选取与当前点距离最小的k个点
	(4)确定前k个点出现频率最高的类别作为当前点的预测分类

	"""
	dataSetSize = dataSet.shape[0]
	print dataSetSize
	diffMat = tile(inX,(dataSetSize,1)) - dataSet#这里要使用tile来扩展备份数组的维度 这样可以不用使用循环去求得和各个点之间的差值
	print diffMat
	sqDiffMat = diffMat ** 2 #vector calc 
	print sqDiffMat
	print type(sqDiffMat) #<type 'numpy.ndarray'>
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5 #is the end of ola calc 
	sortedDistIndicies = distances.argsort()##这个argsort用于在ndarray上 用于判断元素的排名位置
	print sortedDistIndicies
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(),
		key=operator.itemgetter(1),reverse=True)#asc not desc 
	return sortedClassCount[0][0]



"""

group,labels = createDataSet()#当然 这里的group 是我们的数据集  这里的label是标签，如果数据集越大我们能预测的越准确
print classify0([0,0],group,labels,3)# you can use [0,0] or another value 

"""





"""
把由多列特征值和标签构成的文本文件进行解析为矩阵
"""
def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines() #这种就直接读取了所有文件到内存中了
	numberOfLines = len(arrayOLines)#获取文件行数 
	# print numberOfLines
	returnMat = zeros((numberOfLines,3)) #构建0矩阵  ndarray   this is just init a ndarray ,and after then we can use 
	# print returnMat
	classLabelVector = []
	index = 0 
	for line in arrayOLines:
		line = line.strip()##去除两侧空格   
		listFromLine = line.split('\t')	#这里不是根据空格哦而是根据换档(Tab)
		# print listFromLine
		returnMat[index,:] = listFromLine[0:3]#set the value of the ndarray 
		# print listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))##create the label 
		index += 1 
	return returnMat,classLabelVector


"""
归一化特征值

需要归一化原因：在使用k-近邻算法的时候，由于计算的是标准差,所以有可能存在某些特征值距离so max,例如我们想知道在本次相亲飞机飞的时间为A(5600)的时候，
那么这次相亲的成败。那么可能在数据集中有很多值与A相比波动很大，这样该特征值在计算的时候会导致样本之间的距离（样本由多个特征值构成）变的很大,
虽然你可以认为多个特征值的权重是一样的，但是其中的某个特征不能如此严重的影响计算结果

ndarray's method min and max used as find the max or min value,when using in 1 dim ,it will return the max or the min value ,
when using in n (n>1) dimension it will fetch the max or the min value of the specify axis (using the input integer argument)
"""
def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)#这个dataset是由多个特征值列构成的n维数组，由于这里的axis参数均为0，所以获取到的都是在最内部的维度上取得的max and min  也就是取得各个列上的最大最小值
	ranges = maxVals - minVals#求得的是一个特征值,求得各个特征值的波动峰谷差
	normDataSet = zeros(shape(dataSet))#init a zero ndarray, 
	m = dataSet.shape[0]#get the first dimension of the ndarray 
	normDataSet = dataSet - tile(minVals,(m,1))#殷帅：使用到了tile 进行数组的冗余扩展，这样是为了补齐维度，便于后续的运算
	normDataSet = normDataSet/tile(ranges,(m,1))#yinshuai:这里自己画图脑补下吧，这里计算出来之后所有的特征值列的值都是在0-1 之间的，这个用一个比例来表示的,
	#总体来说使用上面这种均减去min值的方式很好，这样一来值为max的那个值被归一为了1，那么值越接近最大值，那么其归一化之后越接近1
	return normDataSet,ranges,minVals



"""
测试分类，作为完整程序验证分类器
机器学习算法的一个很重要的工作就是评估算法的正确率，通常我们只提供已有数据的90%作为训练样本来训练分类器，而使用其余的10%的数据去测试分类器
"""
# def datingClassTest():
# 	hoRatio = 0.10# 10% data to test the function of the  classify 
# 	datingDataMat ,datingLabels = file2matrix(DATING_FILE_PATH)
# 	normMat,ranges,minVals = autoNorm(datingDataMat)
# 	m = normMat.shape[0]
# 	numTestVects = int(m*hoRatio)
# 	errorCount = 0.0
# 	for i in range(numTestVects):
# 		classifierResult = classify0(normMat[i,:],normMat(numTestVects))




"""
约会网站预测函数
"""
def classifyPerson():
	resultList = ['not at all','in small doses','in large doses']
	percentTats = float(raw_input("percentage of time playing video games? "))
	ffMiles = float(raw_input("frequent flier miles earned per year ?"))
	iceCream = float(raw_input("liters of ice cream consumed per year? "))
	datingDataMat,datingLabels = file2matrix(DATING_FILE_PATH)
	normMat,ranges,minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles,percentTats,iceCream])
	classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
	print "You will probably like this person : ", resultList[classifierResult-1]


if __name__ == '__main__':
	classifyPerson()

