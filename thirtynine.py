elevtwo = {i:i**2 for i in range(1001)}
print("got exponential nums")

def get_possibility(p):
	for a in range(1,p//2):
		for b in range(a,p//2):
			c = (elevtwo.get(a) + elevtwo.get(b))**0.5
			if a+b+c==p: yield a,b,c

r = [set(i for i in get_possibility(p)) for p in range(1,1001)]

rlen = list(map(len, r))
maxpossibility = list(r[rlen.index(max(rlen))])[0]
print(maxpossibility)

print(sum(maxpossibility))
