from time import sleep
import tkinter as tk
from tkinter import Button, messagebox
from Sudoku import sudoku_solver, modified_solver
from copy import deepcopy

class SudokuUI(tk.Tk):
    def __init__(self, board):
        super().__init__()

        self.board = board
        self.selected_cell = None

        self.solution = sudoku_solver(deepcopy(board))
        self.solution_steps = modified_solver(deepcopy(board))

        self.title("Sudoku Solver")
        self.geometry("450x550")

        self.canvas = tk.Canvas(self, width=450, height=450)
        self.canvas.pack()

        self.solve_button = Button(self, text='Solve', command=self.solve_board)
        self.solve_button.pack(pady=10)

        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.bind("<Key>", self.key_pressed)

        self.draw_grid()
        self.draw_numbers()

    def draw_grid(self):
        for i in range(10):
            width = 2 if i % 3 == 0 else 1
            self.canvas.create_line(i * 50, 0, i * 50, 450, width=width)
            self.canvas.create_line(0, i * 50, 450, i * 50, width=width)

    def draw_numbers(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    x = j * 50 + 25
                    y = i * 50 + 25
                    self.canvas.create_text(x, y, text=self.board[i][j], tags="numbers", font=("Arial", 18))

    def cell_clicked(self, event):
        x, y = event.x, event.y
        col, row = x // 50, y // 50

        if self.selected_cell:
            self.canvas.delete(self.selected_cell)

        self.selected_cell = self.canvas.create_rectangle(col * 50, row * 50, (col + 1) * 50, (row + 1) * 50, outline="red", width=2)

    def key_pressed(self, event):
        if self.selected_cell and event.char.isdigit() and event.char != '0':
            x1, y1, x2, y2 = self.canvas.coords(self.selected_cell)
            col, row = int(x1 // 50), int(y1 // 50)
            self.board[row][col] = int(event.char)
            if self.solution[row][col] == int(event.char):
                self.board[row][col] = int(event.char)
                self.draw_numbers()
            else:
                messagebox.showerror("Error", "Not Valid")
        
    def solve_board(self):
        for solution in self.solution_steps:
            self.board[solution[0]][solution[1]] = solution[2]
            self.draw_numbers()
            self.update()  # Update the canvas after each move
            sleep(0.001)  # Add a small delay to visualize the solving process

def display_sudoku(board):
    app = SudokuUI(board)
    app.mainloop()

# Example Sudoku board with some cells filled
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

display_sudoku(board)

