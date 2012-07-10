import time

top = 800000

#t = time.time()
## eratostene sieve
#nums = [True]*top
#for i in range(2,top):
#	for j in range(i*2,top, i):
#		if nums[j]!=False: nums[j] = False
#
#primes = list(filter(lambda x:nums[x], range(2,top)))
#d = dict.fromkeys(primes, True)
##print(d.keys())
#print("got primes with sieve in:{0}".format( time.time()-t ))

t = time.time()
nonprimes = set(j for i in range(2,top) for j in range(i*2, top, i))
primes = [i for i in range(2,top) if i not in nonprimes]
d = dict.fromkeys(primes, True)
#print(d.keys())
print("got primes with functional sieve in:{0}".format( time.time()-t ))

print("got primes")

def removedigits(n):
	n = str(n)
	for i,c in enumerate(n):
		yield str(n)[:i+1]
		yield str(n)[i:]

def isgood(n):
	r = ([d.get(int(i)) for i in removedigits(n)])
	return all(r)
assert(isgood(3797))


goods = [i for i in d.keys() if isgood(i) and i>7]
print(goods,len(goods))
print(sum(goods))
