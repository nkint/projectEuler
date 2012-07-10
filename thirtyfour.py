def memoize(f):
	d = dict()
	def callable(*args):
		result = d.get(args)
		if not result:
			result = d[args] = f(*args)
		return result
	return callable

@memoize
def factorial_recursive(n):
	#if n>9: print("dudee")
	return (n!=1 and n!=0) and n*factorial(n-1) or 1


import functools as ft
@memoize
def factorial(n):
	#if n>9: print("dudee")
	if n==0 or n==1: return 1
	return ft.reduce(lambda x,y: x*y, range(1,n+1))

def curious(n):
	return n==sum(factorial(int(i)) for i in str(n))

assert(factorial(5)==120)
assert(curious(145))

print(factorial(3))

top = 100000
print( sum(filter(curious, range(3, top))) )
