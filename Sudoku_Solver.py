def display(sudoku):
    print("Solved sudoku:")
    for rows in sudoku:
        print(*rows)

def find(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return None

def check_validity(sudoku, n, pos):
    row, col = pos
    for i in range(9):
        if sudoku[row][i] == n and i != col:
            return False
    for j in range(9):
        if sudoku[j][col] == n and j != row:
            return False
    x = col // 3
    y = row // 3
    for i in range(y * 3, (y * 3) + 3):
        for j in range(x * 3, (x * 3) + 3):
            if sudoku[i][j] == n and (i , j) != pos:
                return False
    return True

def solve(sudoku):
    f = find(sudoku)
    if not f:
        return True
    
    row, col = f
    for i in range(1, 10):
        if check_validity(sudoku, i, (row, col)):
            sudoku[row][col] = i
            if solve(sudoku):
                return True
            sudoku[row][col] = 0
    return False


def main():
    print("Enter sudoku:")
    sudoku = []
    for i in range(9):
        row = list(map(int, input().split()))
        sudoku.append(row)
    if solve(sudoku):
        display(sudoku)
    else:
        print("No solution")
main()