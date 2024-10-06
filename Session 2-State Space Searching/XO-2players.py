import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")


# Global variables
player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

def btn_click(btn):
    global player

    if btn["text"] == " ":
        btn["text"] = player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            player = "O" if player == "X" else "X"

def check_winner():
    for row in buttons:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != " ":
            return True

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != " ":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != " ":
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != " ":
        return True

    return False

def is_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == " ":
                return False
    return True

def reset_game():
    global player
    player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = " "

# Create buttons and add them to the grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3,
                                  command=lambda i=i, j=j: btn_click(buttons[i][j]))
        buttons[i][j].grid(row=i, column=j)

# Start the main loop
root.mainloop()