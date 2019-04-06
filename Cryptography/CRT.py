import sys

file = sys.argv[1]

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

def getGCD(x,y):
	x = int(x)
	y = int(y)
	if y == 0:
		return x
	else:
		return getGCD(y, x%y)

def inverse(num):

def CRT(a,b):
	

a,b = getInput()		
a = a.split()
b = b.split()		

gcd = getGCD(b[0],b[1])

for i in range(2,len(b)):
	gcd = getGCD(gcd,b[i])

if gcd == 1:
	CRT(a,b)

else:
	quit()
