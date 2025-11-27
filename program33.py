from dataclasses import dataclass

num = int(input("Enter an integer: "))


@dataclass
class isDivisible:
    @staticmethod
    def compute(num) -> str:
        if num % 3 == 0 and num % 5 == 0:
            return "divisible by 3 and 5"
        else:
            return "not divisible by 3 and 5"


if __name__ == "__main__":
    result = isDivisible()
    print(result.compute(num))
