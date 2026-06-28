rows, cols = 3, 4
matrix = [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]

print("Two-Dimensional Array (Matrix):")
for row in matrix:
    print(row)

print("\nElement at row 1, col 2:", matrix[1][2])

print("\nRow-wise traversal:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end="\t")
    print()

matrix[0][0] = 99
print("\nAfter modifying matrix[0][0] to 99:")
for row in matrix:
    print(row)
