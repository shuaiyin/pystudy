#coding=utf-8
import sys
sys.path.append("..")
from  kNN import * ##引入外部函数模块的一种方法，光import kNN 是不能把其中的函数引进来的
from matplotlib.font_manager import FontProperties

datingDataMat,datingLabels = file2matrix('./datingTestSet.txt')
print type(datingDataMat)#<type 'numpy.ndarray'>

import matplotlib
import matplotlib.pyplot as plt 
fig = plt.figure()
ax = fig.add_subplot(111)
#设置label  
# ax.set_xlabel('玩视频游戏所耗时间百分比') #  
# ax.set_ylabel('每周消费的冰激凌公升数')


"""
#this is the figure1 

ax.scatter(datingDataMat[:,1],datingDataMat[:,2])

#该次散点图使用datingDateMat 矩阵的第二，第三列数据，分别表示特征值"玩视频游戏所耗时间百分比" and "每周消费的冰激凌公升数"
但是这种没有样本类别标签的约会数据散点图，难以辨别图中的点究竟属于哪个样本分类

"""

"""
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],
	15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()
#上述代码利用变量datingLabels存储的类标签属性，在散点图上绘制了色彩不等，尺寸不同的点
"""


normMat,ranges,minVals = autoNorm(datingDataMat)
print normMat
"""
[[ 0.44832535  0.39805139  0.56233353]
 [ 0.15873259  0.34195467  0.98724416]
 [ 0.28542943  0.06892523  0.47449629]
 ..., 
 [ 0.29115949  0.50910294  0.51079493]
 [ 0.52711097  0.43665451  0.4290048 ]
 [ 0.47940793  0.3768091   0.78571804]]

"""

