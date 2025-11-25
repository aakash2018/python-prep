from dataclasses import dataclass

values = input("Enter the 3 side of triangle").split()

side1, side2, side3 = map(int, values)
print(side1, side2, side3)


@dataclass
class formTriangle:
    side1: int
    side2: int
    side3: int

    @staticmethod
    def check(side1, side2, side3):
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            print("The three sides can firm a triangle.")
        else:
            print("The three sides cannot form a triangle")


if __name__ == "__main__":
    result = formTriangle(side1, side2, side3)
    result.check(result.side1, result.side2, result.side3)
