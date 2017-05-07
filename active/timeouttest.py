from timeout import timeout
from multiprocessing import Process
import time
import os 
@timeout(5)
def double(val):
	proc = os.getpid()
	print('{0} doubled to {1} by process id: {2}'.format(val, val*val, proc))
	try:
		time.sleep(6)
		print "ok"
	except Exception,e:
		print "this way" 

def main():
	procs = []
	number = [1,2,3,4,5]
	for val in number:
		proc = Process(target=double, args=(val,))
		procs.append(proc)
		proc.start()
	for proc in procs:
		proc.join()


main()