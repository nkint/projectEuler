import itertools as it
import math as m

def maxprimes(max):
	'''thanks riko! get all primes under max.
	'''
	max = int(max)
	limit = int(max**0.5 + 1.5)
	s = set(range(3, max, 2)).difference(
		j for i in range(3, limit, 2) for j in range(i*i, max, i))
	s.add(2)
	return sorted(list(s))

MAX = 60000000
primeset = set(maxprimes(MAX))
print('got {0} primes'.format(len(primeset)))

def is_prime(n):
	if n<MAX: 
		return n in primeset
	else:
		#print(n)
		return [l for l in range(2,int(m.sqrt(n))+1) if n%l==0] == []

conditions_dict = dict()
#p = sorted(list(primeset))
#_m = 1000
#for i in range(_m):
#	for j in range(_m):
#		n = int(str(p[i])+str(p[j]))
#		if is_prime(n): 
#			conditions_dict[ p[i],p[j] ] = n
#		n = int(str(j)+str(i))
#		if is_prime(n): 
#			conditions_dict[ p[i],p[j] ] = n
#print('got dict',conditions_dict)

cache = dict()
def conditions(l):
	cached_solution = cache.get(tuple(l), 0)
	if cached_solution == -1: 
		#print('cached'); 
		return False
	elif cached_solution != 0: 
		#print('cached'); 
		return cached_solution

	for i,j in it.permutations(l,2):
		n = int(str(i)+str(j))
		if not is_prime(n): 
			cache[tuple(l)] = -1
			return False 
	if len(l)==5: print(l)
	cache[tuple(l)] = sum(l)
	return sum(l)



primes = maxprimes(9000)
def c(*a):
	return conditions([primes[x] for x in a])

l = [3, 7, 109, 673]
print(conditions(l))

l1 = [primes.index(i) for i in l]

def foo():
	max = len(primes)

	
	for i in range(max):
		for j in range(i,max):
			#if not conditions([primes[i],primes[j]]): continue
			if not c(i,j): continue

			for l in range(j,max):
				#if not conditions([primes[i],primes[j],primes[l]]): continue
				if not c(i,l) and not c(l,j): continue

				for k in range(l,max):
					#if not conditions([primes[i], primes[j], primes[l], primes[k]]): continue
					if not c(i,k) and not c(j,k) and not c(l,k): continue

					for h in range(k,max):

						### debug
						#if primes[i]==3 and primes[j]==7 and primes[l]==109 and primes[k]==673:
						#	print("DUDEE")
						#if primes[i]>7: print('out', primes[i])
						###

						p = [primes[i], primes[j], primes[l], primes[k], primes[h]]
						if conditions(p):
							print(conditions(p))
							return
					

from time import time
t = time()
foo()
print(time() - t)
