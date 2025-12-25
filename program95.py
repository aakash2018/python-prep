def powerbase(base, exponent):
    if exponent == 0:
        return 1

    return base * powerbase(base, exponent - 1)


print(powerbase(2, 4))
