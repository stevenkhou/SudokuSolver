from pprint import pprint

def find_next_empty(board):
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    
    return None, None

def is_valid(board, guess, row, col):

    row_vals = board[row]
    if guess in row_vals:
        return False
    
    col_vals = [board[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for x in range(col_start, col_start + 3):
            if board[r][x] == guess:
                return False
    return True

def solve_sudoku(board):
    
    row, col = find_next_empty(board)

    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(board, guess, row, col):
            board[row][col] = guess
            if solve_sudoku(board):
                return True
        board[row][col] = 0 
    return False

if __name__ == '__main__':
    example_board = [
        [0, 0, 1,   0, 9, 0,   0, 3, 0],
        [9, 6, 3,   0, 0, 0,   0, 0, 0],
        [8, 0, 0,   7, 5, 0,   0, 0, 6],

        [0, 0, 0,   0, 7, 0,   5, 0, 0],
        [0, 0, 7,   0, 8, 5,   4, 2, 0],
        [1, 0, 4,   0, 6, 0,   0, 0, 0],

        [3, 1, 8,   6, 0, 0,   0, 5, 7],
        [0, 0, 0,   0, 0, 0,   0, 8, 4],
        [0, 9, 0,   0, 2, 0,   0, 0, 0]
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