def factorial(n):
	if n==1: return 1
	else: return n*factorial(n-1)

assert(factorial(4)==24)

result = sum(map(int, str(factorial(100))))
print(result)
