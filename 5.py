from math import sqrt
from pprint import pprint
from itertools import starmap
from functools import reduce

def prime(x):
	'''return true if x is a prime number.'''
	return [i for i in range(2,int(sqrt(x))+1) if x%i==0] == []
primes = [i for i in range(2,100) if prime(i)]

def factors(x):
	'''return prime factors of x. factors(12)==[2,2,3].'''
	i=0
	factors = []
	while x>1:
		p = primes[i]
		if x%p==0:
			x /= p
			factors.append(p)
		else:
			i += 1
	return factors

def yielding_factors(x, start=2):
	'''yields factors of all numbers from 2 to x.'''
	for i in range(start,x):
		yield factors(i)

def frequency_dict(l):
	'''return a dictionary with as keys all element in l and as values the count of the element.'''
	return { j: i.count(j) for j in i}

def predicate_on_dicts(d1, d2, predicate):
	'''d1, d2: dictionary. predicate: lambda x,y:... . 
	return a dictionary with as values the value of d1 or d2 that evaluates the predicate for all keys of d1.
	d1 = {'a':2, 'b':3}
	d2 = {'a':4}
	predicate_on_dicts(d1, d2, lambda x,y:x>y) --> {'a':4, 'b':3}
	'''
	return {j: d1[j] if predicate(d1.get(j,0),d2.get(j,0)) else d2[j]
			for j in d1.keys()}

# the algorithms is:
# calculate al factors in all numbers from 2 to max
# get all max primes frequencies and multiply each others
#
# example:
# max = 4 
# yielding_factors --> [[2], [3], [2, 2], [5]]
# p2f --> {2: 2, 3: 1, 5: 1} 
#         because 3,5 appear only in [3], [5]
#         2 appears in [2] and [2,2] and max frequencies is in [2,2].count(2)=2
# exps --> [3, 5, 2**2]
# result --> 3 * 5 * 4

max = 5
p2f = dict() # primes2frequencies
for i in yielding_factors(max+1):
	temp = frequency_dict(i)	
	p2f.update( predicate_on_dicts(temp, p2f, lambda x,y: x>y) )

exps = starmap(lambda x,y: x**y, p2f.items())
result = reduce(lambda x,y: x*y, exps)

print(result)
