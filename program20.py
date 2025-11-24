num = int(input("Enter the number "))


class isEvenOdd:
    def __init__(self, num):
        self.num = num

    def isCheck(self):
        if self.num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")


result = isEvenOdd(num)
result.isCheck()
