#coding=utf-8
"""
function:使用朴素贝叶斯对电子邮件进行分类
step:	
	(1)收集数据：提供文本文件
	(2)
	(3)
	(4)
"""
import sys
from bayes import *
def textParse(bigString):
	"""
	文本分析，这里不使用String.split() 这种根据空格的切分的方式，因为这会把标点落在单词里面
	"""
	import re
	listOfTokens = re.split(r'\W*',bigString)#分隔符是除单词，数字,下划线外的任意字符串,其实就是切分之后只留下字母，数字下划线而已
	return [tok.lower() for tok in listOfTokens if len(tok) > 2]#这里过滤掉长度小于less than 2的单词



def spamTest():#
	docList = []; classList = []; fullText = []
	#构造了测试数据集合，从垃圾邮件和正常邮件中分析出文本列表
	for i in range(1,26):#totally 26 files    spam file list is the set of rubbish email
		wordList = textParse(open('test_data/email/spam/%d.txt' % i).read())#using open(filepath).read() will load all content of the file into memory 
		docList.append(wordList)
		fullText.extend(wordList)#the extend method will change the origin value  这里貌似只是把垃圾邮件中出现的单词汇总了
		classList.append(1)
		wordList = textParse(open('test_data/email/ham/%d.txt' % i).read())
		docList.append(wordList)
		classList.append(0)

	vocabList = createVocabList(docList)#汇总所有出现过的单词(normal email and spam)
	trainingSet = range(50); testSet = []
	# print trainingSet
	"""
	下面是构建一个测试集和一个训练集，两个集合中的邮件都是随机选出来的。
	(1)在本例中一共有50封邮件，并不是很多，其中的10封邮件被随机选择为测试集 
	(2)分类器所需要的概率计算只是利用训练集中的文档完成的
	(3)接下来，随机选择10个文件，选出的数字所对应的文档被添加到测试集，同时也将其从训练集中剔除，这种随机选择数据的一部分作为训练集，而剩余部分作为测试集的过程称作留存交叉验证
	"""
	for i in range(10):#随机构建训练集
		# print 'trainingSet len is ',len(trainingSet)
		randIndex = int(random.uniform(0,len(trainingSet))) #uniform() 方法将随机生成下一个实数(not int)，它在[x,y]范围内。
		# print randIndex
		testSet.append(trainingSet[randIndex])
		del(trainingSet[randIndex])
	trainMat = []; trainClasses = []#初始化训练矩阵　和相应的训练类别
	for docIndex in trainingSet:
		trainMat.append(setOfWords2Vec(vocabList,docList[docIndex]))
		trainClasses.append(classList[docIndex])
	print len(trainClasses)
	print trainClasses
	p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
	errorCount = 0
	for docIndex in testSet:
		wordVector = setOfWords2Vec(vocabList,docList[docList])
		if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
			errorCount += 1
	print 'the error rate is :' + float(errorCount)/len(testSet)




###################################################################################P35



# print bigString.split()
# sys.exit(0)
# print textParse(bigString)
spamTest()
