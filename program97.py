def reverse_string(values):
    if len(values) <= 1:
        return values

    return reverse_string(values[1:]) + values[0]


print(reverse_string("321"))
