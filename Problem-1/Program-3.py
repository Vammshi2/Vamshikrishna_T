# Using a Dictionary for Operation Mapping

class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        self.operations = {
            "add": lambda: self.a + self.b,
            "subtract": lambda: self.a - self.b,
            "multiply": lambda: self.a * self.b,
            "divide": self.safe_divide
        }

    def safe_divide(self):
        return "Division by zero error" if self.b == 0 else self.a / self.b

    def compute(self, operation: str):
        operation = operation.lower()
        return self.operations.get(operation, lambda: "Invalid operation")()


calc = Calculator(a,b)
print(calc.compute("Multiply"))
