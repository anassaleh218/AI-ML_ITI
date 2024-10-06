# Task 2 - Alpha Beta with GUI
from math import inf as infinity
from random import choice
import time
import tkinter as tk
from tkinter import messagebox

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# Initialize the main window
root = tk.Tk()
root.title("Task 2 - Alpha Beta GUI")
buttons = [[None for _ in range(3)] for _ in range(3)]


def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0
    return score


def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    return [player, player, player] in win_state


def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP) or len(empty_cells(state)) == 0


def empty_cells(state):
    cells = [[i, j] for i, row in enumerate(state)
             for j, cell in enumerate(row) if cell == 0]
    return cells


def valid_move(x, y):
    return [x, y] in empty_cells(board)


def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        buttons[x][y]["text"] = "X" if player == HUMAN else "O"
        buttons[x][y]["state"] = "disabled"
        return True
    return False


def minimax(state, depth, player, alpha, beta):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """

    if player == COMP:  # Maximizing player (Computer)
        best = [-1, -1, -infinity]
    else:  # Minimizing player (Human)
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):  # Leaf node
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player, alpha, beta)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score
            alpha = max(alpha, score[2])
        else:
            if score[2] < best[2]:
                best = score
            beta = min(beta, score[2])

        # Alpha-beta pruning
        if beta <= alpha:
            break

    return best


def ai_turn():
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP, -infinity, +infinity)
        x, y = move[0], move[1]

    set_move(x, y, COMP)

    if wins(board, COMP):
        messagebox.showinfo("Tic Tac Toe", "You Lose!")
        reset_game()
    elif len(empty_cells(board)) == 0:
        messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
        reset_game()



def human_turn(x, y):
    if set_move(x, y, HUMAN):
        if not game_over(board):
            ai_turn()
        else:
            if wins(board, HUMAN):
                messagebox.showinfo("Tic Tac Toe", "You Win!")
            elif len(empty_cells(board)) == 0:
                messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
            reset_game()


def reset_game():
    global board
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "normal"


for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", width=13, height=3,
                                  command=lambda i=i, j=j: human_turn(i, j))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
