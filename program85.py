matrix = []

print("Enter the values of the 3X# matrix:")

for _ in range(3):
    row = []
    for _ in range(3):
        value = int(input("Enter a value: "))
        row.append(value)
    matrix.append(row)

sum_even = 0
count_even = 0

for i in range(3):
    for j in range(3):
        if (i + j) % 2 == 0:
            sum_even += matrix[i][j]
            count_even += 1

average_even = sum_even / count_even

print("Average of values at even positions:", average_even)
