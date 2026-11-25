number = input("Enter a number: ").strip()

if number == number[::-1]:
	print(f"{number} is a palindrome.")
else:
	print(f"{number} is not a palindrome.")
