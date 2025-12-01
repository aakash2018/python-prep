n = int(input("enter the value of  N: "))


class PerfectSquare:
    @property
    def showSquare(self):
        count = 0
        num = 1

        while count < n:
            square = num**2

            print(square, end=" ")
            count += 1

            num += 1

        print()


if __name__ == "__main__":
    result = PerfectSquare()
    result.showSquare
