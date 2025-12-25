def vector_sum(vector):
    if len(vector) == 0:
        return 0
    else:
        return vector[0] + vector_sum(vector[1:])


print(vector_sum([2, 4, 5, 1, 3]))
