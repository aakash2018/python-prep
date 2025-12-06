class evenOddArray:
    def __init__(self):
        self.arr = []
        self.all_even = True

    def addNumber(self, num):
        self.arr.append(num)

    def compute(self, size):
        for elment in self.arr:
            if elment % 2 != 0:
                self.all_even = False
                break

        if self.all_even:
            print("All elements are even.")
        else:
            print("Not all elements are even.")


if __name__ == "__main__":
    obj = evenOddArray()
    size = int(input("Enter the size of the arrays: "))

    print("Enter elements for array 1:")
    for i in range(size):
        element = int(input("Enter element {}: ".format(i + 1)))
        obj.addNumber(element)

    obj.compute(size)
