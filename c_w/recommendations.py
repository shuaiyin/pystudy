#coding=utf-8
# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

"""
上面这些数据可以从http://www.grouplens.org/node/73  获取到涉及电影评价的真实数据，叫做MovieLens,有不同数据量集可以下载，解压之后归档文件中包含了不少文件
"""


from math import sqrt
import sys

# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
  # Get the list of shared_items
  """
  返回一个有关person1与person2的基于距离的相似度评价   计算用户之间的相似度
  这是欧几米德距离评价方法---ys:其实感觉与K-近邻有些相似了
  这是一种距离度量法
  """
  si={}
  for item in prefs[person1]: 
    if item in prefs[person2]: si[item]=1
  # if they have no ratings in common, return 0 二者没有相同之处
  if len(si)==0: return 0#这里进行一次迭代只是为了发现是不是二者没有任何相似的影集
  # Add up the squares of all the differences
  sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) 
                      for item in prefs[person1] if item in prefs[person2]])
  #这里之所以分子，分母都添加了一个1 ，这是一种避免sum之后的结果为0的好方式哦
  return 1/(1+sum_of_squares)

# result = sim_distance(critics,'Lisa Rose','Mick LaSalle')
# print result


# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
  # Get the list of mutually rated items
  """
  皮尔逊相关度评价   计算用户之间的相似度
  皮尔逊相关系数，该相关系数是判断两组数据与某一直线拟合程度的一种度量，对应的公式比欧几米德评价的计算公式复杂，但是他在数据不是很规范（normalized)的时
  候(比如，影评者对影片的评价总是相对于平均水平偏离很大时)，会倾向于给出更好的结果
  该函数将返回一个介于-1与1之间的数值，值为1则表示2个人对每一样武平均有着完全一致的评价
  """
  si={}#
  #得到双方都曾评价过的物品列表
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1
  # if they are no ratings in common, return 0
  if len(si)==0: return 0
  # Sum calculations
  n=len(si)
  
  # Sums of all the preferences 对所有偏好求和
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  # print sum1,sum2

  # Sums of the squares 对所有偏好求平方和
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])#用户1的影评评分平方和 ,equall to X的平方的期望
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])#用户2的影评评分平方和 ,equall to Y的平方的期望
  
  # Sum of the products 对所有偏好求乘积之和
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])###这里的求和，求的是XY（两个变量相乘）的总和，当然这里为了计算E(XY)而做的铺垫 E(XY) = SUM(XY)/N
  
  # Calculate r (Pearson score) 计算皮尔逊评价值
  #这里的(sum1*sum2)/pow(n,2)得到的是积的期望，类似于E(XY),而这里的pSum又是X*Y的积的和，那么sum(X*Y)/N得到的就是E(XY)
  #下面得到的应该是n(E(XY)-E(X)*E(Y))
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))##仔细考虑这里的除以n的原因,,,i think this has some problem in it 
  """
  两个变量之间相关系数的求法
  (1)cov(X,Y) = [E(XY) - E(X)E(Y)]/ 具体公式自己查

  """
  if den==0: return 0

  r=num/den

  return r


# result = sim_pearson(critics,'Lisa Rose','Mick LaSalle')
# print result
# sys.exit(0)


# Returns the best matches for person from the prefs dictionary. 
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_pearson):
  """
  从反映偏好的字典中返回最为匹配者  找出与自己有相似品味的影评者
  返回结果的个数和相似度函数均为可选参数
  """
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]#不和自己做比较
  scores.sort()
  scores.reverse()
  return scores[0:n]


# print topMatches(critics,'Toby',n=3)
# sys.exit(0)



# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
  """
  1.利用所有他人评价的加权平均，为某人提供建议(这里进行推荐的时候不仅仅只是依赖相关度)
  2.计算相似度的方法是可选项，既可以选择皮尔逊相关度评价，也可以选择欧几米德相关度评价方法等
  3.找到一位趣味相投的影评者并阅读他所撰写的评论固然不错，但是现在我们真正想要的不是这些，而是一份影片的推荐，
  当然，我们可以查找与自己品味最为相近的人，并从他喜欢的影片中找出一部自己还未看过的影片，但是这样太随意了
  4.有时，这种方法可能会有问题：评论者还未对某些影片做过评价，而这些影片也许就是我们所喜欢的；还有一种可能，
  我们会找到一个热衷某部影片的古怪评论者，而根据topMatches所返回的结果，所有的其他评论者都不看好这部影片
  """

  totals={}#用于存储相似度和用户评价的加权和 这里的key是影视作品的名称，值为加权值（相似度*其他某个用户对影视的评价)
  simSums={}#用于存储其他用户对于某个影视作品只要进行了评论，那么就把其相似度累加过来. 这里的key是影视作品的名称,值为评论过作品的其他人和本人之间的相似度的总和
  for other in prefs:#对字典进行遍历的时候其实遍历的是字典的key，那么这里就是评影人
    # don't compare me to myself
    if other==person: continue#
    sim=similarity(prefs,person,other)#计算输入用户和其他用户之间的相关度
    # ignore scores of zero or lower
    if sim<=0: continue
    for item in prefs[other]:#这里的item获取到的是他人所评价过的电影
      # only score movies I "haven't" seen yet 
      if item not in prefs[person] or prefs[person][item]==0:#如果用户没有对这个影片做过评价，或者评价为0
        #其实下面得到的就是other看过的电影，但是本人没有看过的电影
        # Similarity * Score
        totals.setdefault(item,0)#这里的setdefault用的非常好，dict.setdefault(key,[default])如果键在字典中,返回这个键所对应的值。如果键不在字典中,向字典中插入这个键,并且以default为这个键的值
        totals[item]+=prefs[other][item]*sim
        # Sum of similarities
        simSums.setdefault(item,0)#
        simSums[item]+=sim#
  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items()]#dict.items will create a tuple list make of (key,value)
  # Return the sorted list
  rankings.sort()
  rankings.reverse()
  return rankings

# print s(critics,'Toby')
"""
其实就是给那些用户所没有看过的电影给个推荐。
[(3.3477895267131013, 'The Night Listener'), (2.8325499182641614, 'Lady in the Water'), (2.5309807037655645, 'Just My Luck')]

"""
# result = sim_pearson(critics,'Lisa Rose','Mick LaSalle')
# sys.exit(0)

def transformPrefs(prefs):
  result={}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item,{})
      
      # Flip item and person
      result[item][person]=prefs[person][item]
  return result


def calculateSimilarItems(prefs,n=10):
  # Create a dictionary of items showing which other items they
  # are most similar to.
  result={}
  # Invert the preference matrix to be item-centric
  itemPrefs=transformPrefs(prefs)
  c=0
  for item in itemPrefs:
    # Status updates for large datasets
    c+=1
    if c%100==0: print "%d / %d" % (c,len(itemPrefs))
    # Find the most similar items to this one
    scores=topMatches(itemPrefs,item,n=n,similarity=sim_distance)
    result[item]=scores
  return result

def getRecommendedItems(prefs,itemMatch,user):
  userRatings=prefs[user]
  scores={}
  totalSim={}
  # Loop over items rated by this user
  for (item,rating) in userRatings.items( ):

    # Loop over items similar to this one
    for (similarity,item2) in itemMatch[item]:

      # Ignore if this user has already rated this item
      if item2 in userRatings: continue
      # Weighted sum of rating times similarity
      scores.setdefault(item2,0)
      scores[item2]+=similarity*rating
      # Sum of all the similarities
      totalSim.setdefault(item2,0)
      totalSim[item2]+=similarity

  # Divide each total score by total weighting to get an average
  rankings=[(score/totalSim[item],item) for item,score in scores.items( )]

  # Return the rankings from highest to lowest
  rankings.sort( )
  rankings.reverse( )
  return rankings

def loadMovieLens(path='./testdata/ml-100k'):
  """
  上面这些数据可以从http://www.grouplens.org/node/73  获取到涉及电影评价的真实数据，叫做MovieLens,有不同数据量集可以下载，解压之后归档文件中包含了不少文件
  我们关系的是u.item和u.data前者包含了一组有关影片ID和片名的列表，后者包含了如下形式的给出的实际评价情况。

  196 242 3 881250949
  186 302 3 891717742
  22  377 1 878887116
  244 51  2 880606923
  166 346 1 886397596
  298 474 4 884182806
  115 265 2 881171488
  此处的每一行数据都包含了一个用户ID,影片ID，用户对该片给出的评分，以及评价时间

  """
  # Get movie titles
  movies={}
  for line in open(path+'/u.item'):
    (id,title)=line.split('|')[0:2]
    movies[id]=title
  
  # Load data
  prefs={}
  for line in open(path+'/u.data'):
    (user,movieid,rating,ts)=line.split('\t')
    prefs.setdefault(user,{})
    prefs[user][movies[movieid]]=float(rating)
  return prefs

prefs = loadMovieLens()
# print prefs['87']#这个数据集并没有给出人的姓名，只是有索引id
"""
{'Birdcage, The (1996)': 4.0, 'E.T. the Extra-Terrestrial (1982)': 3.0, 'Bananas (1971)': 5.0, 'Sting, The (1973)': 5.0, 
'Bad Boys (1995)': 4.0, 'In the Line of Fire (1993)': 5.0, 'Star Trek: The Wrath of Khan (1982)': 5.0, 'Speechless (1994)': 4.0,
 'Mission: Impossible (1996)': 4.0, 'Return of the Pink Panther, The (1974)': 4.0, 'Under Siege (1992)': 4.0, 'I.Q. (1994)': 5.0, 
 'Evil Dead II (1987)': 2.0, 'Heat (1995)': 3.0, 'Naked Gun 33 1/3: The Final Insult (1994)': 4.0, etc.................}
"""
print getRecommendations(prefs,'87')[:5]
"""
[(5.0, 'They Made Me a Criminal (1939)'), (5.0, 'Star Kid (1997)'), (5.0, 'Santa with Muscles (1996)'), 
(5.0, 'Saint of Fort Washington, The (1993)'), (5.0, 'Marlene Dietrich: Shadow and Light (1996) ')]
"""