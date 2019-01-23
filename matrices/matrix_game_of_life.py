# Welcome to the Game of Life!
#
# The Game of Life is a life simulation game, played on a 2-dimensional grid. Each cell of the grid can contain a living cell (represented by "o") or an empty cell (represented by " "). The grid starts with an initial state, and changes each day based on the following rules:
#
# 1. Any live cell with fewer than two live neighbors dies, as if caused by under population.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
# 4. Any empty cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#
# We're going to write some code related to this game in this interview.
#
# 1. Create a representation of the game and print it.
# 2. Run the simulation for one day and print the new state.

# | | | | | |
# | | |o|o|o|
# |o|o|o|o| |
# | | |o| |o|
# | | | | | | 


# write a function that takes in a grid and prints it 
def print_grid(grid):
    
    if not grid:
        return
    
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    for i in range(num_rows):
        new_row = ""
        for j in range(num_cols):
            new_row += "|" + grid[i][j]
        new_row += "|"
        print(new_row)


def run_simulation(grid):
    
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    new_grid = []
    
    
    for i in range(num_rows):
        new_grid.append([])
        for j in range(num_cols):
            num_live_neighbors = 0
            for mini_i in range(i-1, i+2):
                if mini_i >= 0 and mini_i < num_rows:
                    for mini_j in range(j-1, j+2):
                        if mini_j >= 0 and mini_j < num_cols:
                            if not (mini_i == i and mini_j == j):
                                if grid[mini_i][mini_j] == "o":
                                    num_live_neighbors += 1 

            # print("Neighbors: ", num_live_neighbors)
    
            if num_live_neighbors < 2 and grid[i][j] == "o":
                new_grid[i].append(" ")     
            elif (num_live_neighbors == 2 or num_live_neighbors == 3) and grid[i][j] == "o":
                new_grid[i].append("o")
            elif num_live_neighbors > 3 and grid[i][j] == "o":
                new_grid[i].append(" ")
            elif num_live_neighbors == 3 and grid[i][j] == " ":
                new_grid[i].append("o")
            else:
                new_grid[i].append(" ")
    
    return new_grid


           
# | | | | |*|_
# | | |o|o|o|_
# |o|o|o|o| |
# | | |o| |o|
# | | | | |o| 


# (1, 4) would also include (0, 0), (1, 0), and (2, 0) as neighbors
# if (x, last index)
# if (

grid = [" ", " ", " ", " ", " "], [" ", " ", "o", "o", "o"], ["o", "o", "o", "o", " "], [" ", " ", "o", " ", "o"], [" ", " ", " ", " ", " "]
# print(print_grid(grid))

# grid = [" ", " ", " ", " ", " "], [" ", " ", "o", " ", " "], [" ", " ", "o", " ", " "], [" ", " ", "o", " ", " "], [" ", " ", " ", " ", " "]

print_grid(grid)
print_grid(run_simulation(grid))
print_grid(run_simulation(run_simulation(grid)))

