class AverageNumber:
    @property
    def showAverage(self):
        total = 0
        count = 0
        while True:
            number = int(input("Enter a number (enter 0 to stop): "))

            if number == 0:
                break

            total += number
            count += 1

        if count > 0:
            average = total / count
            print("Average:", average)
        else:
            print("No numbers were entered.")


if __name__ == "__main__":
    result = AverageNumber()
    result.showAverage
