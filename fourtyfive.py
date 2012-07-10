
# triangle could be avoided due to
# strong connectwion between triangle and hexagonal number..
#triangle = lambda n: n*(n-1)/2  
pentagonal = lambda n: n*(3*n-1)/2
hexagonal = lambda n: n*(2*n-1)

def make_generator(f):
	def generator(limit):
		return set([f(i) for i in range(100,limit)])
	return generator

sets = [make_generator(f)(100000) for f in
		#[triangle, pentagonal, hexagonal]]
		[pentagonal, hexagonal]]

print(sets[0].intersection(*sets[1:]))
