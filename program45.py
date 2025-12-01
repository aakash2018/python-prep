import math

number = int(input("Enter a number:"))


class isPrimeNumber:
    @property
    def checkPrime(self):
        if number < 2:
            is_prime = False
        else:
            is_prime = True

            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    is_prime = False
                    break

        if is_prime:
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number")


if __name__ == "__main__":
    result = isPrimeNumber()
    result.checkPrime
