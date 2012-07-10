import itertools as it
import operator

# http://www.visualbasicscript.com/m69988.aspx
# 
# Experimenting with the calculator I came up with two different scenarios_
# that could possibly produce a 9 digit pandigital identity.
# 
# axbbbb=cccc
# and
# aaxbbb=cccc 

onetonine = list(sorted([str(i) for i in range(1,10)]))
def ispandigital(*args):
	return list(sorted("".join([str(i) for i in args])))==onetonine
assert(ispandigital(39,186,7254))

xy = it.chain(it.product(range(10,100), range(100,1000)),it.product(range(10), range(1000, 100000)))
xyp = map(lambda x: (x[0],x[1],operator.mul(*x)), xy)
pandigits = list(filter(lambda x: ispandigital(*x), xyp))
pandigitsprod = set(map(lambda x: x[2], pandigits))
print(pandigits)
print(sum(pandigitsprod))

