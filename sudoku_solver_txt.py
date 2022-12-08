# function to print the grid
def print_grid(grid):
  for i in range(9):
    for j in range(9):
      print(grid[i][j], end=" ")
    print()

# function to find the next empty cell in the grid
def find_next_empty_cell(grid):
  for i in range(9):
    for j in range(9):
      if grid[i][j] == 0:
        return (i, j)
  return None

# function to check if the given number is valid in the given cell
def is_valid(grid, i, j, num):
  # check if the number is already present in the row
  for col in range(9):
    if grid[i][col] == num:
      return False

  # check if the number is already present in the column
  for row in range(9):
    if grid[row][j] == num:
      return False

  # check if the number is already present in the 3x3 grid
  start_row = i - i % 3
  start_col = j - j % 3
  for row in range(start_row, start_row + 3):
    for col in range(start_col, start_col + 3):
      if grid[row][col] == num:
        return False

  # the number is valid
  return True

# function to solve the Sudoku puzzle
def solve_sudoku(grid):
  # find the next empty cell
  empty_cell = find_next_empty_cell(grid)
  if empty_cell == None:
    # the grid is full, the puzzle is solved
    return True

  i, j = empty_cell

  # try each number from 1 to 9 in the empty cell
  for num in range(1, 10):
    if is_valid(grid, i, j, num):
      # the number is valid, so fill the cell with the number
      grid[i][j] = num

      # try to solve the rest of the puzzle
      if solve_sudoku(grid):
        # the puzzle is solved, so return the solved grid
        return True

      # the number is not valid, so backtrack
      grid[i][j] = 0

  # no number is valid in the current cell, so backtrack
  return False

# example Sudoku puzzle
grid = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
