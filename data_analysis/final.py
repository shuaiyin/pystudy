#coding=utf-8
from pandas import Series,DataFrame
csv_path = './ch06/ex1.csv'
content = pd.read_table(csv_path,sep=',')