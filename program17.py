num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2 "))


class biggerOne:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def isBiggerOne(self):
        if self.num1 > self.num2:
            print("num1 is bigger")
        elif self.num1 < self.num2:
            print("num2 is bigger")
        else:
            print("Both number are equal")


result = biggerOne(num1, num2)
result.isBiggerOne()
