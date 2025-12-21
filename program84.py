matrix = [[0] * 5 for _ in range(5)]

print(matrix)
print("Enter the elements of the matrix:")
for i in range(5):
    for j in range(5):
        matrix[i][j] = int(input(f"Enter element at position ({i+1}, {j+1}):"))

max_value = matrix[0][0]
max_position = (0, 0)

max_value = matrix[0][0]
max_position = (0, 0)

for i in range(5):
    for j in range(5):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_position = (i, j)

print(f"\nLargest value: {max_value}")
print(f"Position:({max_position[0]+1},{max_position[1]+1})")
