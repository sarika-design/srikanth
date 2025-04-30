a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print("Result:", a + b)
elif operation == '-':
    print("Result:", a - b)
elif operation == '*':
    print("Result:", a * b)
elif operation == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")
