num = int(input("Enter a number: "))


class fibonacciSeries:
    @property
    def showSeries(self):
        a, b = 0, 1
        print("Fibonacci sequence:")
        while a <= num:
            print(a, end=" ")
            a, b = b, a + b


if __name__ == "__main__":
    result = fibonacciSeries()
    result.showSeries
