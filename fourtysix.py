from pprint import pprint
from time import time
import itertools as it

top = 10000

odd = lambda x:not x%2==0
odds = set([i for i in range(top) if odd(i)])

def maxprimes(max):
	max = int(max)
	limit = int(max**0.5+1.0)
	s = set(range(3, max, 2)).difference(
		j for i in range(3, limit, 2) for j in range(i*i, max, i))
	s.add(2)
	return s
primes = maxprimes(top)
print("got primes")

t = time()
goldbachodds = set([(p+2*j**2) for i,p in enumerate(primes) for j in range(1,100)])
print("functional > t:",time()-t)

l = odds.difference(goldbachodds,primes, [1])
print(min(l))
