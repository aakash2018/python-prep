class largestElement:
    def __init__(self):
        self.arr = []

    def addNumber(self, num):
        self.arr.append(num)

    def checkLargest(self):
        self.largest = self.arr[0]
        for i in range(1, len(self.arr)):
            if self.arr[i] > self.largest:
                self.largest = arr[i]

    @property
    def compute(self):
        self.checkLargest()
        print("Largest element:", self.largest)


if __name__ == "__main__":
    obj = largestElement()
    n = int(input("Enter the number of element: "))

    for i in range(n):
        num = int(input("Enter number: "))
    obj.addNumber(num)

    obj.compute
