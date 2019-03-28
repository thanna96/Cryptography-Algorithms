i = 1
while i == 1:
	print("Enter two numbers a|b : ")
	a = int(raw_input("a: "))
	b = int(raw_input("b: "))

	if (b%a) == 0:
		print("a divides b")
		print("Press 1 to try different numbers\n0 to quit")
		i = int(raw_input())
	else:
		print("a does not divide b")
		print("Press 1 to try different numbers\n0 to quit")
		i = int(raw_input())
quit()
