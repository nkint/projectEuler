import itertools as it


top = 1000000
# canonical prime generation
#def isprime(n):
#	return not [i for i in range(1,int(n**0.5)+1) if n%i==0]
#primes = [i for i in range(top+1) if isprime(i)]
#d = dict.fromkeys(primes, True)

# eratostene sieve
nums = [True]*top
for i in range(2,top):
	for j in range(i*2,top, i):
		if nums[j]!=False: nums[j] = False

primes = list(filter(lambda x:nums[x], range(2,top)))
d = dict.fromkeys(primes, True)
print("got primes")

def getcircular(n):
	n = str(n)
	t = [  "".join( [n[i:],n[:i]] ) 
			for i,s in enumerate(n)]
	return list(map(lambda x: int(x), t))

def iscircularprime(n):
	l = getcircular(n)
	return l == list(filter(d.get, l))

############################################################
# assertion test
assert(iscircularprime(11))
assert(iscircularprime(19)==False)
l = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79]
for i in l:
	assert(iscircularprime(i))
ltest = list(filter(iscircularprime, range(1,80)))
############################################################

circularprimes = list(filter(iscircularprime, primes))
print(len(circularprimes))

