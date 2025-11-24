from dataclasses import dataclass

num1, num2, num3 = map(int, input("Enter the number1 number2 and number3 ").split())


@dataclass
class isDivisible:
    num1: int
    num2: int
    num3: int

    def isCheck(self):
        self.sum_of_num = num1 + num2 + num3
        if self.sum_of_num % 5 == 0:
            print("The sum is divisible by 5.")
        else:
            print("The sum is not divisible by 5.")


result = isDivisible(num1, num2, num3)
result.isCheck()
