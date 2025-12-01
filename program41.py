class nestedMultiplicands:
    @property
    def multi(self):
        for i in range(1, 11):
            for j in range(1, 11):
                product = i * j
                print(i, "x", j, "=", product)

        print("-" * 20)


if __name__ == "__main__":
    result = nestedMultiplicands()
    result.multi
