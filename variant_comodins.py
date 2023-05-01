"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Headers for functions in abstract board for simple tic-tac-toe-like games, 2021.
Intended for Grau en Intel-ligencia Artificial, Programacio i Algorismes 1.
I would prefer to do everything in terms of object-oriented programming though.
"""
# Import: 
# color GRAY; PLAYER_COLOR, NO_PLAYER
# board dimension BSIZ
from constants import PLAYER_COLOR, BSIZ, NO_PLAYER, GRAY

# Data structure for stones
from collections import namedtuple
import random

Stone = namedtuple('Stone', ('x', 'y', 'color'))


def set_board_up(stones_per_player=((BSIZ ** 2) - 1) // 2):
    # current_player = random.randint(0, 1)
    current_player = 0

    def board():
        a = []
        for i in range(BSIZ):
            b = []
            for j in range(BSIZ):
                b.append(NO_PLAYER)
            a.append(b)
        return a

    board = board()

    stone = Stone(NO_PLAYER, NO_PLAYER, GRAY)

    stones_played = []


    def stones():

        return stones_played

    def select_st(i, j):
        nonlocal stone
        nonlocal current_player


        if (0 > i or i >= BSIZ) or (0 > j or j >= BSIZ):
            return False

        if board[i][j] == current_player:
            for p in stones_played:
                if p.x == i and p.y == j:
                    stone = p 
                    return True
        return False

    def end():
    
        for j in range(BSIZ):
            result_col = True
            for i in range(BSIZ - 1):
                if board[i][j] != board[i + 1][j] or board[i][j] == NO_PLAYER:
                    result_col = False
            if result_col is True:
                return True

                # check row
        for i in range(BSIZ):
            result_row = True
            for j in range(BSIZ - 1):
                if board[i][j] != board[i][j + 1] or board[i][j] == NO_PLAYER:
                    result_row = False
            if result_row is True:
                return True

        result_diag1 = True
        for k in range(BSIZ - 1):
            if board[k][k] != board[k + 1][k + 1] or board[k][k] == NO_PLAYER:
                result_diag1 = False

        result_diag2 = True
        for k in range(BSIZ - 1):
            if board[k][BSIZ - 1 - k] != board[k + 1][BSIZ - 2 - k] or board[k][BSIZ - 1 - k] == NO_PLAYER:
                result_diag2 = False

        return (result_diag1 is True) or (result_diag2 is True)

    def move_st(i, j):
        nonlocal current_player
        nonlocal stone
        if (0 > i or i >= BSIZ) or (0 > j or j >= BSIZ):
            return True, current_player, False

        if board[i][j] == NO_PLAYER:
            if stone.x != -1:
                "canviem el tauler i treiem la pedra seleccionada"
                board[stone.x][stone.y] = NO_PLAYER
                stones_played.remove(stone)

            "canviem el tauler i afegim la nova pedra"
            board[i][j] = 1-current_player
            #hem modificat aquí 
            stone = Stone(i, j, PLAYER_COLOR[current_player])
            stones_played.append(stone)
            current_player = 1 - current_player
            "reiniciem stone per la comparació: if stone.x != -1:" \
            " ja que si no entra al select_st, stone no canviarà i per tant no eliminarà res, ja que encara no hi hauran 8 stones"
            stone = Stone(NO_PLAYER, NO_PLAYER, GRAY)

            return len(stones_played) != 2 * stones_per_player, current_player, end()

        else:
            return True, current_player, False

    def draw_txt(end=False):
        'Use ASCII characters to draw the board.'
        for i in range(BSIZ):
            for j in range(BSIZ):
                if j != (BSIZ - 1):
                    print('|', "X" if board[i][j] == 1 else "0" if board[i][j] == 0 else " ", '|', end='')
                else:
                    print('|', "X" if board[i][j] == 1 else "0" if board[i][j] == 0 else " ", '|', end='\n')

            print('-' * (6 * BSIZ))

    # return these 3 functions to make them available to the main program
    return stones, select_st, move_st, draw_txt
