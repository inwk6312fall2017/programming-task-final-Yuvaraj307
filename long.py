from collections import Counter

longest = 0

with open('Book1.txt', 'r') as handle:
	for word in handle:
		word.split()
		word.strip()
		print(word)
		if len(word) > longest:
			longest = len(word)
			longest_word = word
			print(longest_word)
 
           

