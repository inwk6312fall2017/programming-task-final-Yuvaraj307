from collections import Counter

longest = 0

with open('Book1.txt', 'r') as handle:
	for word1 in handle:
		word1.split()
		word1.strip()

with open('Book2.txt', 'r') as handle:
	for word2 in handle:
		word2.split()
		word2.strip()

with open('Book3.txt', 'r') as handle:
	for word3 in handle:
		word3.split()
		word3.strip()

		if len(word1) > len(word2):
			longest = len(word1)
			longest_word = word1
			
		elif len(word2) > len(word3):
			longest = len(word2)
			longest_word = word2
			
		elif len(word1) > len(word3):
			longest = len(word3)
			longest_word = word3
		
	print(longest_word)
 
           

