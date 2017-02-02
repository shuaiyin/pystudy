#coding=utf-8
from pandas import DataFrame,Series
import pandas as pd 
import sys
"""
    total_bill   tip    		 sex smoker   day    time  size
    用户消费总额  用户所给的小费
"""
PATH = '../test_data/tips.csv'
tips = pd.read_csv(PATH)

# sys.exit(0)

#添加“小费总额百分比”的列
tips['tip_pct'] = tips['tip']/tips['total_bill']
print tips[:5]
"""
   total_bill   tip     sex smoker  day    time  size   tip_pct
0       16.99  1.01  Female     No  Sun  Dinner     2  0.059447
1       10.34  1.66    Male     No  Sun  Dinner     3  0.160542
2       21.01  3.50    Male     No  Sun  Dinner     3  0.166587
3       23.68  3.31    Male     No  Sun  Dinner     2  0.139780
4       24.59  3.61  Female     No  Sun  Dinner     4  0.146808

"""


grouped = tips.groupby(['sex','smoker'])
print grouped['tip_pct'].agg('mean')
"""
我们希望对不同的列使用不同的聚合函数，或一次应用多个函数。这里根据sex和smoker对tips进行分组
sex     smoker
Female  No        0.156921
        Yes       0.182150
Male    No        0.160669
        Yes       0.152771

"""



##custom aggregate function 
def peak_to_peak(arr):
	return arr.max() - arr.min()

print grouped['tip_pct'].agg(['mean','std',peak_to_peak])
"""
                   mean       std  peak_to_peak
sex    smoker                                  
Female No      0.156921  0.036421      0.195876
       Yes     0.182150  0.071595      0.360233
Male   No      0.160669  0.041849      0.220186
       Yes     0.152771  0.090588      0.674707


"""

286  page 