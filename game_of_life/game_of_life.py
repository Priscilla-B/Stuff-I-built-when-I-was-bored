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
render(state)

# milestone 3: next_board_state

def next_board_state(init_state):
    if len(init_state) * len(init_state[0]) < 9:
        raise Exception("length and height of initial stage is too small to compute")
    # first take a cell
    for i in range(1, len(init_state)-1):
        for j in range(1, len(init_state[i])-1):
            current = init_state[i][j]
            # neighbors = 

    # get its next 8 neighbors 
    # sum their values
    # update the state of the cell based on the sum of neighbor values
    