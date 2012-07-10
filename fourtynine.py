import itertools as it
import pprint

def maxprimes(max):
	'''thanks riko!'''
	max = int(max)
	limit = int(max**0.5 + 1.5)
	s = set(range(3, max, 2)).difference(
	        j for i in range(3, limit, 2) for j in range(i*i, max, i))
	s.add(2)
	return s

top = 100000
primes = maxprimes(top)
fourdigitprimes = set(p for p in primes if len(str(p))==4)
alreadypassed = dict()

def prime_sequence(n):
	'''return a list - if exists - of primes that are permutations of n'''
	perm = map(lambda x: int("".join(x)), it.permutations(str(n)))
	primes_in_perm = [i for i in perm if i in fourdigitprimes]
	return primes_in_perm

def fixedpass_sequence(n,k=3330):
	'''return the arithmetic sequence - if exists - with fixed pass k'''
	d = dict()
	for i,x in enumerate(n):
		for j,y in enumerate(n[i+1:]):
			delta = abs(x-y)
			try:
				d[delta].update([x,y])
			except:
				d[delta] = set([x,y])
	return d.get(k)

def sequence(n):
	'''check for no duplicates and perform prime_sequence, fixedpass_sequence function call'''
	string = "".join(sorted(str(n)))
	try: if alreadypassed[string]: return []
	except: alreadypassed[string] = True
	return fixedpass_sequence(prime_sequence(n))

t = list(filter(lambda x:x and len(x)>=3, 
	        [(sequence(i)) for i in fourdigitprimes]))
pprint.pprint(t)
