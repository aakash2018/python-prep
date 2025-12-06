class addTwoVector:
    def __init__(self):
        self.vector1 = []
        self.vector2 = []
        self.result_vector = []

    def addVector1(self, num):
        self.vector1.append(num)

    def addVector2(self, num):
        self.vector2.append(num)

    def calculateVector(self, n):
        for i in range(n):
            self.sum_element = self.vector1[i] + self.vector2[i]
            self.result_vector.append(self.sum_element)

    @property
    def compute(self):
        print("Resulting vector (sum of corresponding elements): ", self.result_vector)


if __name__ == "__main__":
    obj = addTwoVector()

    n = int(input("Enter the size of the vectors: "))

    print("Enter  elements of vector1:")

    for i in range(n):
        ele = int(input("Enter element{}:".format(i + 1)))
        obj.addVector1((ele))

    print("Enter  elements of vector2:")

    for i in range(n):
        ele = int(input("Enter element{}:".format(i + 1)))
        obj.addVector2((ele))

    obj.calculateVector(n)

    obj.compute
