num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


class Divisible:
    def __init__(self):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def isDivisible(num1, num2) -> str:
        if num1 % num2 == 0:
            return "divisible"
        else:
            return "not divisible"


if __name__ == "__main__":
    result = Divisible()
    print(result.isDivisible(result.num1, result.num2))
