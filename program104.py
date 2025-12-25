def check_tic_tac_toe(matrix):
    for row in matrix:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] and matrix[0][col] != " ":
            return matrix[0][col]

    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != " ":
        return matrix[0][0]

    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != " ":
        return matrix[0][2]

    for row in matrix:
        if " " in row:
            return "Game not over yet"

    return "Tie"


print(check_tic_tac_toe([[0, 1, 1], [1, 0, 0], [0, 0, 1]]))
