matrix1 = [[0, 0], [0, 0]]
matrix2 = [[0, 0], [0, 0]]
sum_matrix = [[0, 0], [0, 0]]

print("Enter the elements of the first matrix:")
for i in range(2):
    for j in range(2):
        matrix1[i][j] = int(input(f"Enter element at position ({i+1},{j+1}): "))

print("\n Enter the elements of the second matrix:")
for i in range(2):
    for j in range(2):
        matrix2[i][j] = int(input(f"Enter element at position ({i+1},{j+1}): "))

for i in range(2):
    for j in range(2):
        sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

print("\n sum of the two matrices:")
for row in sum_matrix:
    print(row)
