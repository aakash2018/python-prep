from dataclasses import dataclass

num = int(input("Enter a number: "))


@dataclass
class displayTable:
    num: int

    @staticmethod
    def showTable(num) -> int:
        for i in range(1, 11):
            print(num, "X", i, "=", i * num)


if __name__ == "__main__":
    result = displayTable(num)
    result.showTable(result.num)
