number = int(input("Enter a number: "))
sign = -1 if number < 0 else 1
reversed_number = int(str(abs(number))[::-1]) * sign
print("Reversed number:", reversed_number)
