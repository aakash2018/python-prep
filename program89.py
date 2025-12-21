matrix = []
for i in range(4):
    row = []
    for j in range(4):
        element = int(input(f"Element at pos. ({i},{j}): "))
        row.append(element)
    matrix.append(row)

is_diagonal = True
for i in range(4):
    for j in range(4):
        if i != j and matrix[i][j] != 0:
            is_diagonal = False
            break

if is_diagonal:
    print("The matrix is a diagonal matrix.")
else:
    print("The matrix is not a diagonal matrix.")
