import math

n = int(input("Enter  the value of N: "))


class FirstNPrime:
    @property
    def isPrime(self):
        count = 0
        num = 2
        while count < n:
            is_prime = True

            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(num, end=" ")
                count += 1

            num += 1

        print()


if __name__ == "__main__":
    result = FirstNPrime()
    result.isPrime
