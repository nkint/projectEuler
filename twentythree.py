import itertools as it
from pprint import pprint

def divisors(n):
	return set(it.chain(*[(x,divmod(n,x)[0]) for x in range(2,int(n**0.5)+1) if n%x==0]))
	'''
	same algorithm to find prime factors but add also n/=prime every pass
	this is a nice solution with built-in function divmod
	from 
	http://www.progsoc.uts.edu.au/wiki/index.php?title=Euler_Solution_95&printable=yes
	
	d =[1,] 
	for x in range(2,(int(n**0.5)+1)):
		res,rem = divmod(n,x)
		if rem == 0:
			d.append(x)
			d.append(res)
	return set(d)
	'''

def isabundant(n):
	return sum(divisors(n))>n

top = 28124
abundants = [n for n in range(1,top) if isabundant(n)]
adict = dict.fromkeys(abundants, 1)

def f(x):
	x1 = x[0]
	x2 = x[1]
	n = x1-x2
	if x2>x1: return 0
	if adict.get(n):
		return 1
	return 2

t = 0
for i in range(1, top):
	got = False
	for a in abundants:
		condition = f([i,a])
		if condition==0: 
			break
		elif condition==1: 
			got = True
			break
		else: pass
	if not got: 
		t= t+i

print(t)





