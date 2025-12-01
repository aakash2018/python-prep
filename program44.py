from dataclasses import dataclass

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))


@dataclass
class CalculateExponent:
    @classmethod
    def calculate(cls) -> int:
        resultOne = 1
        for _ in range(1, exponent + 1):
            resultOne = resultOne * base
        return resultOne


if __name__ == "__main__":
    print(CalculateExponent.calculate())
