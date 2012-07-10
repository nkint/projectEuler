################################################## brute forxe

def w(tdag, path):
	print('w',tdag,path)
	e = []
	for i,v in enumerate(path):
		e.append( tdag[i][v] )
	return sum(e)

t = [[1],[1,2]]
assert(w(t,(0,1))==3)
t = [[1],[1,2], [1,2,3]]
assert(w(t,(0,1,2))==6)

def search_max(tdag):
	if len(tdag)==1:
		return (0,)
	else:
		print('search_max', tdag)
		left = [ [col for col in row[:-1]] for row in tdag[1:] ]
		right = [ [col for col in row[1:]] for row in tdag[1:] ]
		print(left)
		print(right)

		path1 = (0,) + search_max(left)
		path2 = (0,) + tuple(x+1 for x in search_max(right))

		if w(tdag, path1)>w(tdag, path2):
			return path1
		else:
			return path2

t = [[1],[2,3],[4,5,6]]
print(search_max(t))
t = [[1],[2,3],[2,3,9]]
print(search_max(t))

######################################## cool one
def foo(s,l):
	a = [x+y for x,y in zip(s,l)]
	b = [x+y for x,y in zip(s[1:],l)]
	return [max(x) for x in zip(a,b)]
from functools import reduce
print(reduce(foo, t[::-1]))
