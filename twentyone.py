
def memoize(f):
	results = dict()
	def decorator(*n):
		try:
			r = results[n]
		except:
			r = f(*n)
			results[n] = r
		return r
	return decorator

@memoize
def divisors(n):
	return [i for i in range(1,n//2+1) if n%i==0]

# assert test
#div220 = [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
#assert(divisors(220)==div220)

def d(n): return sum(divisors(n))
def amicable(a,b):
	if a==d(b) and b==d(a):
		return a,b
	else: return False

import itertools as it

#more then 10 minutes of computations..

top = 10001
nums = it.combinations(range(1,top), 2)
amicables = list(filter(lambda x: amicable(*x), nums))

print(amicables)
print(sum(it.chain(*amicables)))


