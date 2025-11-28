class Increment:
    @property
    def compute(self) -> int:
        i = 1
        while i <= 10:
            print(i)
            i = i + 1


if __name__ == "__main__":
    result = Increment()
    result.compute
