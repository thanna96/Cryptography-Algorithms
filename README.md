# Overview:
These programs are designed to help decrypt or encrypt plaintext. Each program has its own specific use 
from encrypting/decrypting to finding primes or factoring integers. 

# 1- Shift Cipher:
This program uses the Caesar cipher to encrypt or decrypt your text.
If you choose to encrypt the program will iterate through your plaintext
and shift each letter by the specified amount. If you choose to decrypt
the program will take your cipher text and print out all 26 possibilities 
of the plaintext. The decryption method is called a Brute Force. 
* Update: I have added the feature to input a file and have the program decrypt/encrypt your text. 
Also, I have added in a dictionary file that is used to decipher the decrypted codes to see which makes most sense.
* Update: I have separated this program into two, one that encrypts and one that decrypts.

# 2- Divisibility Checker:
This program takes input from the user and checks to see if a|b. 

# 3- GCD:
This program utilizes recursion to reproduce the Euclidean algorithm and find the 
greatest common divisor of two integers.

# 4- Modular Arithmetic:
Simple Program that takes in two numbers and finds all the X = a mod b 
from -15 to 15.

# 5- Inverse Mod Calculator:
This program find the inverse of a number a modulo b.
*I will be updating this program to have a faster algorithm in the future.

# 6 - Substitution Cipher:
Takes in the two input files, one with known text and one with 
ciphertext. It then gets the number count of each character
from the known text and uses the count to replace the characters
and outputs the results into a plainttext file.

# 7 - Chinese Remainder Theorem:
This program uses the chinese remainder theorem to find the unique
integer x that is congruent with multiple a mod b. It takes in a 
file with the a mod b and returns the x in the command line.
*I will update the implementation in the future.

# The future programs I will be adding are:
* 8- Affine Cipher
* 9- Vigenere Cipher
* 10- Eulers Function (phi)
* 11- Primitive Root Checker
* 12- Discrete Log
* 13- Prime Number Checker
