def collatxz_sequence(number):
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        sequence.append(number)
    return sequence


print(collatxz_sequence(5))
