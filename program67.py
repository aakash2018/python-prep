class secondLargest:
    def __init__(self):
        self.arr = []

    def addNumber(self, n):
        self.arr.append(n)

    def compute(self):
        self.arr.sort()
        print("secondLargest:", self.arr[-2])


if __name__ == "__main__":
    obj = secondLargest()
    n = int(input("Enter the size of the array:"))

    print("Enter element for the array:")
    for i in range(n):
        elment = int(input("Enter element {}:".format(i + 1)))
        obj.addNumber(elment)

    obj.compute()
