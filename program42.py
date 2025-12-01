from dataclasses import dataclass

num = int(input("Enter a number: "))


@dataclass
class displayTable:
    num: int

    @staticmethod
    def showTable(num) -> int:
        sum_of_numbers = 0
        for i in range(1, num + 1):
            sum_of_numbers += i

        print("The sum of numbers from 1 to", num, "is:", sum_of_numbers)


if __name__ == "__main__":
    result = displayTable(num)
    result.showTable(result.num)
