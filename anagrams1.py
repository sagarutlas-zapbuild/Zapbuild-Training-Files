def anagrams(word, words):
	x = 0
	while (x < len(words)):
		if sorted(words[x]) != sorted(word):
			words.remove(words[x])   
		else:
			x += 1
	print('Final output:\n',words) 	

anagrams('abba', [ 'abcd', 'bbaa', 'dada','abba','ddaa'])
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])