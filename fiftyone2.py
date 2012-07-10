import itertools as it

def maxprimes(max):
	'''thanks riko! get all primes under max.
	'''
	max = int(max)
	limit = int(max**0.5 + 1.5)
	s = set(range(3, max, 2)).difference(
		j for i in range(3, limit, 2) for j in range(i*i, max, i))
	s.add(2)
	return s

primes = set(maxprimes(1000000))

def memoize(f):
	f.cache = dict()
	def decorator(*n, **k):
		_k = k.get('k')
		if (n,_k) not in f.cache:
			f.cache[ n,_k ] = f(*n, **k)
		return f.cache[ n,_k ]
	return decorator

#@memoize
def combine(s, n, k=1):
	if k<=0: return
	
	for i in range(len(s)+1):
		r = s[:i] + str(n) + s[i:]
		if k==1: 
			#if int(r) in primes:
			yield r
		else:
			for j in combine(r,n,k-1):
				yield j

def foo(s, starnumber=3):
	for k in range(starnumber):
		r = set()
		for n in {0,1,2,3,4,5,6,7,8,9}:
			#r = set( combine(str(s), n, k) )
			r.update(set( combine(str(s), n, k) ))
			#if k==2: print(r)
		#if {'56003', '56113', '56333', '56443', '56663', '56773', '56993'}.issubset(r):
		#	print('dudee',s ,r)
		#if s==563: print('________________',r)
	
	return r

foo(563)

#print(foo(233, 3))

for s in range(600):
	_i = foo(s, 3)


	# select only primes
	r = list( filter(lambda x:int(x) in primes, _i) )
	
	if s==563: print('-------------', _i, r)

	# select only 8 primes
	r = list(r)
	if len(r)<=7: continue

	# discard '00x' number
	r_len = list(map(lambda x: len(str(x)), r))
	try:
		one, = set(r_len)
	except:
		continue
	print(min(r), '  -->   ', r, one)

	if s==233:
		from pprint import pprint
		pprint(r)
