
wordnumber = {
0: "zero",  
1: "one",  
2: "two",  
3: "three",  
4: "four",  
5: "five",  
6: "six",  
7: "seven",  
8: "eight",  
9: "nine",  
10: "ten",  
11: "eleven",  
12: "twelve",  
13: "thirteen",  
14: "fourteen",  
15: "fifteen",  
16: "sixteen",  
17: "seventeen",  
18: "eighteen",  
19: "nineteen",  
20: "twenty",  
30: "thirty",  
40: "forty",  
50: "fifty",  
60: "sixty",  
70: "seventy",  
80: "eighty",  
90: "ninety",  
100: "hundred",  
1000: "onethousand" }
#1000: "thousand" }

strings = [' '*1000]

def number2word(n):
	#print("number2word n:{0}".format(n))
	num = str(n)
	if n<20 or (20<=n<100 and n%10==0) or n==1000: 
		   return wordnumber[n]
	elif n<100:
		num0 = int(num[0])
		num1 = int(num[1])
		return wordnumber[num0*10]+wordnumber[num1]
	else:
		assert(len(num)==3)
		num0 = int(num[0])
		num1 = int(num[1:])
		word = ""
		word += wordnumber[num0]+wordnumber[100]
		
		if num1==0: return word
		else: 
			word+="and"
			word += wordnumber.get(num1, number2word(num1))
			return word


#print(number2word(2))
#print(number2word(23))
#print(number2word(123))
#print(number2word(323))
assert(len(number2word(342))==23)
assert(len(number2word(115))==20)
assert(number2word(600)=="sixhundred")

s = list(map(number2word, [i for i in range(1, 1001)]))

for i, string in enumerate(s):
	print("{0} : {1}".format(i+1, string))

s = map(len, s)
print(sum(s))

