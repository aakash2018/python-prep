rows_a = int(input("Enter the number of rows of matrix A: "))
cols_a = int(input("Enter the number of columns of matrix A: "))

rows_b = int(input("Enter the number of rows of matrix B: "))
cols_b = int(input("Enter the number of columns of matrix B: "))

if cols_a != rows_b:
    print("Matrix multiplication is not possible.")
else:
    print("Enter the elements of matrix A:")
    matrix_a = []
    for _ in range(rows_a):
        row = []
        for _ in range(cols_a):
            element = int(input())
            row.append(element)
        matrix_a.append(row)

    print("Enter the elements of matrix B:")
    matrix_b = []
    for _ in range(rows_b):
        row = []
        for _ in range(cols_b):
            element = int(input())
            row.append(element)
        matrix_b.append(row)

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    print("The result of the multiplication of matrix A and B is:")
    for row in result:
        print(row)
