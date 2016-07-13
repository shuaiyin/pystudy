#coding=utf-8
import exceptions 
#something about exception 
#find out what exception the exception class give us  
print dir(exceptions)
"""
['ArithmeticError',
 'AssertionError',
 'AttributeError',
 'BaseException',
 'BufferError',
 'BytesWarning',
 'DeprecationWarning',
 'EOFError',
 'EnvironmentError',
 'Exception',
 'FloatingPointError',
 'FutureWarning',
 'GeneratorExit',
 'IOError',
 'ImportError',
 'ImportWarning',
 'IndentationError',
 'IndexError',
 'KeyError',
 'KeyboardInterrupt',
 'LookupError',
 'MemoryError',
 'NameError',
 'NotImplementedError',
 'OSError',
 'OverflowError',
 'PendingDeprecationWarning',
 'ReferenceError',
 'RuntimeError',
 'RuntimeWarning',
 'StandardError',
 'StopIteration',
 'SyntaxError',
 'SyntaxWarning',
 'SystemError',
 'SystemExit',
 'TabError',
 'TypeError',
 'UnboundLocalError',
 'UnicodeDecodeError',
 'UnicodeEncodeError',
 'UnicodeError',
 'UnicodeTranslateError',
 'UnicodeWarning',
 'UserWarning',
 'ValueError',
 'Warning',
 'ZeroDivisionError',
 '__doc__',
 '__name__',
 '__package__']
"""



data = {'name':'yinshuai'}
try:
	1/data['age']
except ZeroDivisionError:
	print 'can not be zero'
except Exception:
	print 'find exception '

"""
find exception 
"""


##not only one exception !!!
#有的时候不仅仅需要一个except,我们可能需要捕获很多exception 
print '---test 1 -------'
try:
	x = input('Enter the first number:')
	y = input('Enter the second number:')
	print x/y
except ZeroDivisionError:
	print 'divisor can not be zero'
except TypeError:
	print 'please input right type '


###不知道下面这么做会不会被骂
print '--------test 2----'
try:
	x = input('Enter the first numer')
	y = input('Enter the second number')
	print x/y
except Exception,e:
	print e 
"""
55  'sss'    show exception unsupported operand type(s) for /: 'int' and 'str'
55 0   integer division or modulo by zero
其实很容易发现的，使用继承于Except 类的东西是有好处的，在那些我们能知道会出现那些except 的场合可以做相应的友好处理
其实这样的catch是很危险的，因为他会隐藏所有coder未曾想到的并且未做好准备的错误
他同样会catch 用户the 指令 用户end execute (ctrl c ) and when using sys.exit
"""


#####用一个block 捕捉2个或者多个exception 
print '--------test 3 -------'
try:
	x = input('Enter the first number')
	y = input('Enter the second number')
	print x/y
except (ZeroDivisionError,TypeError,NameError):
	print 'shit,find exception'
"""
0 0    shit,find exception 
'ss' 0 shit,find exception
"""


######catch exception and print the except object  e 
print '--test 4 ------------'
try:
	x = input('Enter the first number')
	y = input('Enter the second number')
	print x/y
except (ZeroDivisionError,TypeError,NameError),e:
	print e 
"""
0 0 		integer division or modulo by zero
0 'ss'  	unsupported operand type(s) for /: 'int' and 'str'
"""



###万事大吉 
try:
	print 'A simple tast'
except:
	print 'something may go wrong '
else:
	print 'it went as planed '
"""
A simple tast
it went as planed 
"""




while True:
	try:
		x = input('Enter the first number')
		y = input('Enter the second number')
		print x/y
	except:
		print ' invalid input, please try again '
	else:
		break
"""
这里的循环只有在没有exception 才会结束,that to say,as long as there is wrong ,it will need you reinput 
we can use 
except Exception,e: to show the except content to the user 
"""



