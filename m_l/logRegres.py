
#coding=utf-8
"""
 1.换句话说，y也就是我们关系的变量，例如她喜不喜欢你，与多个自变量（因素）有关，例如你人品怎样、车子是两个轮的还是四个轮的、长得胜过潘安还是和犀利哥有得一拼、有千尺豪宅还是三寸茅庐等等，
 我们把这些因素表示为x1, x2,…, xm。那这个女的怎样考量这些因素呢？最快的方式就是把这些因素的得分都加起来，最后得到的和越大，就表示越喜欢。但每个人心里其实都有一杆称，每个人考虑的因素
 不同，萝卜青菜，各有所爱嘛。例如这个女生更看中你的人品，人品的权值是0.6，不看重你有没有钱，没钱了一起努力奋斗，那么有没有钱的权值是0.001等等。我们将这些对应x1, x2,…, xm的权值叫做
 回归系数，表达为θ1, θ2,…, θm。他们的加权和就是你的总得分了。请选择你的心仪男生，非诚勿扰！哈哈。

 2.那么我们可以认为这多个自变量（因素）就是我们的特征列，那么类别列就是我们的关系变量，那么各个自变量给多少权值能最终得到我们的类别列的，那么这个说白了有种根据梯度进行上升后者下降，经过
 多次迭代稳定之后，得到这些稳定系数。

 3.ys:线性回归和ogistic回归有啥区别？ 
 ys:"线性"回归是这种东西：θ1 * X1 +  θ2 * X2 + θ3 * X3 + ..... +  θm * Xm   or   θ.transpose() * X  (这里的 是回归系数向量，这里的X是自变量向量)
 	而logistic回归是一个分类，得出的是一个概率（介于0-1之间），我们往往通过的这个概率来做判定，例如根据概率来判断这个女孩是否喜欢你！！！！！
 csdn:所以说上面的logistic回归就是一个线性分类模型，它与线性回归的不同点在于：为了将线性回归输出的很大范围的数，例如从负无穷到正无穷，压缩到0和1之间，这样的输出值表达为“可能性”才能说服广大民
 众。当然了，把大值压缩到这个范围还有个很好的好处，就是可以消除"特别""冒尖"的变量的影响（不知道理解的是否正确）。而实现这个伟大的功能其实就只需要平凡一举，也就是在输出加一个logistic函数。另外
 ，对于二分类来说，可以简单的认为：如果样本x属于正类的概率大于0.5，那么就判定它是正类，否则就是负类。实际上，SVM的类概率就是样本到边界的距离，这个活实际上就让logistic regression给干了。

 4.先验原理：如果一个项集是频繁的则它的所有子集一定也是频繁的
 一个项集的支持度绝不会超过他的子集的支持度，这个性质也成支持度度量的"反单调性"
 
"""
import sys 
# from math import exp#wrong
from numpy import mat,ones,exp,array,arange ##warnings:虽然math包里面也有exp但是math包里面的不能对matrix做运算，所以需要在numpy中引入这个exp


def loadDataSet():
	"""
	生成初始测试数据集
	打开文件读取数据，每行的前2个值分别是X1和X2，第三个值是数据对应的类别标签。次外，为了方便计算，该函数还将X0的值设置为1.0
	"""
	dataMat = []; labelMat = []#this is not list but matrix
	fr = open('./test_data/testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat,labelMat


def writeFile(content):
	fileHandler = open('./test_data/temp_data.txt','a')
	fileHandler.write(str(content))
	fileHandler.close


def sigmoid(inX): 
	"""
	总述：ys：使用这个函数的目的就是把线性回归转换为logitic回归（0-1之间）
	ys:那么这里为啥还要用这个函数？这个函数的输入参数是什么呢？
	inX = θ1 * X1 +  θ2 * X2 + θ3 * X3 + ..... +  θm * Xm  
	<<===>>>
	inX = θ.transpose() * X  (这里的 是回归系数向量，这里的X是自变量向量)
	那么当然这里的X向量当中的值经常是参差不齐的，例如男子的存款这一特征值，在进行运算之后,得到的"线性回归值"可能范围不受控制哦，
	那么通过“逻辑,逻辑，逻辑“回归，就是把这些东西整到0-1之间这个概率上，是不是有点逻辑的韵味，是不是更加直观呢
    Logistic回归用于二分类问题，面对具体的"二分类"问题，比如明天是否会下雨。人们通常是估计，并没有十足的把握。因此用概率来表示再适合不过了。
    Logistic本质上是一个基于条件概率的判别模型(DiscriminativeModel)。利用了Sigma函数值域在[0,1]这个特性。

	"""
	return 1.0/(1+exp(-inX))



def gradAscent(dataMatIn,classLabels):
	"""
	梯度上升算法,
	该函数有2个参数，第一个参数是dataMatIn,它是一个2维Numpy数组，每列分别代表不同的特征(身高，家产，颜值等),每行则代表每个训练样本(民间找到的脑残粉，拜金女等样本)
	我们这里采用的是100个样本的简单数据集，它包含了2个特征X1和X2，再加上第0维特征X0，所以dataMatIn里存放的是100*3的矩阵
	第二个参数是类别标签，它是一个1*100的行向量

	"""
	dataMatrix = mat(dataMatIn)#将一个list转换为矩阵
	labelMat = mat(classLabels).transpose()#为了便于矩阵计算，需要将该行向量转换为列向量，使用转置
	# print labelMat
	# sys.exit(0)
	m,n = dataMatrix.shape
	alpha = 0.001#变量alpha是向目标移动的步长
	maxCycles = 5000#myCycles是迭代次数
	weights = ones((n,1))#每次回归系数初始化为1,也就是最开始迭代的时候，我们认为所有变量（特征值）的权值都是1，也就是最开始公平对待
	for k in range(maxCycles):#在for循环迭代完成之后，将返回训练好的回归系数
		h = sigmoid(dataMatrix*weights)#当然这里的weights是ones单位数组，然而dataMatrix是矩阵，这里可以得到的就是矩阵可以乘以数组，可以乘以列表等，只要满足相乘条件即可，感觉就像是矩阵乘以矩阵是的
		# print 'logis  is ',h
		error = (labelMat - h)#这里的error就是一种误差率，线性回归值与训练值之间的误差向量
		"""
		writeFile(error)
		writeFile('\n*******************\n')
		"""
		weights = weights + alpha * dataMatrix.transpose()*error#这里处理的是矩阵运算### 使用alpha*gradient（梯度）更新回归系数值
		# print 'the weigths is ',weights  上面这个公式直接使用的是计算权重的化简公式
	return weights


def plotBestFit(wei):
    """
    这里画出数据集（使用scatter绘制散点图）和logistic回归最佳拟合直线（使用plot绘制）
    画出决策边界
    """
    import matplotlib.pyplot as plt 
    weights = wei.getA()##getA is a method the change numpy.matrx into numpy.ndarray
    dataMat,labelMat = loadDataSet()
    dataArr = array(dataMat)#the type of dataMat is list, using array to change list to ndarray
    n = dataArr.shape[0]
    xcord1 = []; ycord1 = []#这里的xcord1 ycord1分别用于存储label为1的时候的特征值（有两个特征值，这里用x，y分别存储）
    xcord2 = []; ycord2 = []#里的xcord2 ycord2分别用于存储label为0的时候的特征值（有两个特征值，这里用x，y分别存储）
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    fig = plt.figure()#Figure(640x480)
    #这里的add_subplot中的111三个数字分别代表把划分分割成1行1列，图像画在从左到右从上到下的第1块，当然这里只是划分了一块，所以就只有一个地方放图
    #更加直观的例子，例如参数为349,那么则将画布分割成3行4列（3*4=12）块，图像被放置到藏左到右从上到下的第9块上.如果要在一个图表中绘制多个子图，可使用 subplot。
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')##scatter 用于点绘制，需要传入轴坐标list 
    ax.scatter(xcord2,ycord2,s=30,c='green')#这里的marker表示绘制点的时候使用的形状，为s表示square（正方形），默认是圆形，这里的s表示size，对于圆形图案来说，那么就是半径这种东西了吧，我认为
    x = arange(-3.0,3.0,0.1)#这里的定义了这条最佳拟合直线的x轴坐标数组 
    """
    回忆sigmoid函数在x=0处，函数的值为0.5，这个位置就是两个分类的分界处，因此我们设定 θ0 * X0 + θ1 * X1 +  θ2 * X2 =0,然后解除X2和X1的关系式
    （即分割线方程，注意X0=1.0)
	当然这里的X1，X2分别用x,y坐标表示
    """
    y = (-weights[0]-weights[1]*x)/weights[2]#
    ax.plot(x,y)#这里的plot用于绘制直线图，不同于scatter用于绘制散点图，但是二者都是输入两组array
    plt.xlabel('X1')
    plt.xlabel('X2')
    plt.show()



def stocGradAscent0(dataMatrix, classLabels):
    """
    随机梯度上升算法和梯度上升算法在代码上很相似，但也有一些区别：
    第一,后者的变量h和误差error都是向量，而前者则全是数值；
    第二，前者没有矩阵的转换过程，所有的变量数据类型都是numpy数组
    he say: each update of the param only rely on the new one simple sample !!!!
    """
    m,n = dataMatrix.shape
    alpha = 0.01
    weights = ones(n)   #initialize to all ones   the type is ndarray 
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights


dataArr,labelMat = loadDataSet()#this type of dataArr is list
# weights = stocGradAscent0(array(dataArr),labelMat)
dataMatrix = array(dataArr)
m,n = dataMatrix.shape
alpha = 0.01
weights = ones(n)
for i in range(m):
    h = sigmoid(sum(dataMatrix[i] * weights))
    error = labelMat[i] - h
    weights = weights + alpha * error * dataMatrix[i]

print weights
print type(weights)

# sys.exit(0)
plotBestFit(mat(weights))
sys.exit(0)

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

def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5: return 1.0
    else: return 0.0

def colicTest():
    frTrain = open('horseColicTraining.txt'); frTest = open('horseColicTest.txt')
    trainingSet = []; trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscent1(array(trainingSet), trainingLabels, 1000)
    errorCount = 0; numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainWeights))!= int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount)/numTestVec)
    print "the error rate of this test is: %f" % errorRate
    return errorRate

def multiTest():
    numTests = 10; errorSum=0.0
    for k in range(numTests):
        errorSum += colicTest()
    print "after %d iterations the average error rate is: %f" % (numTests, errorSum/float(numTests))
        

