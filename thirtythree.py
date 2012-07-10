import itertools as it
import functools as ft
from fractions import Fraction
from pprint import pprint

def isgood(x):
	# in my opinion project euler #33 is not clear at all.
	# what does it means non-trivial?
	# i found those 3 condition:
	#   1 - the digit of the first fraction to eliminate is not in same position (es. 30 and 50: 0 is in the 2° position)
	#   2 - digit of second fraction is contained in the first
	#   3 - numerator < denominator
	#   
	t1 = list(map(str,x[0]))
	t2 = list(map(str,x[1]))
	s1 = t1[0]
	s2 = t1[1]
	bool1 = s1[0]==s2[1] or s1[1]==s2[0] 
	bool2 = t2[0] in t1[0] and t2[1] in t1[1] 
	bool3 = int(s1)<int(s2)
	return bool1 and bool2 and bool3

assert( isgood([(49,98), (4,8)]) )
assert( not isgood([(98,49), (8,4)]))
assert( not isgood([(30, 50), (3,5)]))

# all fractions with 2 digits number and with 1 digit number

twodigitsnum = it.product(range(10,100), range(10,100))
onedigitsnum = it.product(range(1,10), range(1,10))
twodigitsfractions = list(map(lambda x: (x[0], x[1], Fraction(*x)),twodigitsnum))
onedigitsfractions = list(map(lambda x: (x[0], x[1], Fraction(*x)),onedigitsnum))

# all fractions of 2 digits number and the equivalent 1 digit number fractions
equivalentfractions = [ [(i[:2]),(j[:2])]
				for i in twodigitsfractions 
					for j in onedigitsfractions if i[2]==j[2]!=1]
# find good ones
allgoods = list(map(lambda x: x[0], filter(isgood, equivalentfractions)))
goods = list(filter(lambda x: allgoods.count(x)==1, allgoods))
pprint(goods)

# denominator of product in lowest common terms
n = map(lambda x: x[0], goods)
d = map(lambda x: x[1], goods)
f = Fraction(ft.reduce(lambda x,y: x*y, n), 
	     ft.reduce(lambda x,y: x*y, d))
print(f.denominator)
