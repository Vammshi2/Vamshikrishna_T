class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Division by zero error"
        return self.a / self.b


# Usage
calc = Calculator(10.5, 5.5)
operation = "add"

if operation == "add":
    print(calc.add())
elif operation == "subtract":
    print(calc.subtract())
elif operation == "multiply":
    print(calc.multiply())
elif operation == "divide":
    print(calc.divide())

