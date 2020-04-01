
def create_board(size):
    """Function to create board"""
    board = []
    for idx in range(size):
        board.append(['-' for _ in range(size)])
        # board.append('{} {}'.format(size - idx - 1, '  -' * size))
    # board.append('     ' + '     '.join([str(idx_el) for idx_el in range(size)]))
    return board


def print_board(board):
    """Function to print player board"""
    for line in board:
        print(line)


def set_start_point(board):
    """Function to set start point"""
    board[len(board[0]) - 1][0] = 'x'
    return len(board[0]) - 1, 0, 'N'


def set_point(board, points):
    idx, idy, current_direction = points
    """Function set current point in board"""
    board[idx][idy] = 'x'
    return idx, idy, current_direction


def move(board, points, string_move, directions):
    idx, idy, current_direction = points
    board[idx][idy] = '-'
    moves = [m for m in string_move]
    for move_player in moves:
        if move_player in ['L', 'R']:
            current_direction = check_direction(move_player, current_direction, directions)
        else:
            idx, idy = move_forward(len(board), idx, idy, current_direction)
    return idx, idy, current_direction


def move_forward(size, idx, idy, current_direction):
    """Function check index next move"""
    if current_direction == 'N':
        idx -= 1
        if idx < 0:
            idx = 0
    if current_direction == 'S':
        idx += 1
        if idx > size - 1:
            idx = size - 1
    if current_direction == 'E':
        idy += 1
        if idy >= size - 1:
            idy = size - 1
    if current_direction == 'W':
        idy -= 1
        if idy < 0:
            idy = 0
    return idx, idy


def check_direction(move_player, current_direction, directions):
    """Function check next direction"""
    if move_player == 'R':
        id_direction = directions.index(current_direction)
        if id_direction == len(directions) - 1:
            current_direction = directions[0]
        else:
            current_direction = directions[id_direction + 1]
    if move_player == 'L':
        id_direction = directions.index(current_direction)
        if id_direction == 0:
            current_direction = directions[-1]
        else:
            current_direction = directions[id_direction - 1]
    return current_direction


def check_win(board):
    """function checks if you won"""
    return board[0][len(board)-1] == 'x'

def main():
    """Main game function"""
    directions = ['N', 'E', 'S', 'W']
    board = create_board(4)
    points = set_start_point(board)
    while True:
        print_board(board)
        string_move = input('Insert string: ')
        idx, idy, current_direction = move(board, points, string_move, directions)
        points = idx, idy, current_direction
        set_point(board, points)
        if check_win(board):
            print('You win!')
            break
        print(f'current_direction {current_direction}')


if __name__ == '__main__':
    main()

