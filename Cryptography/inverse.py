#Thomas Hanna - inverse calculator
#Finds the inverse of a number mod x if it has one

#find the GCD using Euclideans algorithm
def gcd(a,b):
	if b == 0:
		return a 
	else:
		return gcd(b,a%b)

#finds the inverse using a brute force method
def inverse(a,b):
	n = 0
	i = 0
	if gcd(a,b) != 1:
		return None
	else:
		while n != 1:
			i = i + 1
			n = a*i % b
			if n == 1:
				return i

a = int(raw_input("Enter integer: "))
b = int(raw_input("Enter Modulo: "))
print(inverse(a,b))

