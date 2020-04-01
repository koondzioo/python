# północ (N), południe (S), wschód (E), zachód (W).
kierunki = ['N', 'E', 'S', 'W']
ruchy = {'M': 1,
         'R': 1,
         'L': -1}


def create_board(size):
    board = []
    for idx in range(size):
        board.append(['-' for _ in range(size)])
        # board.append('{} {}'.format(size - idx - 1, '  -' * size))
    # board.append('     ' + '     '.join([str(idx_el) for idx_el in range(size)]))
    return board


def print_board(board):
    for line in board:
        print(line)


def set_start_point(board):
    board[len(board[0]) - 1][0] = 'x'
    return board


def set_point(board, idx, idy):
    board[idx][idy] = 'x'
    return board


def move(board, points, string_move):
    idx, idy, kierunek = points
    board[idx][idy] = '-'
    global kierunki, ruchy
    moves = [m for m in string_move]
    for move_player in moves:
        if kierunek == 'N' and move_player == 'M':
            idx -= 1
        if move_player == 'R':
            idx_kierunki = kierunki.index(kierunek)
            kierunek = kierunki[idx_kierunki+1]
            print(kierunek)
    return idx, idy



if __name__ == '__main__':
    board = create_board(4)
    set_start_point(board)
    print_board(board)
    print('-----------')
    points = 3, 0, kierunki[0]
    idx, idy = move(board, points, 'MMRR')
    set_point(board, idx, idy)
    print_board(board)

    # board = create_board(4)
    # set_start_point(board)
    # print_board(board)
