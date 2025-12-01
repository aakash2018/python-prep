class SumOfEven:
    @property
    def compute(self):
        sum_of_evens = 0
        num = 2
        for i in range(1, 100, num):
            sum_of_evens += i

        print("The sum of even numbers from 1 to 100 is:", sum_of_evens)


if __name__ == "__main__":
    result = SumOfEven()
    result.compute
