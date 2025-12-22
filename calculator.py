def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print("Welcome to the Calculator")

continue_calc = True

num1 = float(input("Enter the first number: "))

while continue_calc:
    print("\nAvailable operations:")
    for op in operations:
        print(op)

    operator = input("Choose an operation: ")

    if operator not in operations:
        print("Invalid operation")
        continue

    num2 = float(input("Enter the next number: "))

    result = operations[operator](num1, num2)
    print("Result:", result)

    choice = input("Do you want to continue? (yes/no): ").lower()

    if choice == "yes":
        num1 = result   # store result for next calculation
    else:
        continue_calc = False
        print("Thank you for using the calculator!")
