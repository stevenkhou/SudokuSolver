from pprint import pprint

def find_next_empty(board):
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    
    return None, None

def is_valid(board, guess, row, col):

    for i in range(9):
        if board[row][i] == guess or board[i][col] == guess:
            return False
    
    row_start, col_start = (row // 3) * 3, (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for x in range(col_start, col_start + 3):
            if board[r][x] == guess:
                return False
    
    return True

def solve_sudoku(board):
    
    empty_cell = find_next_empty(board)
    
    if empty_cell[0] is None:
        return True

    row, col = empty_cell
    for guess in range(1, 10):
        if is_valid(board, guess, row, col):
            board[row][col] = guess
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False

if __name__ == '__main__':
    example_board = [
        [9, 0, 0,   6, 0, 0,   3, 0, 0],
        [0, 5, 0,   8, 3, 0,   4, 0, 9],
        [0, 0, 0,   0, 0, 0,   2, 0, 7],

        [7, 0, 0,   0, 0, 6,   0, 0, 0],
        [8, 3, 0,   1, 0, 0,   0, 0, 6],
        [1, 0, 6,   0, 0, 4,   5, 7, 0],

        [0, 0, 0,   9, 0, 0,   0, 3, 4],
        [0, 7, 8,   4, 0, 0,   6, 0, 0],
        [0, 2, 0,   0, 0, 0,   0, 1, 0]
    ]
    print("Original Sudoku Board:")
    pprint(example_board)

    if solve_sudoku(example_board):
        print("\nSolved Sudoku Board:")
        pprint(example_board)
    else:
        print("Solution DNE")

#Empty board:
"""
[0, 0, 0,   0, 0, 0,   0, 0, 0],
[0, 0, 0,   0, 0, 0,   0, 0, 0],
[0, 0, 0,   0, 0, 0,   0, 0, 0],

[0, 0, 0,   0, 0, 0,   0, 0, 0],
[0, 0, 0,   0, 0, 0,   0, 0, 0],
[0, 0, 0,   0, 0, 0,   0, 0, 0],

[0, 0, 0,   0, 0, 0,   0, 0, 0],
[0, 0, 0,   0, 0, 0,   0, 0, 0],
[0, 0, 0,   0, 0, 0,   0, 0, 0]
"""