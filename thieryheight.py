onetonine = [str(i) for i in range(1,10)]
def ispandigit(n):
	return sorted(str(n))==onetonine
assert(ispandigit(918273645))

top = 10000
ns = set([tuple(x for x in range(1,i)) for i in range(1,10)])
def pandigitconcatenation(i,j):
	result = "".join(str(x) for x in map(lambda x:x*i, j))
	if ispandigit(result): return result

r = [pandigitconcatenation(i,j) for i in range(top) for j in ns]
r = list(filter(lambda x:x, r)) # remove None element
print(r)
print(max(r))
