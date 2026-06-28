def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n, solutions)
            board[row] = -1

def print_board(solution, n):
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if solution[row] == col else ". "
        print(line)
    print()

n = 4
board = [-1] * n
solutions = []
solve_n_queens(board, 0, n, solutions)

print(f"N-Queen Problem (N={n})")
print(f"Total Solutions: {len(solutions)}\n")
for idx, sol in enumerate(solutions):
    print(f"Solution {idx + 1}:")
    print_board(sol, n)
