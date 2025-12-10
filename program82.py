import random

matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(4):
    for j in range(4):
        matrix[i][j] = random.randint(1, 100)

print("Original Matrix:")
for row in matrix:
    print(row)

print("Original Matrix:")
for row in matrix:
    print(row)

transposed_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
