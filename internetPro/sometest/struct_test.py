#coding=utf-8
"""
1.我们知道python只定义了6种数据类型，字符串，整数，浮点数，列表，元组，字典。但是C语言中有些字节型的变量，在python中该如何实现呢？这点颇为重要，特别是要在网络上进行数据传输的话。
python提供了一个struct模块来提供转换。下面就介绍这个模块中的几个方法。
struct.pack():
struct.pack用于将Python的值根据格式符，转换为字符串（因为Python中没有字节(Byte)类型，可以把这里的字符串理解为字节流，或字节数组）。
"""
import struct 
a = 20 
b = 400
str_packed = struct.pack('ii',a,b) ##ii 表示两个int
print len(str_packed) #8
print str_packed  #�
print repr(str_packed) #'\x14\x00\x00\x00\x90\x01\x00\x00'
"""
二进制是乱码
其中十六进制的 0x00000014, 0x00001009分别表示20和400
"""


a,b = struct.unpack('ii',str_packed)#可以看到 “ii”以四个字节为分界，把8个字节的str分成了两个int型的整数。
print a,b #20 400 

#struct.calcsize()用来计算特定格式的输出的大小，是几个字节，比如：
print struct.calcsize('HH4s') #8  =  2 + 2 + 4 * 1 
print struct.calcsize('4Q')#32 =  4 * 8
print struct.calcsize('4f') #16 = 4 * 4
print struct.calcsize('QQff2c')#but cQQFF is not true !! 26 = 8 + 8 + 4 + 4 + 2 * 1 

print struct.calcsize('44c') # 44 = 44 *1 
print struct.calcsize('6B') # 6 = 6 * 1 
print struct.calcsize('ii') # 8 = 4 + 4 
"""

struct.calcsize():用来计算特定格式的输出的大小，是几个字节
关于各种format所占空间的大小如:  http://images.cnblogs.com/cnblogs_com/coser/201112/201112171613441943.png
这里例举几个:

Format        C Type       			Python type    			Standard size  
c 			 char          			string of length 1		1 
b      		signed char    			integer 				1
B   		unsigned char  			integer					1
Q 			unsigned long long 		integer					8
H 			unsigned short 			integer					2
f 			float 					float   				4
d			double 					float					8
s 			char[]					string 					n*1
i         	int 					integer 				4
L 			unsigned long 			integer					4
"""




