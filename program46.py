import math

n = int(input("Enter a number: "))


class PrimeSeries:
    @property
    def series(self):
        for num in range(2, n):
            if n < 2:
                is_prime = False
            else:
                is_prime = True

                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0:
                        is_prime = False
                        break

                if is_prime:
                    print(num, end=" ")
        print()


if __name__ == "__main__":
    result = PrimeSeries()
    result.series
