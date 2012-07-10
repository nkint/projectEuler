def fib():
	a,b = 0, 1
	while True:
		yield a
		a,b = b, a+b
itr = fib()
n = 0
for i in itr:
	if len(str(i))>=1000: break
	else: n+=1

#while len(str(next(i)))<=1000: n+=1

print(len(str(i)))
print(n)
