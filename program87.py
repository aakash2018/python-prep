matrix = []

for _ in range(3):
    row = []
    for _ in range(3):
        element = int(input("Enter an element: "))
        row.append(element)
    matrix.append(row)
det = (
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
    - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
    + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
)

print("Deterninant:", det)
