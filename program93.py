def checkPrime(n, divisor=2):
    if n <= 1:
        return false
    elif n == 2:
        return True
    elif n % divisor == 0:
        return False
    elif divisor * divisor > n:
        return True
    else:
        return checkPrime(n, divisor + 1)


print(checkPrime(5))
