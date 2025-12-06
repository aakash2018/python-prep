class ascendingOrder:
    def __init__(self):
        self.arr = []
        self.is_ascending = True

    def addNumber(self, num):
        self.arr.append(num)

    def calculate(self, num):
        for i in range(1, num):
            if self.arr[i] < self.arr[i - 1]:
                self.is_ascending = False
                break

        if self.is_ascending:
            print("The array is in the ascendingOrder.")
        else:
            print("The array is not in ascendingOrder.")


if __name__ == "__main__":
    obj = ascendingOrder()
    n = int(input("Enter the size of the array: "))

    for i in range(n):
        ele = int(input("Eneter element {}:".format(i + 1)))
        obj.addNumber(ele)

    obj.calculate(n)
