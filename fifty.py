########################################################## data structure and functions
'''
due to the fact that 953 is sums of  [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
the challange is reduced to find the start point (7) and the length of the sum (21)

we can find all primes below 10**6 and brute forcing all possibles sums.
this method take hours.

the tricky is to restrict the set of the primes in which we'll do the nested for-loop
between primes that sums to 10**6!
this is done with: get_sums_under_top.

lesson learned:
	everytime you write a for-loop pay attention how to restrict the bounds.
'''

def maxprimes(max):
	'''thanks riko! get all primes under max.
	'''
	max = int(max)
	limit = int(max**0.5 + 1.5)
	s = set(range(3, max, 2)).difference(
		j for i in range(3, limit, 2) for j in range(i*i, max, i))
	s.add(2)
	return sorted(list(s))

def get_sums_under_top(top, primes):
	'''get the sum length of all consecutive primes below top.
	'''
	s = 0
	for i,p in enumerate(primes):
		s+=p
		if s>top: break
	return i+1

class Num():
	'''class for handle a number and the sum of its parts.
	'''
	def __init__(self, n, sums):
		self.n = n
		self.sums = sums
	def __len__(self):
		return len(self.sums)
	def __repr__(self):
		return "{0}, {1}".format(self.n, len(self))
		#return "{0}, {1}: {2}".format(self.n, len(self)), self.sums)


def make_prime(l, primes):
	'''delegate for construct a Num instance only if it's in primes.
	'''
	s = sum(l)
	if s in primes:
		p = Num(s, l)
		return p
	return None

def sumprimes_gen(primes, limit):
	'''generator for Num instances that contains a prime maked as sum of consecutive primes till limit.
	'''
	set_primes = set(primes) # hashable set for rapid search
	for i in range(limit):
		for j in range(limit-i):
			l = primes[i:i+j]
			p = make_prime(l, set_primes)
			if not p: continue

			if p.n > top: break
			else: yield p

########################################################## solutions

top = 10**6
primes = maxprimes(top) # all primes
print("got {0} primes".format(len(primes)))

primes_to_sum = get_sums_under_top(top, primes) # primes used for sum below 10**6
print("solution is gone to be over {0}° primes".format(primes_to_sum))

goods = list(sumprimes_gen(primes, primes_to_sum))
goods.sort(key=len)
print(goods[-1])
