class averageDisplay:
    def __init__(self):
        self.arr = []

    def addNumber(self, num):
        self.arr.append(num)

    def calculate(self):
        self.sum = 0
        for ele in self.arr:
            self.sum += ele

    def average(self):
        self.averages = self.sum / len(self.arr)

    @property
    def compute(self):
        self.average()
        print("Average:", self.averages)


if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    obj = averageDisplay()

    for i in range(n):
        ele = int(input("Enter element {}:".format(i + 1)))
        obj.addNumber(ele)

    obj.calculate()
    obj.compute
