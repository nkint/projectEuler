def is_palindrome(n):
	return str(n)==str(n)[::-1]
def sum_reverse(n):
	return n+int( str(n)[::-1] )

lychrels = dict()
def lychrel(m):
	n = m
	for i in range(1,50):
		n = sum_reverse(n)
		if is_palindrome(n): return False
	lychrels[m]=i
	return True

print(lychrel(47))
print(lychrel(349))
print(lychrel(4994))
print(lychrel(196))

count=0
for i in range(2, 10001):
	if lychrel(i): count+=1

print(count)
from pprint import pprint
pprint(lychrels)

print(len(lychrels))
