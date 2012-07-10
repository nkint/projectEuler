import operator as op
from functools import reduce

s = str(12345)
combs = []

def _c(n, r):
	if r==0 or n==[]: return []
	if r==1: 
		return [str(i) for i in n]
	else:
		ret = []
		for i,v in enumerate(n): 
			c1 = _c(n[i+1:], r-1)
			i = str(v)
			ret.extend( [i+j for j in c1] )
		return ret

#print( _c([1,2,3,4,5],3) )
#print(len( _c([i for i in range(1,23+1)],10)))

def c(n, r):
	if r==0 or n==0: return 0 
	if r==1: 
		return n
	else:
		ret = 0
		for i in range(n): 
			c1 = c(n-i-1, r-1)
			ret += c1
		return ret

#print( c(5,3) )
#print( c(23, 10) )
#count = 0
#for n in range(1,101):
#	for r in range(n):
#		value = c(n, r)
#		if value>1000000:
#			print(n,r)
#			count+=1
#print("--",count)
print("--")

# dannazione! non ho capito l'inglese del testo!!
# basta usare la formula, avevo capito che in alcuni casi
# la formula non funziona: 'It is not until'

from functools import reduce
import time

cached_factorial = dict()

def factorial(n):
	if n<=1: return 1
	if cached_factorial.get(n)==None:
		cached_factorial[n] = reduce(lambda x,y:x*y, range(1, n+1))
	return cached_factorial.get(n)
def ncr(n,r):
	f = factorial
	return f(n)/(f(r)*f(n-r)) 

t = time.time()
count = [ncr(n,r) for n in range(1,101) for r in range(1,n-1)]
count = [i for i in count if i>1000000]
print(len(count))
print(time.time()-t)
