class Hand(object):
	def __init__(self, s):
		self.cards = sorted([Card(i) for i in s.split()], reverse=True)
		print(self.cards)

	def get_val(self):
		if set(card.number for card in self.cards)=={10,11,12,13,14}:
			return 10
		elif cards[-1].number-cards[0].number==0 and all(card.suit==self.cards[0].suit for card in self.cards):
			return 9
		elif len([1 for card in self.cards if card.suit==self.cards[0].suit])==5:
			return 8
		elif 
		

class Card(object):
	
	def __init__(self, s):

		def suit2number(char):
			suits = [str(c) for c in range(1,11)] + ['J', 'Q', 'K', 'A']
			return suits.index(char)+1

		self.number = suit2number(s[0])
		self.suit = s[1]

	def __repr__(self):
		return "Card: {0} - {1}".format(self.number, self.suit)

	def __eq__(self, other):
		return self.number==other.number and self.suit==self.suit
	def __lt__(self, other):
		return self.number < other.number

if __name__ == "__main__":
	s1 = Hand("5H 5C 6S 7S KD")
