# milestone 1: store the board state
import random
from turtle import width
def random_state(width:int, height:int) -> list[list]:
    """
    Creates a two dimensional array based on given width and height values.
    Each element of the array represents a cell in the board, randomly initialized 
    as either 1(alive) or 0(dead). Function returns the 2-d array as the board state
    of the game.

    """
    board_state = []
    for j in range(height):
        board_state.append([random.randint(0,1) for i in range(width)])
    return board_state


# milestone 2: pretty print to the terminal
def render(state):
    "uses green to represent live cells (value of 1) and red to represent dead cells (value of 1)"
    print("---"*len(state))
    for i in range(len(state)):
        row = ''
        for j in range(len(state[i])):
            if state[i][j] == 0:
                char = '🟥'
            else:
                char = '🟩'
            row += char
        print("|", row, "|")
    print("---"*len(state))
    
state = random_state(20, 20)
# render(state)

# milestone 3: next_board_state
def sum_neighbors(cell_i, board):
    i = cell_i[0]
    j = cell_i[1]
    neighbors = []
    neighbors.extend(board[i-1][j-1:j+2]) # first row of neighboring cells
    neighbors.extend(board[i+0][j-1:j+2]) # second, this includes active cell
    neighbors.extend(board[i+1][j-1:j+2]) # third
    del neighbors[4] # removes the active cell, which will always be the fifth element
    return sum(neighbors)

# print(sum_neighbors([1, 1], state))


def next_board_state(init_state):
    if len(init_state) * len(init_state[0]) < 9:
        raise Exception("length and height of initial stage is too small to compute")
    # first take a cell
    for i in range(1, len(init_state)-1):
        for j in range(1, len(init_state[i])-1):
            current_i = [i, j]
            live_neighbors = sum_neighbors(current_i, init_state)

            if live_neighbors <= 1:
                init_state[i][j] = 0
            elif live_neighbors <= 3:
                init_state[i][j] = 1
            else:
                init_state[i][j] = 0
    return init_state
render(state)             
board_state = next_board_state(state)
render(board_state)
    # get its next 8 neighbors 
    # sum their values
    # update the state of the cell based on the sum of neighbor values

