from pprint import pprint
from operator import itemgetter

class NameScore():
	name = ""
	position = 0
	value = 0
	def __init__(self,name): 
		self.name=name
		self.value = sum([ord(char)-96 for char in name])
	def __str__(self):
		return "name:{0} value:{1} position:{2} total:{3}".format(
				self.name, 
				self.value, 
				self.position, 
				self.total)
	total = property(lambda x: x.position*x.value)	

file = open("22.txt",'r')
rawstring = file.read()
file.close()

names = [NameScore( n.replace('"','').lower() ) 
		for n in rawstring.split(',')]

alphs = sorted(names, key=lambda x:x.name)

def assign_position(x): 
	x.position=alphs.index(x)+1
	return x
alphs = list(map(assign_position, alphs))

#n = alphs[937]
#print(n)

totals = sum([i.total for i in alphs])
print(totals)
