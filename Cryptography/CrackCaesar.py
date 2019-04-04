import sys

ciphFile = sys.argv[1]
dictFile = sys.argv[2]

dictionaryFile = open(dictFile,'r')
cipherFile = open(ciphFile,'r')
dictionary = dictionaryFile.read().split()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(26):
	cipherFile.seek(0)
	pText = ""
	count = 0
	for line in cipherFile:
		for ch in line:
			if ch.lower() in alphabet:
				pText += alphabet[(alphabet.index(ch.lower()) - i) % 26]
			else:
				pText += ch

	for word in pText.split():
		if word in dictionary:
			count = count + 1
	
	if count > len(pText.split())/2:
		print(i)
		print(pText)
		dictionaryFile.close()
		cipherFile.close()
		quit()

dictionaryFile.close()
cipherFile.close()
quit()

