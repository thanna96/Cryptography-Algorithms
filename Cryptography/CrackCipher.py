#Thomas Hanna - Substitution Cipher Decryptor

#imports:
import sys

#Variables:
alphabet = "abcdefghijklmnopqrstuvwxyz "
cFile = sys.argv[1]
kFile = sys.argv[2]

#Reads the input files and counts the number of each letter
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

#Creates the mappings for the letters 
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

#iterates through the cipher text file and replaces letters according to the mapping
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
