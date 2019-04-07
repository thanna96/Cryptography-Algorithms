#Thomas Hanna - Chinese Remainder Theorem Calculator 
#Performs CRT to find unique x value 

#imports:
import sys

file = sys.argv[1]

#gets a and b value from file
def getInput():
	bArray = ""
	aArray = ""
	with open(file) as f:
		for line in f:
			words = line.split()
			bArray += " "
			aArray += " "
			bArray += words[-1]
			aArray += words[2]
	return aArray, bArray

#returns gcd of 2 integers
def getGCD(x,y):
	x = int(x)
	y = int(y)
	if y == 0:
		return x
	else:
		return getGCD(y, x%y)

#find the inverse of a number 
def inverse(num1,num2):
	n = 0
	i = 0
	if getGCD(num1,num2) != 1:
		return None
	else:
		while n != 1:
			i = i + 1
			n = num1*i % num2
			if n == 1:
				return i

#does the CRT and finds x
def CRT(a,b):
	a = map(int, a)
	b = map(int, b)
	
	k = ((a[1] - a[0]) * inverse(b[0],b[1])) % b[1]
	x = (a[0] + (k * b[0])) % (b[0] * b[1])
	l = ((a[2] - (x % b[2])) * (inverse((b[0] * b[1] % b[2]),b[2]))) % b[2]
	x2 = (x + b[0] * b[1] * l) % (b[0] * b[1] * b[2])
	
	return x2

a,b = getInput()		
a = a.split()
b = b.split()		

gcd = getGCD(b[0],b[1])

if gcd != 1:
	print "there is no unique solution"
	quit()
	
for i in range(2,len(b)):
	gcd = getGCD(gcd,b[i])

#will only do the CRT gcd of all b == 1
if gcd == 1:
	print CRT(a,b)

else:
	print "There is no unique solution"
	quit()
