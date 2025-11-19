a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
class aritmeticTwoNum:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def addition(self):
        return self.a + self.b //2

    def compute(self):
        return {
          "mean": self.addition()
        } 

result = aritmeticTwoNum(a,b)
print("The sum is:", result.compute())