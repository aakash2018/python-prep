from dataclasses import dataclass


@dataclass
class SumOfDiagonal:
    matrix: list

    def calculate(self):
        self.sum_diagonal = 0

        # main diagonal sum
        for i in range(3):
            self.sum_diagonal += self.matrix[i][i]

        print("Matrix:")
        for row in self.matrix:
            print(row)

        print("Sum of main diagonal values:", self.sum_diagonal)


if __name__ == "__main__":
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    print("Enter values for the 3x3 matrix:")
    for i in range(3):
        for j in range(3):
            value = int(input(f"({i},{j}): "))
            matrix[i][j] = value

    obj = SumOfDiagonal(matrix)
    obj.calculate()
