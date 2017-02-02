#coding=utf-8
from numpy import * 
import sys

"""
1.一种用于度量聚类效果的指标是SSE(sum of squared error ),误差平方和，在本文件中的kMeans函数中的clusterAssment矩阵的第一列之和。SSE的值越小表示数据点越接近于它们的质心,
2.聚类效果也越好，因为对误差取了平方，一次更加重视那些远离中心的点。 一种肯定可以降低SSE的方法是增加簇的个数，但这违背了聚类的目标。
3.聚类的目标是在保持簇"数目不变"的情况下"提高簇的"质量"！！！！
4.
"""

FILE_PATH = './test_data/testSet2.txt'

def loadDataSet(fileName):
	dataMat = []
	fr = open(fileName)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fitLine = map(float,curLine)#批量的把list当中的数据转换为float类型，返回list
		dataMat.append(fitLine)
	return dataMat


def distEclud(vecA,vecB):
	"""
	用于计算两个向量的欧氏距离，当然也可以使用其他计算距离的方式
	"""
	return sqrt(sum(power(vecA-vecB,2)))

def randCent(dataSet,k):
	"""
	funciton: 构建簇质心
	该函数为给定数据集构造一个包含k个随机质心的集合。随机质心必须要在整个数据集的边界之内，
	这可以通过找到数据集每一维的最小和最大值来完成，然后生成0到1.0之间的随机数并通过取值范围和最小值，以便确保随机点在数据的边界之内
	input argument:
			dataSet : type is matrix
			k: the num of xxx
	"""
	n = shape(dataSet)[1]#获取特征值的列数
	centroids = mat(zeros((k,n)))#
	for j in range(n):
		minJ = min(dataSet[:,j])#the type of minJ is matrix
		rangeJ = float(max(dataSet[:,j]) - minJ)#reforce transfer  the matrix type  into float type !! 
		#set a ndarray value to matrix ?? ok 
		centroids[:,j] = minJ + rangeJ * random.rand(k,1) #a ndarray data plus a matrx type data will return a matrix data !!!!!
	return centroids

# b1 = array([[1,0,1],[True,False,False]])
# arr = array([1,2,3,1,2])
# arr = array([[1,2,2],[3,4,2]])
# print arr == 2
# # print nonzero(b1)
# sys.exit(0)
def kMeans(dataSet,k,distMeas=distEclud,createCent=randCent):
	"""
	K均值聚类算法
	input argument:
		(1)dataSet
		(2)k 设定的聚簇的数目
		(3)distMeas: 计算距离所采用的函数，默认利用欧拉计算距离
		(4)createCent:初始化质心的方式，这里默认为随机初始化

	K-均值聚类中簇的数目k是一个用户预先定义的参数，那么用户如何知道k的选择是否正确？如何才能知道生成的簇比较好呢？ 
	K-均值聚类算法收敛但聚类效果差的原因是，K-均值算法收敛到了局部最小值，而非全局最小值（局部最小值指结果还可以但并非最好结果，全局最小值是可能的最好结果）
	"""
	m  = shape(dataSet)[0]#函数一开始确定数据集中的数据点的总数，然后创建一个矩阵来存储每个点的簇分配结果
	#簇分配结果矩阵clusterAssment包含两列：一列记录簇索引值，第二列存储误差。这里的误差是指当前点到簇质心的距离，后边会使用该误差来评价聚类的效果
	clusterAssment = mat(zeros((m,2)))
	centroids = createCent(dataSet,k)#这里初始化ｋ个质心！！！
	clusterChanged = True 
	while clusterChanged:
		clusterChanged = False
		for i in range(m):#遍历所有数据找到距离每个点最近的质心,这可以通过对"每个"点遍历"所有"质心 and 计算点到每个质心的距离来完成
			minDist = inf; minIndex = -1#numpy中的inf表示一个无限大的正数
			for j in range(k):#遍历ｋ个质心,通过对"每个"点遍历"所有"质心 and 计算点到每个质心的距离
				distaJ = distMeas(centroids[j,:],dataSet[i,:])#计算质心和测试行数据之间的欧拉距离！！（这里使用的距离算法就是欧拉）
				if distaJ < minDist:
					minDist = distaJ; minIndex = j#其实这里的minIndex就是使的当前测试数据行和质心距离更小的簇的索引
			if clusterAssment[i,0] != minIndex: clusterChanged = True#as long as it do not reach the finally result(has True dataline) ,it will execute with no stop 
			clusterAssment[i,:] = minIndex,minDist ** 2#分配结果的矩阵中保存着该点到簇质心的距离平方值,以为对误差取了平方，因此更加重视那些远离簇质心的点
		for cent in range(k):#更新质心的位置！首先通过数组过滤来获得给定簇的所有点，然后计算所有的点的均值，选项axis=0表示沿矩阵的列方向进行均值计算；
			"""
			1.matrix.A can transfer a matrix into an array !!!!
			2.'array == some num' is a vector calculate!! it will set the value in "array" with True  or False rely on the comparation result 
			3.the nonzero method will return a tuple,such as (array([ 6, 10, 15, 18, 30, 38, 42, 43, 46, 50, 54, 58, 62, 66, 70]), array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
			it means the position in (6,0) (10,0) ...  is False
			4.nonzero(clusterAssment[:,0].A == cent)[0] will return the dataLine of the specify group(using cent to show)
			5.there is a matrix A,and B is an array ,we can use A[B] to select multi data line of the matrix A 
			"""
			ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]
			print 'the point in cent ',cent,' is ',ptsInClust
			centroids[cent,:] = mean(ptsInClust,axis=0)#calculate the avarage of the specify dim !!
	return centroids,clusterAssment


# dataMat = mat(loadDataSet(FILE_PATH))
# kMeans(dataMat,2)
# sys.exit(0)





def biKmeans(dataSet,k,distMeas=distEclud):
	"""
	function ::::  二分K-均值聚类算法
	input argument:
		(1)dataSet:
		(2)k ::设定的聚簇的数目
		(3)distMeas: 计算距离所采用的函数，默认利用欧拉计算距离
	在给定数据集、所期望的簇数目和距离计算方法的前提下，函数返回聚类结果


	在之前的K-均值聚类中簇的数目k是一个用户预先定义的参数，那么用户如何知道k的选择是否正确？如何才能知道生成的簇比较好呢？ 
	K-均值聚类算法收敛但聚类效果差的原因是，K-均值算法收敛到了局部最小值，而非全局最小值（局部最小值指结果还可以但并非最好结果，全局最小值是可能的最好结果）

	为克服K-均值算法收敛于局部最小值的问题，有人提出了另一个称为二分k-均值(bisecting K-means)的算法，该算法首先将所有点作为一个簇，然后将该簇一分为2,之后
	选择其中一个簇继续进行划分，选择哪一个簇进行划分取决于对其划分是否可以最大程度降低SSE的值，上述基于SSE的划分过程不断重复，直到得到用户指定的簇数为止

	伪代码如下所示：
		将所有点看成一个簇： 
		当簇数目小于k时
			对于每一个簇： 
				计算总误差  
				在给定的簇上面进行K-均值聚类(k=2)  
				计算将该簇一分为二之后的总误差  
			选择使得误差最小的那个簇进行划分操作

	"""
	m = shape(dataSet)[0]
	clusterAssment = mat(zeros((m,2)))#init cluster and distance !!!
	print dataSet
	sys.exit(0)
	centroid0 = mean(dataSet,axis=0).tolist()[0]#求得第一个质心！第一个质心就是特征值列的均值构成的
	centList = [centroid0]#将第一个质心放到质心列表集合中！！！
	#在这个for 循环之后，clusterAssment 当中就存储了各个点距离质心之间的平方距离了
	for j in range(m):
		clusterAssment[j,1] = distMeas(mat(centroid0),dataSet[j,:]) ** 2

	while(len(centList) < k):#如果没有获取到k个质心的话,遍历列表centList中的每一个簇
		lowestSSE = inf 
		for i in range(len(centList)):#对于每一个簇,遍历列表centList中的每一个簇
			#对于每个簇，将"该簇"中的"所有点"看成一个小的数据集ptsInCurrCluster
			ptsInCurrCluster = dataSet[nonzero(clusterAssment[:,0].A == i)[0],:]#其实最开始的时刻所有的点都是属于第0个质心的  ---pointincurrentcluster
			"""
			将ptsInCurrCluster输入到函数kMeans()中进行处理（k=2),k均值算法会生成两个质心（簇），同时给出每个簇的误差值，这些误差与剩余数据集的误差之和作为本次划分的误差
			在调取这个kMeans方法的时候，使用默认的距离计算方式（欧拉），使用的生成质心的方式为随机生成法
			对收集的簇进行后处理，一种方法是将具有更大SSE（误差平方值）的簇划分成两个簇。具体实现时可以将最大簇包含的点过滤出来并在这些点上运行k-均值算法，其中的k设置为2
			"""
			centroidMat,splitClustAss = kMeans(ptsInCurrCluster,2,distMeas)
			sseSplit = sum(splitClustAss[:,1])#计算切分后所有点的误差和
			sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:,0].A != i)[0],1])
			print "sseSplit,and notSplit: ",sseSplit,sseNotSplit
			if(sseSplit + sseNotSplit) < lowestSSE:
				bestCentToSplit = i
				bestNewCents = centroidMat
				bestClustAss = splitClustAss.copy()
				lowestSSE = sseSplit + sseNotSplit
		bestClustAss[nonzero(bestClustAss[:,0].A == 1)[0],0] = len(centList)
		bestClustAss[nonzero(bestClustAss[:,0].A == 0)[0],0] = bestCentToSplit
		print 'the bestCentToSplit is : ',bestCentToSplit
		print 'the len of bestClustAss is :', len(bestClustAss)
		centList.append(bestNewCents[1,:])
		clusterAssment[nonzero(clusterAssment[:,0].A == bestCentToSplit)[0],:] = bestClustAss
	return mat(centList),clusterAssment


#用于生成k个质心的测试
dataMat = mat(loadDataSet(FILE_PATH))

print biKmeans(dataMat,4)
sys.exit(0)


center = randCent(mat(dataMat),5)##need matrix param 
print center
print type(center)
"""
[[-1.57766498  3.85912883]
 [-4.87507773  0.12090467]
 [-3.32746413  1.79961195]
 [-3.95044513  3.49477696]
 [-2.55200907  1.73982385]]
<class 'numpy.matrixlib.defmatrix.matrix'>
"""

print '-------------'
centroids,clusterAssment =  kMeans(dataMat,4)
print centroids,clusterAssment#获得到4个质心  还有每个点属于的簇和距离质心之间的距离
"""
[[ 0.29674154 -2.76397043]
 [-2.764387    1.60824825]
 [-3.84165867  3.351989  ]
 [ 2.3772111   3.2195035 ]]

 [[  3.           1.23267771]
 [  2.           0.73984329]
 [  0.          15.56079013]
   ....
 [  3.           1.14619913]
 [  1.           1.38787727]
 [  1.           0.36728761]
 [  0.          12.5073786 ]
 [  1.          32.21144906]]

"""
sys.exit(0)
