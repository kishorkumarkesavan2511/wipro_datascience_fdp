number = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(abs(number)))
print(digit_sum)
