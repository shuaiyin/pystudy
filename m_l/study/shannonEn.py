#coding=utf-8
"""
对香农熵的测试
在信息论和概率统计中，熵是表示随机变量不确定性的度量，熵越大，表示数据越杂乱无章，反之，则说明数据越有序
"""

import numpy as np 
p = np.linspace(0.,1.,11)
print p
print type(p)
"""
[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1. ]
<type 'numpy.ndarray'>
yinshuai:linspace用于构建等差数列的
"""

Hp = -p*np.log2(p) - (1-p)*np.log2(1-p)
# Hp[0] = Hp[-1] = 0

