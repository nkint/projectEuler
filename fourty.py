import functools as ft
top = 1000000
string = "".join(str(i) for i in range(top+1))
elementindex = [10**i for i in range(7)]
elements = map(int, [string[i] for i in elementindex])
print(ft.reduce(lambda x,y:x*y, elements))
