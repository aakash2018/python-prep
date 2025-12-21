m = int(input("enter the number of rows: "))
n = int(input("enter the number of columns: "))

minefield = []

# input minefield
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Element at position ({i},{j}): "))
        row.append(element)
    minefield.append(row)

# initialize neighboring_mines with zeros
neighboring_mines = [[0 for _ in range(n)] for _ in range(m)]

# calculate neighboring mines
for i in range(m):
    for j in range(n):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # skip the cell itself
                if dx == 0 and dy == 0:
                    continue

                new_i = i + dx
                new_j = j + dy

                if 0 <= new_i < m and 0 <= new_j < n:
                    neighboring_mines[i][j] += minefield[new_i][new_j]

print("Minefield:")
for row in minefield:
    print(row)

print("\nNeighboring mines count:")
for row in neighboring_mines:
    print(row)
