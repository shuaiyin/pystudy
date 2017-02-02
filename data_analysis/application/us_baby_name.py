#coding=utf-8
import pandas as pd 
from pandas import DataFrame,Series	
import numpy as np 
import sys

#read csv file into dataFrame structure
names1880 = pd.read_csv('../test_data/names/yob1880.txt',names=['name','sex','births'])
print names1880
"""
           name sex  births
0          Mary   F    7065
1          Anna   F    2604
2          Emma   F    2003
3     Elizabeth   F    1939
...
1994       Wood   M       5
1995     Woodie   M       5
1996     Worthy   M       5
1997     Wright   M       5
1998       York   M       5
1999  Zachariah   M       5

[2000 rows x 3 columns]


"""
print names1880.groupby('sex').births.sum()
"""
sex
F     90993
M    110493
Name: births, dtype: int64
"""

#year 2010  is the last valid  static year 
years = range(1880,2011)
pieces = []
columns = ['name','sex','births']
for year in years:
	path = '../test_data/names/yob%d.txt' % year
	frame = pd.read_csv(path,names=columns)
	frame['year'] = year
	pieces.append(frame)


#integrate the data set into simple DataFrame 
names =pd.concat(pieces,ignore_index=True)#using ignore_index to ignore the origial line numer return from read_csv method 
print names
"""
Name: births, dtype: int64
              name sex  births  year
0             Mary   F    7065  1880
1             Anna   F    2604  1880

...
27           Edith   F     768  1880
28          Mattie   F     704  1880
29            Rose   F     700  1880
...            ...  ..     ...   ...
1690754    Zaviyon   M       5  2010
1690755   Zaybrien   M       5  2010
1690756   Zayshawn   M       5  2010
1690757     Zayyan   M       5  2010
1690758       Zeal   M       5  2010
1690759     Zealan   M       5  2010
1690760   Zecharia   M       5  2010
1690761   Zeferino   M       5  2010
1690762   Zekariah   M       5  2010

"""


##now we can using "group by" or "pivot_table" to do some aggregate operation 
total_births = names.pivot_table('births',index='year',columns='sex',aggfunc=np.sum)
print total_births.tail()#get the last 5 rows 
"""
sex         F        M
year                  
2006  1896468  2050234
2007  1916888  2069242
2008  1883645  2032310
2009  1827643  1973359
2010  1759010  1898382

"""

##the next we insert a "prop" column to save the percent of specify baby name 

def add_prop(group):
	#
	births = group.births.astype(float)#transfer to float type  ,it will recreate a new Series, and will not change the original data 

	group['prop'] = births/births.sum()
	print '------'
	return group

# print add_prop(names)
# names = names.groupby(['year','sex']).apply(add_prop)
names = names.groupby(['year','sex']).apply(add_prop)
print names
"""
              name sex  births  year      prop
0             Mary   F    7065  1880  0.077643
1             Anna   F    2604  1880  0.028618
2             Emma   F    2003  1880  0.022013
.....
1690780     Zyonne   M       5  2010  0.000003
1690781  Zyquarius   M       5  2010  0.000003
1690782      Zyran   M       5  2010  0.000003
1690783      Zzyzx   M       5  2010  0.000003


"""