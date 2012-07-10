import itertools as it
from pprint import pprint

def maxprimes(max):
	'''thanks riko!'''
	max = int(max)
	limit = int(max**0.5 + 1.5)
	s = set(p for p in range(3, max, 2)).difference(
	        j for i in range(3, limit, 2) for j in range(i*i, max, i))
	s.add(2)
	return s

onetonine = [str(i) for i in range(1,10)]
def pandigit(n, m):
	return sorted(str(n))==onetonine[:m]
assert(pandigit(987654321, 9))
assert(pandigit(2143, 4))

allprimes = maxprimes(1e7)
d = dict.fromkeys(allprimes, True)
print("got all primes")

# this solution is ok, but more slow
#r = filter(lambda x: pandigit(x, len(str(x))),
#	   range(10, int(1e7)))
#print(max(r))

r = [it.permutations(onetonine[:i],i) for i in range(1,9)]
r = r = filter(d.get, 
		map(lambda x:int("".join(x)), 
			it.chain(*r)))

print(max(r))

