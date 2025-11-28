class displayEvenOdd:
    @property
    def compute(self):
        num = 1
        while num <= 100:
            if num <= 50:
                print("Even:", num)
            else:
                if num % 2 != 0:
                    print("Odd:", num)
            num += 1


if __name__ == "__main__":
    result = displayEvenOdd()
    result.compute
