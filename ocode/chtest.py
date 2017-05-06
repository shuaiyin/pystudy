#coding:utf-8

import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
font = FontProperties(fname = "/usr/share/fonts/truetype/arphic/ukai.ttc", size=14)
plt.title(u"用户数量(Y)关于游戏消费金额(X)的分布图",fontproperties=font,fontsize=50)
plt.xlabel(u"用户数量(Y)关于游戏消费金额(X)的分布图",fontproperties=font,fontsize=50)
plt.show()