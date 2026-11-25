for number in range(10, 100):
	if all(number % divisor != 0 for divisor in range(2, int(number**0.5) + 1)):
		print(number)
