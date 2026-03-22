# Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
print("Addition =", add(num1, num2))
print("Subtraction =", subtract(num1, num2))
print("Multiplication =", multiply(num1, num2))
print("Division =", divide(num1, num2))
print("Power =", power(num1, num2))