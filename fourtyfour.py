import time
import itertools as it
from pprint import pprint

#def pentagonal():
#	n = 1
#	while True:
#		t = n*(3*n-1)/2
#		n += 1
#		yield n, t
#t = time.time()
#plist = list(map(lambda x:x[1], 
#		it.takewhile(lambda x:x[0]<2500, pentagonal() )))
#print("pentagonals with functional in:{0}".format(time.time()- t))

t = time.time()
plist = [n*(3*n-1)/2 for n in range(1,2500)]
print("pentagonals with lc in:{0}".format(time.time()- t))

pentagonals = dict.fromkeys(plist, True)
def goodpair(x,y):
	return pentagonals.get(x+y) and pentagonals.get(y-x)

good = [(vi,vj) for i,vi in enumerate(plist) 
		for j,vj in enumerate(plist[i+1:]) if goodpair(vi, vj)]
diffs = map(lambda x: x[1]-x[0], good)
print(min(diffs))
