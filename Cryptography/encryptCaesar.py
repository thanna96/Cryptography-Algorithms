import sys

plaintextFile = open(sys.argv[1],'r')
ciphertextFile = open("ciphertext.txt",'w')

alphabet = "abcdefghijklmnopqrstuvwxyz"

key = int(raw_input("Enter the key: "))
cText = ""

for line in plaintextFile:
	for ch in line:
		if ch.lower() in alphabet:
			cText += alphabet[(alphabet.index(ch.lower()) + key) % 26]
		else:
			cText += ch
ciphertextFile.write(cText)
print(cText)
ciphertextFile.close()
plaintextFile.close()
quit()

