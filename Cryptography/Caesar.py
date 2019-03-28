choice = raw_input("Would you like to:\n1-Encrypt\n2-Decrypt(Brute Force)\n3-Exit\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"

if choice == "1":
	pText = raw_input("Enter the plaintext: ")
	key = int(raw_input("Enter the key: "))
	cText = ""
	for i in pText.lower():
		if i in alphabet:
			cText += alphabet[(alphabet.index(i) + key) % 26] 
	print(cText)
	quit()

if choice == "2":
     	cText = raw_input("Enter the ciphertext: ")
        for i in range(26):	
		pText = ""
        	for j in cText.lower():
                	if j in alphabet:
                        	pText += alphabet[(alphabet.index(j) - i) % 26]
        	print(pText.upper())
	quit()

if choice == "3":
	print("Goodbye.")
	quit()

