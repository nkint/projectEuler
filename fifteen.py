# Starting in the top left corner of a 2×2 grid, there are 6 routes (without backtracking) to the bottom right corner.

# ... fucking math. if 'a' is down and 'b' is left
#                   all movement to the bottom right corner
#		    are all balanced 20char-long-string (itertools.product) on alphabet 'ab'
# ... but this solution is incredibly slow
# so we have to use pascal's triangle.
# 
# http://blog.functionalfun.net/2008/07/project-euler-problem-15-city-grids-and.html



import unittest

# first of all, calculate pascal's triangle

class PascalTriangle():
	def __init__(self): 
		self.lines = [[1]]
	def __iter__(self): return self
	def __next__(self): 
		preline = self.lines[-1]
		return self.newline(preline)
	def newline(self, preline):
		try:
			newline = [1] + [preline[i]+preline[i+1] 
						  for i in range(len(preline)-1)] + [1]
		except IndexError: newline = [1,1]
		self.lines.append(newline)
		return newline

knownPascal = [
		#[1],
		[1,1],
		[1,2,1],
		[1,3,3,1],
		[1,4,6,4,1]
	     ]

class Test(unittest.TestCase):
	def test_pascal(self):
		itr = iter(PascalTriangle())
		for i in range(len(knownPascal)):
			self.assertEqual(knownPascal[i], next(itr))	

	def test_15euler(self):
		itr = iter(PascalTriangle())
		c = 1 
		while c<21:
			l = next(itr)
			f = lambda x: (x%2 != 0) and (x-1)//2 or 0
			index = f(len(l))
			if index!=0:
				print("{0}: {1}".format(c,l[index]))
				c+=1
			else: print() 



unittest.main()
