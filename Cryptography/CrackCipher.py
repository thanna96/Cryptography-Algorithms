import sys

alphabet = "abcdefghijklmnopqrstuvwxyz "
cFile = sys.argv[1]
kFile = sys.argv[2]

def read_text(file):
	Dict = {}
	for c in alphabet:
		Dict[c] = 0
	with open(file) as f:
		for line in f:
			for ch in line:
				if ch.lower() in alphabet:
					Dict[ch.lower()] += 1 
	return Dict

def map_letters(known,cipher):
	mappings = {}
	cipherKeys = []
	knownKeys = []
	
	for key, value in sorted(cipher.iteritems(),key = lambda (k,v): (v,k)):
		cipherKeys += key
	
	for key, value in sorted(known.iteritems(),key = lambda (k,v): (v,k)):
		knownKeys += key
	
	for i in range(len(knownKeys)):
		mappings[cipherKeys[i]] = knownKeys[i]
	
	return mappings

def decrypt(ciphertext,mapping):
	pText = ""
	with open(ciphertext) as f:
		for line in f:
			for ch in line:
				if ch.lower() in alphabet:
					pText += mapping[ch.lower()]
				else:
					pText += ch
	print pText
	
freqCipher = read_text(cFile)
freqKnown = read_text(kFile)
mapping = map_letters(freqKnown,freqCipher)
decrypt(cFile,mapping)
quit()
