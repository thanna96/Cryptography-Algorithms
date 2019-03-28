def modSet(a,b):
	modSet = []
	for i in range(-15,15):
		num = b * i + a
		modSet.append(num)
	print(modSet)	
		
print("Enter two integers a and b s.t. x = a mod b:")
a = int(raw_input("a: "))
b = int(raw_input("b: "))
modSet(a,b)

