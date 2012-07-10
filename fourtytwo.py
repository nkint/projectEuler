import itertools as it
from pprint import pprint

f = open("42.txt", 'r')
names = [name.replace('"','') for name in f.read().split(',')]
f.close()

def sumword(word):
	val = lambda x: ord(x)-ord('a')+1
	return sum(map(val, word.lower()))
assert(sumword("SKY")==55)

def trianglenums():
	n = 1
	while True:
		t = 0.5*n*(n+1)
		n += 1
		yield t, n

ts = map(lambda x: x[0], # take only t on generated tuple t,n
		it.takewhile( lambda x: x[1]<100, # if n<100
			trianglenums() )) #in generator trianglenums
d = dict.fromkeys(ts,True)
print("got triangles")
trianglewords = filter(lambda x:d.get(sumword(x)), names)
print(len(list(trianglewords)))
