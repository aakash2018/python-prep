from dataclasses import dataclass

num1, num2, num3 = map(float, input("Enter the value of num1,num2 and num3 ").split())


@dataclass
class isPositive:
    num1: int
    num2: int
    num3: int

    @property
    def checkPositive(self) -> str:
        sum = self.num1 + self.num2 + self.num3
        return "Positive" if sum > 0 else "Negative" if sum < 0 else "Zero"


result = isPositive(num1, num2, num3)
print(result.checkPositive)
