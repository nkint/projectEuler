import itertools as it
from pprint import pprint

top = 10000

def maxprimes(max):
	max = int(max)
	limit = int(max**0.5+1.0)
	s = set(range(3, max, 2)).difference(
		j for i in range(3, limit, 2) for j in range(i*i, max, i))
	s.add(2)
	return s

primes = maxprimes(top)
primeslist = list(primes)
print("got primes")

def f(n):
	r = []
	for p in primeslist:
		i=0
		while n%p==0:
			n/=p
			i+=1
		if i!=0: r.append(p**i)
	return set(r)

print(f(644))

from time import time
t = time()

#numbers and factor: nf, dict or list
nfd = {i:set(f(i)) for i in range(100000, 200000) if i not in primes}
nfl = list(nfd.keys())
print("got factors in :", time()-t)

k = 4
for i,v in enumerate(nfl):
	t = nfl[i:i+k]
	
	if len(t)<k: continue

	list_of_factors = [ nfd.get(t[j]) for j in range(k) ]
	num_of_factors = list(map(len, list_of_factors))
	slenbool = list(map(lambda x:x==k, num_of_factors))
	
	if all(slenbool):
		print("----------")
		pprint(list(zip(t, list_of_factors)))


