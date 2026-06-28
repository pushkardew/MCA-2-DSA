def column_major_index(row, col, num_rows):
    return col * num_rows + row

def store_column_major(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    flat = []
    for j in range(cols):
        for i in range(rows):
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

flat = store_column_major(matrix)
print("\nColumn-Major Order (1D representation):", flat)

r, c = 1, 2
idx = column_major_index(r, c, len(matrix))
print(f"\nIndex of element at row={r}, col={c} in column-major: {idx}")
print(f"Element at that index: {flat[idx]}")
