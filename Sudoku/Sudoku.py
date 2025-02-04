from copy import deepcopy


def check_row(row):
    count = [0] * 9
    for i in range(9):
        count_index = row[i] - 1
        if count_index == -1:
            continue
        if count[count_index] > 0:
            return False
        else:
            count[count_index] += 1
    return True

def check_column(column_index,grid):
    count = [0] * 9
    for i in range(9):
        count_index = grid[i][column_index] - 1
        if count_index == -1:
            continue
        if count[count_index] > 0:
            return False
        else:
            count[count_index] += 1
    return True

def check_subgrid(row_index,column_index,grid):
    a = row_index//3
    b = column_index//3
    subgrid_elements = []
    for i in range((a*3),(a*3)+3):
        for j in range((b*3),(b*3)+3):
            subgrid_elements += [grid[i][j]]
    count = [0] * 9
    for i in range(9):
        count_index = subgrid_elements[i] - 1
        if count_index == -1:
            continue
        if count[count_index] > 0:
            return False
        else:
            count[count_index] += 1
    return True
    
def backtrack(row_index,column_index,stack,grid):
    grid[row_index][column_index] = 0
    backtrack_pos = stack.pop()
    row_index = backtrack_pos[0]
    column_index = backtrack_pos[1]
    if grid[row_index][column_index] == 9:
        return backtrack(row_index,column_index,stack,grid)
    else:
        grid[row_index][column_index] += 1
        return row_index, column_index
    
def sudoku_solver(grid):
    row_index = 0
    column_index = 0
    stack = []
    while row_index < 9:
        if grid[row_index][column_index] != 0:
            column_index += 1
            if column_index == 9:
                column_index = 0 
                row_index += 1
        else:
            grid[row_index][column_index] += 1
            while check_row(grid[row_index]) == False or check_column(column_index,grid) == False or check_subgrid(row_index,column_index,grid) == False:
                if grid[row_index][column_index] == 9:
                    row_index,column_index = backtrack(row_index,column_index,stack,grid)
                else:
                    grid[row_index][column_index] += 1
            stack.append([row_index,column_index])
            column_index += 1
            if column_index == 9:
                column_index = 0 
                row_index += 1
    return grid

def modified_solver(grid):
    row_index = 0
    column_index = 0
    stack = []
    progress = []
    while row_index < 9:
        if grid[row_index][column_index] != 0:
            column_index += 1
            if column_index == 9:
                column_index = 0 
                row_index += 1
        else:
            grid[row_index][column_index] += 1
            progress += [(row_index,column_index,grid[row_index][column_index])]
            while check_row(grid[row_index]) == False or check_column(column_index,grid) == False or check_subgrid(row_index,column_index,grid) == False:
                if grid[row_index][column_index] == 9:
                    row_index,column_index = backtrack(row_index,column_index,stack,grid)
                else:
                    grid[row_index][column_index] += 1
                    progress += [(row_index,column_index,grid[row_index][column_index])]
            stack.append([row_index,column_index])
            column_index += 1
            if column_index == 9:
                column_index = 0 
                row_index += 1
    return progress

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

print(sudoku_solver(board))