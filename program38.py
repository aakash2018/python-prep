class ShowEvenNum:
    @property
    def compute(self):
        for num in range(1, 100, 2):
            print(num)


if __name__ == "__main__":
    result = ShowEvenNum()
    result.compute
