def maxprimes(max):
	'''thanks riko! get all primes under max.
	'''
	max = int(max)
	limit = int(max**0.5 + 1.5)
	s = set(range(3, max, 2)).difference(
		j for i in range(3, limit, 2) for j in range(i*i, max, i))
	s.add(2)
	return s

def combine(s, k, m):
	#print("combine", s, k, m)
	if k==0:
		return [s]
	if k==len(s):
		return [str(m)*k]
	if k>len(s):
		return []
	else:
		p = []
		p.extend( [s[0]+i for i in combine(s[1:], k, m)] )
		p.extend( [str(m)+i for i in combine(s[1:], k-1, m)] )
		return p



import unittest

class Test(unittest.TestCase):
	def test_combine_syntax(self):
		for i in range(50):
			s = str('m')*(i+2)
			n = combine(s,i,'0')
			nums_of_zero = [s.count('0') for s in n]
			self.assertTrue(all([j==i for j in nums_of_zero]), 
					"Number of substitued char: failed in {0} with {1}".format(i, n))
			self.assertTrue(all([len(j)==i+2 for j in n]),
					"Length of returned word: failed in {0} with {1}".format(i,n))

	def test_combine_known(self):
		s = set
		known = ['01', '10']
		self.assertEquals( s(combine('11',1,'0')), 
				   s(known))

		known = ['0033', '0303', '0330', '3003', '3030', '3003', '3300']
		self.assertEquals( s(combine('3333', 2, '0')),
				   s(known))

	def test_on_prime_small(self):
		primes = maxprimes(100)
		word = "33"
		combos = []
		for i in range(10):
			combos.extend( combine(word, 1, i) )
		obtained_primes = [i for i in map(int,combos) if i in primes]
		self.assertEquals(len(obtained_primes), 9)

	def test_project51(self):
		primes = sorted(maxprimes(10000))
		for p in primes:
			for i in range(len(primes)):
				combos = []
				for j in range(6, 10):
					combos.extend( combine(str(p), i, str(j)) )
				obtained_primes = set([i for i in map(int, combos) if i in primes])
				if len(obtained_primes)==8: 
					print("got it, \nprime is {0} \ncombos: {1}\nobtained primes:{2}".format(p,combos, obtained_primes))
					assert(False)

unittest.main()
#print(combine('11',1,'0'))
#print(combine('3333', 2, '0'))
#primes = maxprimes(10e5)

