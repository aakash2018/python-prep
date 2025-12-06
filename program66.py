class reverseArray:
    def __init__(self):
        self.arr = []

    def addNumber(self, num):
        self.arr.append(num)

    def compute(self, n):
        self.start = 0
        self.end = n - 1

        while self.start < self.end:
            self.arr[self.start], self.arr[self.end] = (
                self.arr[self.end],
                self.arr[self.start],
            )
            self.start += 1
            self.end -= 1

        print("Elements in reverse order:")

        for ele in self.arr:
            print(ele)


if __name__ == "__main__":
    obj = reverseArray()
    n = int(input("Enter the size of the array"))

    print("enter elements for the array:")

    for i in range(n):
        ele = int(input("Enter the element{}:".format(i + 1)))
        obj.addNumber(ele)

    obj.compute(n)
