def row_major_index(row, col, num_cols):
    return row * num_cols + col

def store_row_major(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    flat = []
    for i in range(rows):
        for j in range(cols):
            flat.append(matrix[i][j])
    return flat

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

flat = store_row_major(matrix)
print("\nRow-Major Order (1D representation):", flat)

r, c = 1, 2
idx = row_major_index(r, c, len(matrix[0]))
print(f"\nIndex of element at row={r}, col={c} in row-major: {idx}")
print(f"Element at that index: {flat[idx]}")
