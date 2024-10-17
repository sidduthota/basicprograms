class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"

    def modulus(self):
        if self.b != 0:
            return self.a % self.b
        else:
            return "Error: Division by zero"


def perform_operation(a, b, operation):
    calc = Calculator(a, b)

    if operation == 'add':
        return calc.add()
    elif operation == 'subtract':
        return calc.subtract()
    elif operation == 'multiply':
        return calc.multiply()
    elif operation == 'divide':
        return calc.divide()
    elif operation == 'modulus':
        return calc.modulus()
    else:
        return "Invalid operation"


# Example usage:
try:
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    operation = input("Enter the type of operation (add, subtract, multiply, divide, modulus): ").lower()

    result = perform_operation(a, b, operation)
    print(f"The result of the {operation} operation is: {result}")
except ValueError:
    print("Invalid input. Please enter numeric values for a and b.")