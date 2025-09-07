import time
import random
import os
import msvcrt

height = 25
width = 10

high_score = 0

pieces = [
    [[True]],

    [[True], [True]],

    [[True, True, True]],

    [[True], [True], [True]],

    [[False, True, False],
     [True, True, True]],

    [[True, True, True],
     [False, True, False]],

    [[True, False],
     [True, True],
     [True, False]],

    [[False, True],
     [True, True],
     [False, True]],

    [[True, False],
     [True, False],
     [True, True]],

    [[False, True],
     [False, True],
     [True, True]],

    [[True, True],
     [False, True],
     [False, True]],

    [[True, True],
     [True, False],
     [True, False]],

    [[True, True],
     [True, True]],

    [[True, True, True],
     [True, True, True],
     [True, True, True]]
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(score, next_shape):
    print(f"Score: {score}\n")
    print("Next:")
    for i in range(3):  # Always reserve 3 rows
        line = ''
        if i < len(next_shape):
            row = next_shape[i]
            for cell in row:
                line += '[ ]' if cell else '   '
            line += '   ' * (3 - len(row))
        else:
            line = '   ' * 3
        print(line)
    print("\n")

def print_board(board):
    print("+" + "-" * width * 3 + "+")
    for row in board:
        line = "|"
        for cell in row:
            if cell == "Filled":
                line += '[ ]'
            else:
                line += '   '
        line += "|"
        print(line)
    print("+" + "-" * width * 3 + "+")

def can_place(board, shape, start_row, start_col):
    shape_height = len(shape)
    shape_width = len(shape[0])
    for i in range(shape_height):
        for j in range(shape_width):
            if shape[i][j]:
                r = start_row + i
                c = start_col + j
                if r >= len(board) or c < 0 or c >= len(board[0]):
                    return False
                if board[r][c] != "Empty":
                    return False
    return True

def place_piece(board, shape, start_row, start_col):
    shape_height = len(shape)
    shape_width = len(shape[0])
    for i in range(shape_height):
        for j in range(shape_width):
            if shape[i][j]:
                r = start_row + i
                c = start_col + j
                board[r][c] = "Filled"

def rotate_shape(shape):
    rows = len(shape)
    cols = len(shape[0])
    new_shape = []
    for col in range(cols):
        new_row = []
        for row in range(rows - 1, -1, -1):
            new_row.append(shape[row][col])
        new_shape.append(new_row)
    return new_shape

def drop_piece(board, shape, total_score, next_shape):
    shape_height = len(shape)
    shape_width = len(shape[0])
    max_start_col = width - shape_width
    col = random.randint(0, max_start_col)
    piece_row = 0
    fast_drop = False

    while True:
        if not can_place(board, shape, piece_row + 1, col) or piece_row + 1 >= height:
            place_piece(board, shape, piece_row, col)
            total_score += 1  # +1 for successful placement
            break

        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'a': 
                if col > 0 and can_place(board, shape, piece_row, col - 1):
                    col -= 1
            elif key == b'd': 
                if col < width - shape_width and can_place(board, shape, piece_row, col + 1):
                    col += 1
            elif key == b'w':  # Rotate
                new_shape = rotate_shape(shape)
                new_width = len(new_shape[0])
                new_height = len(new_shape)
                if col + new_width > width:
                    col = width - new_width
                if can_place(board, new_shape, piece_row, col):
                    shape = new_shape
            elif key == b's':  # Fast drop
                fast_drop = True
            elif key == b' ':  # Pause
                clear_screen()
                print_header(total_score, next_shape)
                print_board(board)
                print("\nGame Paused. Press any key to continue...")
                msvcrt.getch()

        piece_row += 1
        temp_board = [row.copy() for row in board]
        place_piece(temp_board, shape, piece_row, col)
        clear_screen()
        print_header(total_score, next_shape)
        print_board(temp_board)

        if fast_drop:
            time.sleep(0.05)
        else:
            time.sleep(0.2)

    board, gained_score = check_filled_rows(board, total_score, next_shape)
    total_score += gained_score * 10
    return board, total_score

def check_filled_rows(board, total_score, next_shape):
    rows_to_clear = []

    for index, row in enumerate(board):
        if all(cell == "Filled" for cell in row):
            rows_to_clear.append(index)

    if not rows_to_clear:
        return board, 0  

    for row_index in rows_to_clear:
        for _ in range(2): 
            temp_board = [r.copy() for r in board]
            temp_board[row_index] = ["Empty"] * width
            clear_screen()
            print_header(total_score, next_shape)
            print_board(temp_board)
            time.sleep(0.3)

            temp_board = [r.copy() for r in board]
            clear_screen()
            print_header(total_score, next_shape) 
            print_board(temp_board)
            time.sleep(0.3)

    for row_index in sorted(rows_to_clear):
        for col in range(width):
            for r in range(row_index, 0, -1):
                board[r][col] = board[r - 1][col]
            board[0][col] = "Empty"

    return board, len(rows_to_clear)


def game():
    global high_score
    while True:
        board = [["Empty" for _ in range(width)] for _ in range(height)]
        total_score = 0
        shape = random.choice(pieces)
        next_shape = random.choice(pieces)
        game_over = False

        while not game_over:
            max_start_col = width - len(shape[0])
            col = random.randint(0, max_start_col)
            if not can_place(board, shape, 0, col):
                game_over = True
                break

            board, total_score = drop_piece(board, shape, total_score, next_shape)
            shape = next_shape
            next_shape = random.choice(pieces)

        if total_score > high_score:
            high_score = total_score
        clear_screen()
        print_header(total_score, next_shape)
        print_board(board)
        print(f"\nGame Over! Final Score: {total_score}")
        print(f"High Score: {high_score}")
        print("Press any key to play again...")
        msvcrt.getch()

if __name__ == "__main__":
    game()
