import math
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    countX, countO = 0, 0
    for i in board:
        for j in i:
            if (j == X):
                countX += 1
            elif (j == O):
                countO += 1
            else:
                pass
    if (countX == countO):
        return X
    else:
        return O


def actions(board):
    moves_list = []
    for i in range (3):
        for j in range (3):
            if (board[i][j] is EMPTY):
                moves_list.append((i, j))
    return moves_list


def result(board, action):
    local_board = []
    for row in board:
        local_board.append(row.copy())
    player_name = player(local_board)
    i, j = action[0], action[1]
    local_board[i][j] = player_name
    return local_board


def winner(board):
    win_cases = [
        [(i, i) for i in range (3)], 
        [(i, 2-i) for i in range (3)],
        [(i, 0) for i in range (3)],
        [(i, 1) for i in range (3)],
        [(i, 2) for i in range (3)],
        [(0, j) for j in range (3)],
        [(1, j) for j in range (3)],
        [(2, j) for j in range (3)]
    ]
    Xmoved, Omoved = [], []
    for i in range (3):
        for j in range (3):
            if (board[i][j] == X):
                Xmoved.append((i, j))
            elif (board[i][j] == O):
                Omoved.append((i, j))
            else:
                pass
    for i in win_cases:
        if ((i[0] in Xmoved) and (i[1] in Xmoved) and (i[2] in Xmoved)):
            return X
        elif ((i[0] in Omoved) and (i[1] in Omoved) and (i[2] in Omoved)):
            return O
    else:
        return None

def terminal(board):
    empty_count = 0
    for i in board:
        for j in i:
            if (j is EMPTY):
                empty_count += 1
    if (empty_count == 0):
        return True
    elif (winner(board) is not None):
        return True
    else:
        return False


def utility(board):
    winner_name = winner(board)
    if (winner_name is not None):
        if (winner_name == X):
            return 1
        elif (winner_name == O):
            return -1
        else:
            return 0
    else:
        return 0


def minimax(board):
    local_board = board
    player_name = player(local_board)

    if (player_name == X):
        result_list = []
        result_dict = {}
        for action in actions(local_board):
            new_board = result(local_board, action)
            best_value = best_val(new_board)
            result_dict[action] = best_value
        max_value = max(list(result_dict.values()))
        for move in result_dict:
            if (result_dict[move] == max_value):
                result_list.append(move)
        do_move = random.choice(result_list)
        return do_move
        
    elif (player_name == O):
        result_list = []
        result_dict = {}
        for action in actions(local_board):
            new_board = result(local_board, action)
            best_value = best_val(new_board)
            result_dict[action] = best_value
        min_value = min(list(result_dict.values()))
        for move in result_dict:
            if (result_dict[move] == min_value):
                result_list.append(move)
        do_move = random.choice(result_list)
        return do_move
                

def best_val(board):
    local_board = board
    player_name = player(local_board)

    if (terminal(local_board)):
        return utility(local_board)

    if (player_name == X):
        best_value = -math.inf
        for action in actions(local_board):
            new_board = result(local_board, action)
            value = best_val(new_board)
            best_value = max(best_value, value)
        return best_value
        
    elif (player_name == O):
        best_value = math.inf
        for action in actions(local_board):
            new_board = result(local_board, action)
            value = best_val(new_board)
            best_value = min(best_value, value)
        return best_value