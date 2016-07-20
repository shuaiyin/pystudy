#coding=utf-8
"""
advantage:
	(1)在数据较少的情况下仍然有效，可以处理多类别问题
disadvantage:
	(1)对于输入数据的准备方式较为敏感

适用数据类型：标称型数据
"""
from numpy import *
import sys

def loadDataSet():
	"""
	创建了一些实验样本，该函数返回的第一个变量是进行词条切分后的文档集合，这些文档来自斑点犬爱好者留言板
	该函数返回的第二个变量是一个类别标签的集合，这里有两类，侮辱性和非侮辱性
	这些文本的类别由人工标注，这些标注信息用于训练程序以便自动检测侮辱性语言

	"""
	postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
				['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
				['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
				['stop', 'posting', 'stupid', 'worthless', 'garbage'],
				['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
				['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
	classVec = [0,1,0,1,0,1]#1代表侮辱性文字，0代表正常言论 那么这个矢量中存储的就是上面的每个评论的人工判断的性质
	return postingList,classVec


def createVocabList(dataSet):
	"""
	用于创建一个包含在所有文档中出现的不重复词的"列表"
	"""
	vocabSet = set([])
	for document in dataSet:
		vocabSet = vocabSet | set(document)
	return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
	"""
	function:我们知道了所有的评论所组成的单词列表,那么我们拿出其中的一条评论出来，然后对其中的单词依次在之前的单词列表上做标记
	在该函数中，我们将每个词的出现与否作为一个特征，这可以被描述为词集模型(self-of-words-model)
	input param:
			vocabList: 所有出现的词汇的集合哦 
			inputSet  输入的某个数据集合（例如对狗狗的某条评论）
	输入参数为词汇表及某个文档，输出的是文档向量，向量的每一元素为1或0，分别表示词汇表中的单词在输入文档中是否出现
	"""
	returnVec = [0] * len(vocabList)
	# print returnVec
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1#这里只要单词在文档中出现，那么就给我们的总词汇表进行标记，而不清楚到底出现了几次的情况，这就是词集模型
		else:
			print "the word : %s is not in my Vocabulary! " % word
	return returnVec


def setOfWords2VecMN(vocabList,inputSet):
	"""
	如果一个词在文档中出现不止一次，这可能意味着这比词集模型包含更多的信息，这种方法被称为词袋模型(bag-of-words model)
	在词袋模型中，每个单词可以出现多次 
	"""
	returnVec = [0] * len(vocabList)
	for word in inputSet:
		if word in inputSet:
			returnVec[vocabList.index(word)] += 1
	return returnVec




def trainNB0(trainMatrix,trainCategory):
	"""
	代码函数中输入参数为文档矩阵trainMatrix 以及由每篇文档类别标签所构成的向量trainCategory
	yinshuai:这里的trainMatrix不再是最开始的评论言论，而是经过单词集比对之后的训练矩阵
	return:
		p0Vect 单词表中normal言论的概率向量
		p1Vect 单词表中侮辱性言论的概率向量
		pAbusive  侮辱性言论所占所有言论的比例
	"""
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])#32
	#这里的trainCategory 是训练数据给出的结果类，那么0为正常言论，1为侮辱性的言论，sum(trainCategory)得到的是侮辱性的总数， 那么the next line 求得的是侮辱型言论的比例
	pAbusive = sum(trainCategory)/float(numTrainDocs)#计算侮辱性言论所占所有言论的比例,了解这里的sum 充分利用了 侮辱性1的标记来计算侮辱性言论总数
	"""
	#利用贝叶斯分类器对文档进行分类时，要计算多个概率的乘积以获得文档属于某个类别的概率,即计算P(w0|1)*P(w1|1)*P(w2|1) 如果其中的一个概率为0，那么最后的乘积也为0
	#为了降低这种影响，可以将所有词的出现次数初始化为1，并将分组初始化为2
	#这里的zeros是使用的numpy当中的类，用于生成一个零数组,
	p0Num = zeros(numWords)
	p1Num = zeros(numWords)
	p0Denom = 0.0#这里的p1Denom是计算的正常言论中单词总数,使用浮点数是为了后面的除法
	p1Denom = 0.0#这里的p1Denom是计算的侮辱性言论中单词总数,
	"""
	#为了降低这种影响，可以将所有词的出现次数初始化为1，并将分组初始化为2
	p0Num = ones(numWords)#numpy中的方法，用于创建单位数组,
	p1Num = ones(numWords)
	p0Denom = 2.0 #
	p1Denom = 2.0

	for i in range(numTrainDocs):
		# print trainMatrix[i]
		if trainCategory[i] == 1:#这里的trainMatrix和trainCategory是相对应的，这里class=1即用于判断如果这条言论是侮辱性言论
			p1Num += trainMatrix[i]#对于一条评论，假设其是侮辱性言论，那么将这条训练向量累加到初始的p1Num零向量上,这里的数组的矢量运算，不是list运算
			p1Denom += sum(trainMatrix[i])#由于每条评论的长度是不同的，所以在单词表中出现的标记次数也是不同的。
		else:
			p0Num += trainMatrix[i]#对于一条评论，假设其是正常言论，那么将这条训练向量累加到初始的p0Num零向量上,这里的数组的矢量运算，不是list运算
			p0Denom += sum(trainMatrix[i])
	"""
	#不再使用下面这种方式是为了避免下溢出问题，这是由于太多很小的数相乘造成的
	#当计算乘积P(w0|ci)*P(w1|ci)*P(w2|ci)...P(wn|ci)时，由于大部分因子都非常小，所以程序会下溢出或者的单不出确的答案（可以尝试相乘许多很小的数，最后四舍五入之后为0）
	p1Vect = p1Num/p1Denom#
	p0Vect = p0Num/p0Denom
	"""
	p1Vect = log(p1Num/p1Denom)
	p0Vect = log(p0Num/p0Denom)
	return p0Vect,p1Vect,pAbusive


def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
	"""
	input argument:
		vec2Classify: 要分类的向量vec2Classify(要知道这个待分类的向量是如何得到的)
		p0Vec,p1Vec,pClass1 使用函数trainNB0 计算得到的三个概率
	"""
	p1 = sum(vec2Classify * p1Vec) + log(pClass1)#
	p0 = sum(vec2Classify * p0Vec) + log(1.0-pClass1)
	if p1 > p0: return 1
	else: return 0 


def testNB():
	listOPosts,listClasses = loadDataSet()#获取测试数据集
	myVocabList = createVocabList(listOPosts)#从所有评论中汇总出一份单词表
	trainMat = []
	for postinDoc in listOPosts:
		trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
	p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
	testEntry = ['love','my','dalmation']#dalmation  斑点
	thisDoc = array(setOfWords2Vec(myVocabList,testEntry))
	print testEntry,'classified as :',classifyNB(thisDoc,p0V,p1V,pAb)
	testEntry = ['stupid','garbage']
	thisDoc = array(setOfWords2Vec(myVocabList,testEntry))
	print testEntry,'classified as :',classifyNB(thisDoc,p0V,p1V,pAb)





testNB()
"""
['love', 'my', 'dalmation'] classified as : 0
['stupid', 'garbage'] classified as : 1

"""
# sys.exit(0)



# listOPosts,listClasses = loadDataSet()#GET THE TESE DATA
# myVocabList = createVocabList(listOPosts)#get the all vovalary !!
# trainMat = []#init the train matrix 
# for postinDoc in listOPosts:
# 	trainMat.append(setOfWords2Vec(myVocabList,postinDoc))

# # print trainMat[0]
# trainNB0(trainMat,listClasses)
# p0V,p1V,pAb = trainNB0(trainMat,listClasses)
# print pAb
# print p0V,p1V
"""
0.5
[ 0.04166667  0.04166667  0.04166667  0.          0.          0.04166667
  0.04166667  0.04166667  0.          0.04166667  0.04166667  0.04166667
  0.04166667  0.          0.          0.08333333  0.          0.
  0.04166667  0.          0.04166667  0.04166667  0.          0.04166667
  0.04166667  0.04166667  0.          0.04166667  0.          0.04166667
  0.04166667  0.125     ]

[ 0.          0.          0.          0.05263158  0.05263158  0.          0.
  0.          0.05263158  0.05263158  0.          0.          0.
  0.05263158  0.05263158  0.05263158  0.05263158  0.05263158  0.
  0.10526316  0.          0.05263158  0.05263158  0.          0.10526316
  0.          0.15789474  0.          0.05263158  0.          0.          0.        ]


[-2.56494936 -2.56494936 -2.56494936 -3.25809654 -3.25809654 -2.56494936
 -2.56494936 -2.56494936 -3.25809654 -2.56494936 -2.56494936 -2.56494936
 -2.56494936 -3.25809654 -3.25809654 -2.15948425 -3.25809654 -3.25809654
 -2.56494936 -3.25809654 -2.56494936 -2.56494936 -3.25809654 -2.56494936
 -2.56494936 -2.56494936 -3.25809654 -2.56494936 -3.25809654 -2.56494936
 -2.56494936 -1.87180218] 
[-3.04452244 -3.04452244 -3.04452244 -2.35137526 -2.35137526 -3.04452244
 -3.04452244 -3.04452244 -2.35137526 -2.35137526 -3.04452244 -3.04452244
 -3.04452244 -2.35137526 -2.35137526 -2.35137526 -2.35137526 -2.35137526
 -3.04452244 -1.94591015 -3.04452244 -2.35137526 -2.35137526 -3.04452244
 -1.94591015 -3.04452244 -1.65822808 -3.04452244 -2.35137526 -3.04452244
 -3.04452244 -3.04452244]

"""




# sys.exit(0)
# print listOPosts[3]
# # sys.exit(0)
# print setOfWords2Vec(myVocabList,listOPosts[3])#['stop', 'posting', 'stupid', 'worthless', 'garbage']

# print '-----------this is the new test-------------------'
# print myVocabList








