#coding=utf-8
from numpy import * 
import sys
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
		(3)distMeas: 
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
					minDist = distaJ; minIndex = j
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
		centroids[cent,:] = mean(ptsInClust,axis=0)#calculate the avarage of the specify dim !!
	return centroids,clusterAssment

def biKmeans(dataMat,k,distMeas=distEclud):
	m = shape(dataMat)[0]
	clusterAssment = mat(zeros((m,2)))
	print clusterAssment

###########################################################################################################################


#用于生成k个质心的测试
dataMat = mat(loadDataSet(FILE_PATH))

biKmeans(dataMat,4)
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
