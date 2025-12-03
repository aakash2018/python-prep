num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


class GCDFactor:
    @property
    def showGcd(self):
        smaller = min(num1, num2)
        gcd = 1
        for i in range(1, smaller + 1):
            if num1 % i == 0 and num2 % i == 0:
                gcd = i

        print("GCD of", num1, "and", num2, "is:", gcd)


if __name__ == "__main__":
    result = GCDFactor()
    result.showGcd
