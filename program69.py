class multiplicationArray:
    def __init__(self):
        self.arr1 = []
        self.arr2 = []
        self.result_vector = []

    def addNumber1(self, num):
        self.arr1.append(num)

    def addNumber2(self, num):
        self.arr2.append(num)

    def compute(self, n):
        for i in range(n):
            self.result_vector.append(self.arr1[i] * self.arr2[i])
        print("Resulting array", self.result_vector)


if __name__ == "__main__":
    obj = multiplicationArray()
    size = int(input("Enter the size of the arrays: "))

    print("Enter elements for array 1:")
    for i in range(size):
        element = int(input("Enter element {}: ".format(i + 1)))
        obj.addNumber1(element)

    print("Enter elements for array 2:")
    for i in range(size):
        element = int(input("Enter element {}: ".format(i + 1)))
        obj.addNumber2(element)

    obj.compute(size)
