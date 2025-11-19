a =float(input("Enter first number: "))
b =float(input("Enter second number: "))

class Add :
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

    def substract(self):
        return self.a - self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero is not allowed."

    def compute(self):
        return {
            "addition": self.add(),
            "multiplication": self.multiply(),
            "substraction": self.substract(),
            "division": self.divide()
        }                   

result = Add(a, b)
print("The sum is:", result.compute())
