class displayNumber:
    @property
    def compute(self):
        for num in range(1, 101):
            print(num)


if __name__ == "__main__":
    result = displayNumber()
    result.compute
