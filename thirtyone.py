import itertools as it

allcash = list(reversed([1, 2, 5, 10, 20, 50, 100, 200]))

def possibility(n, cash, include=False):
	'''return a list of best possibility to achive the bill 'n' with cash. 
	best = less number of cash, and high then possible.'''

	#if n!=0 and min(cash)>n: 
	#	print("min cash < n!! n:{0} cash:{1}".format(n,cash))
	#	return []

	if n==0: return []
	if n==1: return [1]
	else:
		remainedcash = list(sorted([c for c in cash if (include) and c<=n or c<n], reverse=True))
		try:
			money = remainedcash[0]
			result = [money] + possibility(n-money, cash, include=include)
			return result
		except IndexError:
			#no coin in possibles cash could be used.. skip
			print("possibility > except!!!!")
		return []

#for i in range(2, 12):
#	print("{2}: {0}  -  {1}".format(possibility(i, allcash), possibility(i, allcash, include=True), i))
assert(possibility(5, {2,5,10,20,50,100}, include=True) ==[5] )

###############################################################################################
# java: http://blog.csdn.net/No_End_Point/archive/2009/06/26/4301149.aspx
# python: http://adamcolton.net/python/88-euler-31
# ruby: http://tardate.blogspot.com/2008/10/rolling-project-euler-on-ruby.html
#
# theory: 
#    http://en.wikipedia.org/wiki/Subset_Sum
#    http://en.wikipedia.org/wiki/Partition_%28number_theory%29

def possibilities(amount, coins, ways=0):
	#print("possibilities: ",amount,coins)
	if amount==0 or len(coins)==1:
		return amount==0 or amount%coins[0]==0
		#if amount==0: print("dud"); return 1
		#if amount%coins[0]==0: print("dud"); return 1
		#else: return 0
	branches = 0
	for i in range(1+amount//coins[0]):
		branches += possibilities(amount-i*coins[0], coins[1:])
	return branches

print(possibilities(200, allcash))
for i in range(10):
	print("{0}. total:{1}".format(i, possibilities(i, allcash)))



###############################################################################################
# finally
# my way, while+recursion, calculate all possibilities, not only the count of them.
#

[print() for i in range(5)]

allcoins = [1, 2, 5, 10, 20, 50, 100, 200]

def part(n, coins):
	# base della ricorsione
	if n==1:
		return [1]

	parts = []
	# finchè ci sono monete disponibili e abbiamo una cifra positiva da scomporre.. 
	while len(coins)!=0 and n>=0:

		# se abbiamo resto c'è una possibile combinazione
		if n-coins[-1] >= 0:

			# ricorsivamente esploriamo le altre possibili combinazioni
			part(n, coins[:-1])

			n -= coins[-1]
			parts.append(coins[-1])

		# altrimenti passiamo alla moneta successiva
		else:
			coins = coins[:-1]

	# trovata una combinazione?
	update(parts)
	return parts

def update(array):
	global total
	if array: total += 1

for i in range(10):
	total = 0
	part(i, allcoins)
	print("{0}. total:{1}".format(i, total))

total = 0
part(200, allcoins)
print(total)


############################ BEST ONE ############################à
############################ written in c
############################ il più leggibile.
#       #include <stdio.h>
#        
#       int coins[8] = {200, 100, 50, 20, 10, 5,2,1};
#        
#       int findposs(int money, int maxcoin)
#       {
#       	int sum = 0;
#               if(maxcoin == 7) return 1;
#       	for(int i = maxcoin; i<8;i++)    {
#       	        if (money-coins[i] == 0) sum+=1; // perfetta divisione, arrivati ad una foglia
#       	        if (money-coins[i] > 0) sum+=findposs(money-coins[i], i);
#       	}
#               return sum;     
#       }
#        
#       int main()
#       {
#           printf("%d",findposs(200, 0));
#       }
