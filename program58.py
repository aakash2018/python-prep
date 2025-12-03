import math

x = float(input("Enter the value of x: "))


class SeriesOne:
    @property
    def showSeries(self):
        sum = 1
        term = 1
        for n in range(1, 11):
            term *= x / n
            sum += term

        return {"result": math.exp(x), "sum": sum}


if __name__ == "__main__":
    res = SeriesOne()
    print("Actuak value of e^x: ", res.showSeries["result"])
    print("Actual value of e^x: ", res.showSeries["sum"])
