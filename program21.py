num = float(input("Enter a number:"))


class isNegativeOrZero:
    def __init__(self, num):
        self.num = num

    def checkNegative(self):
        if self.num > 0:
            print("The number is positive.")
        elif self.num < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")


result = isNegativeOrZero(num)
result.checkNegative()
