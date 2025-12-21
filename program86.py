import random

matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]

row_sums = [0] * 4
column_sums = [0] * 4

for i in range(4):
    for j in range(4):
        row_sums[i] += matrix[i][j]
        column_sums[j] += matrix[i][j]

print("Sum of values in each row:")

for i in range(4):
    print("Row", i + 1, ":", row_sums[i])


print("Sum of values in each column:")

for j in range(4):
    print("Column", j + 1, ":", column_sums[j])
