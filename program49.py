A = int(input("Enter the value of A: "))
B = int(input("Enter  the value of B: "))


class PrintNumbers:
    @property
    def showNumber(self):
        start = min(A, B)
        end = max(A, B)

        for num in range(start, end + 1):
            print(num, end=" ")

        print()


if __name__ == "__main__":
    result = PrintNumbers()
    result.showNumber
