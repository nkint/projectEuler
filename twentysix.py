from fractions import Fraction
from pprint import pprint

class Frac(Fraction):
	def periodicdecimals(self, limit=10000):
		'''return only periodic parts, if there is, in decimal parts unitl 'limit' digits'''
		n = self.numerator
		d = self.denominator

		decimals = ""
		rests = []

		n = n%d
		# algo from http://it.wikipedia.org/wiki/Numero_decimale_periodico
		for i in range(limit):
			decimals += str(n*10//d)
			n = (n*10)%d
			if n in rests:
				return decimals[rests.index(n):]
			else:
				rests.append(n)
				
top = 1000
fracts = [Frac(1,i).periodicdecimals() for i in range(1,top+1)]
lenfracts = [len(str(i)) for i in fracts]
maxindex = lenfracts.index(max(lenfracts))
print( maxindex+1  )
