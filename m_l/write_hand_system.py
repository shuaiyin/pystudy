#coding=utf-8
from numpy import * 
from os import listdir #用于列出给定目录的文件名
import operator
import sys
"""
k-邻近算法
advantage: most easy and most valid algor 
disadvantage: (1)need losts of mem space and using lots of running time
			  (2)无法给出任何数据的基础结构信息，因此我们也无法知晓平均实例样本和典型实例样本具有什么特征


构造使用k-近邻分类器的手写识别系统 这里只能识别数字0-9  需要识别的数字已经用图形处理软件
处理成具有相同的色彩和大小：宽和高32*32px(white-black)
这里采用文本格式存储图片，虽然文本格式存储图像不能有效的利用内存空间，但是为了方便吧
这里没有做归一化处理，这是因为都是0 1 数据哦
"""
TRAIN_DATA_PATH = './test_data/trainingDigits'
TEST_DATA_PATH = './test_data/testDigits'


"""
将图像转换为向量，由于txt文件中存储的都是32*32个0,1
这里我们可以把一个32*32的二进制图像矩阵转换为1*1024的向量
"""
def img2vector(filename):
	returnVect = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0,32*i+j] = int(lineStr[j])
	return returnVect



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
手写数字识别系统的测试代码
yinshuai:

test:其实这里把32*32的测试数据转换为1*1024的数据后（横着的数据哦）作为一次测试的输入
train:训练数据是由之前的经验数据构成，之前的上百个数据组成n*1024的训练矩阵，那么也就是n行了
xxx:这个时候就要把这个测试数据进行tile 使其由一行数据扩展为可以和训练数据行数相称的行数，这样才可以执行欧拉公式哦。。 
"""
def handwritingClassTest():
	hwLabels = []
	trainingFileList = listdir(TRAIN_DATA_PATH)
	m = len(trainingFileList)
	trainingMat = zeros((m,1024))#init ndarray which the shape is (m,1024)
	for i in range(m):
		fileNameStr = trainingFileList[i]
		#可以看下这里的文件命名方式0_25.txt 其中的0表示图片的值，25表示第25种畸形展现方式
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:] = img2vector(TRAIN_DATA_PATH + '/' + fileNameStr)#如此自信的使用":" 是因为之前我们已经开了这个0矩阵空间了，况且这个图片也是1*1024的哦
	print trainingMat.shape #(1934,1024)
	testFileList = listdir(TEST_DATA_PATH)
	errorCount = 0.0 #float calc 
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])#the class of the test data row 
		vectorUnderTest = img2vector(TEST_DATA_PATH + '/' + fileNameStr)
		print vectorUnderTest.shape #(1,1024)
		classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)#fetch k=3
		print "the classifier came back with : %d, the real answer is: %d" % (classifierResult,classNumStr)
		if classifierResult != classNumStr:	errorCount += 1.0
	print "\nthe total number of errors is : %d " % errorCount
	print "\nthe total error rate is : %f" % (errorCount/float(mTest))











if __name__ == '__main__':
	img_file_path  = TRAIN_DATA_PATH + '/0_100.txt'
	testVector = img2vector(img_file_path)#1*1024 vector 
	handwritingClassTest()


