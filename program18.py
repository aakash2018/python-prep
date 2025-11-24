num1 = int(input("enter the num1 "))
num2 = int(input("enter the num2 "))
num3 = int(input("enter the num3 "))


class largestNum:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def isLargestOne(self):
        if self.num1 >= self.num2 and self.num1 >= self.num3:
            return self.num1
        elif self.num2 >= self.num1 and self.num2 >= self.num3:
            return self.num2
        else:
            return self.num3

    def compute(self):
        return {"largestNum is": self.isLargestOne()}


result = largestNum(num1, num2, num3)
print(result.compute())
