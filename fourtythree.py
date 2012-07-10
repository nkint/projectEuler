import itertools as it

primes = [2,3,5,7,11,13,17]

def getpandigits(n):
	pandigits = it.permutations("0123456789"[:n],n)
	return list(map(lambda x: "".join(x), it.chain(pandigits)))

def gettriplet(n):
	n = str(n)
	return [n[i:i+3] for i in range(len(n)-2)][1:]

def isgood(n):
	n = gettriplet(n)
	r = list(it.takewhile(lambda x: x[1]%primes[x[0]]==0, 
		               enumerate(map(int, n))))
	return len(r)==len(n)
assert(isgood(1406357289))

pans = getpandigits(10)
print("pandigit gots:"+str(pans[0]))
goods = list(map(int, filter(isgood, pans)))
print("got goods:"+str(goods))
print(sum(goods))

