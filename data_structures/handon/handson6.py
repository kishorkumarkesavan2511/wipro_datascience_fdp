number = int(input("Enter a number: "))

if number > 1:
	for divisor in range(2, int(number ** 0.5) + 1):
		if number % divisor == 0:
			print(number, "is not prime")
			break
	else:
		print(number, "is prime")
else:
	print(number, "is not prime")
