class specificNumber:
    def __init__(self):
        self.arr = []
        self.count = 0

    def addNumber(self, num):
        self.arr.append(num)

    def compute(self, target):
        for elment in self.arr:
            if elment == target:
                self.count += 1

        print("The number", target, "appears", self.count, "time(s) in the array.")


if __name__ == "__main__":
    obj = specificNumber()
    n = int(input("Enter the size of the array:"))
    for i in range(n):
        ele = int(input("Enter element {}:".format(i + 1)))
        obj.addNumber(ele)

    target = int(input("Enter the number to search for: "))
    obj.compute(target)
