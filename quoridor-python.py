# Initialisation du plateau de jeu
def init_board():
    board_size = 9
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    players = {'A': (0, board_size // 2), 'B': (board_size - 1, board_size // 2)}
    board[players['A'][0]][players['A'][1]] = 'A'
    board[players['B'][0]][players['B'][1]] = 'B'
    return board, players

# Affichage du plateau de jeu
def print_board(board):
    for row in board:
        print('+---' * len(board) + '+')
        print('| ' + ' | '.join(row) + ' |')
    print('+---' * len(board) + '+')

Tiago et Gabriel n'oubliez pas d'expliquer le code.
