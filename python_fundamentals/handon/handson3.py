def lastDigit(a, b):
    return a % 10 == b % 10

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The last digits of the two numbers are the same:", lastDigit(a, b))

