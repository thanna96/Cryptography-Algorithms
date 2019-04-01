import sys

ciphFile = sys.argv[1]
dictFile = sys.argv[2]

dictionaryFile = open(dictFile,'r')
cipherFile = open(ciphFile,'r')

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(26):
	cipherFile.seek(0)
	dictionaryFile.seek(0)
	pText = ""
	for line in cipherFile:
		for ch in line:
			if ch.lower() in alphabet:
				pText += alphabet[(alphabet.index(ch.lower()) - i) % 26]
			else:
				pText += ch

	for word in pText.split():
		if word in dictionaryFile.read():
			print(pText)
			print(i)
			dictionaryFile.close
			cipherFile.close
			quit()
		else:
			break 

dictionaryFile.close()
cipherFile.close()
quit()

