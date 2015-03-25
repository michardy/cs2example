import numpy
import eateggs
x = numpy.pi
print(x*2)

def fib(end):
	last = 0
	cur = 1
	for i in range(end):
		cur+=last
		last = cur
		print(last)

eggs = raw_input('# eggs eaten: ')
eateggs.eatEggs(eggs)
