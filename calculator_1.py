# Simple calculator with basic arithmetic operation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def modulo(x, y):
    if y != 0:
        return x % y
    else:
        return "Error! Division by zero."

def main():
    print("Simple Calculator!")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")

    operation = input("Enter the number corresponding to the operation (1/2/3/4/5): ")

    if operation == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is {result}.")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is {result}.")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is {result}.")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} is {result}.")
    elif operation == '5':
        result = modulo(num1, num2)
        print(f"The result of {num1} % {num2} is {result}.")
    else:
        print("Invalid operation choice! Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
