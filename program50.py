from dataclasses import dataclass

n = int(input("Enter a number (negative number to exit): "))


@dataclass
class SumOfPositive:
    n: int

    @property
    def showNumber(self):
        sum_positive = 0
        num = self.n

        while True:
            if num >= 0:
                sum_positive += num
            else:
                break

            num = int(input("Enter a number (negative number to exit): "))

        print("Sum of positive numbers:", sum_positive)


if __name__ == "__main__":
    result = SumOfPositive(n)
    result.showNumber
