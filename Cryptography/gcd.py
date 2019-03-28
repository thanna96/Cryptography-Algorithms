def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b,a%b)

print("Enter two integers")
a = int(raw_input("a:"))
b = int(raw_input("b:"))

print(gcd(a,b))
