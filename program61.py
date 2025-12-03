class SumArray:
    def __init__(self):
        self.arr = []

    def addNumber(self, num):
        self.arr.append(num)

    def calculate_sum(self):
        return sum(self.arr)


if __name__ == "__main__":
    obj = SumArray()
    n = int(input("How many numbers? "))

    for _ in range(n):
        num = int(input("Enter number: "))
        obj.addNumber(num)

    print("Sum=", obj.calculate_sum())
