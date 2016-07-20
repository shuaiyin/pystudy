#coding=utf-8
import matplotlib.pyplot as plt 
decisionNode = dict(boxstyle="sawtooth",fc="0.8")#这2行是定义文本框的
leafNode = dict(boxstyle="round4",fc="0.8")#这里的fc是控制显示的透明度的
arrow_args = dict(arrowstyle="<-") #控制箭头的，这里同样也控制了箭头的指向 <- and -> is different 

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
	#python中所有的变量默认都是全局有效的
	createPlot.axl.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',xytext=centerPt,textcoords='axes fraction',va="center",ha="center",
							bbox=nodeType,arrowprops=arrow_args)

def createPlot():
	"""
	绘制叶子节点
	"""
	fig = plt.figure(1,facecolor='white')
	fig.clf()
	createPlot.axl = plt.subplot(111,frameon=False)#plotNode()函数执行了实际的绘图功能，该函数需要一个绘图区，该区域由全局变量createPlot.axl 定义
	plotNode('a decision node',(0.5,0.1),(0.1,0.5),decisionNode)
	plotNode('a leaf node ',(0.8,0.1),(0.3,0.8),leafNode)
	plt.show()



def plotMidText(cntrPt,parentPt,txtString):
	"""
	在父子节点减填充文本信息,其实这里填充的是跳转条件，填充位置在起始点与终点两点之间
	"""
	xMid = (parentPt[0] - cntrPt[0])/2.0 + cntrPt[0]#x point
	yMid = (parentPt[1] - cntrPt[1])/2.0 + cntrPt[1]#y point 
	createPlot.axl.text(xMid,yMid,txtString)#createPlot.axl 是全局的一个画布哦


def plotTree(myTree,parentPt,nodeTxt):
	"""
	绘制树
	"""
	numLeafs = getNumLeafs(myTree)
	depth = getTreeDepth(myTree)#计算树的宽与高
	firstStr = myTree.keys()[0]#获取树根(the pic start from the root )
	cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW,plotTree.yOff )
	print '--' + str(cntrPt)##--(0.5, 1.0)   --(0.6666666666666666, 0.6666666666666667)

	plotMidText(cntrPt,parentPt,nodeTxt)#
	plotNode(firstStr,cntrPt,parentPt,decisionNode)
	secondDict = myTree[firstStr]
	plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD#按比例减少全局变量plotTree.yOff, 并且标注此处将要绘制子节点，这些节点既可以是判断节点也可以是叶子节点
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			plotTree(secondDict[key],cntrPt,str(key))
		else:
			plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
			plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
			plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
	plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

	pass

def createPlot(inTree):
	"""

	"""
	fig = plt.figure(1,facecolor='white')
	fig.clf() #init clear the figure
	axprops = dict(xticks= [],yticks = [])
	createPlot.axl = plt.subplot(111,frameon=False,**axprops)
	plotTree.totalW = float(getNumLeafs(inTree))#全局变量 plotTree.totalW  存储树的宽度 
	plotTree.totalD = float(getTreeDepth(inTree))#全局变量 plotTree.totalD 存储树的深度
	print myTree
	print getNumLeafs(myTree)
	print getTreeDepth(myTree)
	plotTree.xOff = -0.5/plotTree.totalW#使用两个全局变量plotTree.xOff 和 plotTree.yOff 来追踪已经绘制的节点位置，以及放置下一个节点的恰当位置
	plotTree.yOff = 1.0
	plotTree(inTree,(0.5,1.0),'')
	plt.show()



def retrieveTree(i):
	"""
	这里主要是为了测试方便，
	"""
	listOfTrees = [
					{'no surfacing':
						{0:'no',1:
							{'flippers':
								{0:'no',1:'yes'}
							}
						}
					},
					{
					 'no surfacing':
					 	{0:'no',1:
							{'flippers':
								{
									0:{'head':
										{0:'no',1:'yes'}
									  },
									1:'no'
								}
							}
						}
					}

	]
	return listOfTrees[i]

def getNumLeafs(myTree):
	"""
	获取树的叶子总数
	"""
	numLeafs = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':#判断子节点是否为字典类型，如果是字典类型，则该节点也是一个判断节点，需要继续递归调用
			numLeafs += getNumLeafs(secondDict[key])
		else: numLeafs += 1 
	return numLeafs

def getTreeDepth(myTree):
	"""
	 获取树的深度
	"""
	maxDepth = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	thisDepth = 0
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			thisDepth = 1 + getTreeDepth(secondDict[key])
		else: thisDepth += 1
		if thisDepth > maxDepth: maxDepth = thisDepth
	return maxDepth





if __name__ == '__main__':
	# createPlot()
	# print retrieveTree()
	myTree = retrieveTree(1)
	print myTree
	print getNumLeafs(myTree)
	print getTreeDepth(myTree)
	createPlot(myTree)
