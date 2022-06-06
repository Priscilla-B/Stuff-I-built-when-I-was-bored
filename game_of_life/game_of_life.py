# milestone 1: store the board state
import random

def dead_state(width:int, height:int):
    """
    Creates a two dimensional array based on given width and height values.
    Each element of the array has a value of 0, to indicate a dead cell.
    """
    dead_board = []
    for i in range(height):
        dead_board.append([0]*width)
        # don't use a variable to store [0]*width before appending it to dead_board
        # if you do that, all the inner lists in the nested list will point to the 
        # same variable and will be stored at the same location
        # this will look okay here, but will affect your random_state function
        # as all the inner lists will have the same random state
    
    return dead_board

def random_state(width:int, height:int) -> list[list]:
    """
    Creates a two dimensional array based on given width and height values.
    Each element of the array represents a cell in the board, randomly initialized 
    as either 1(alive) or 0(dead). Function returns the 2-d array as the board state
    of the game.

    """
    board_state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            board_state[i][j] = random.randint(0,1) 
    return board_state


# milestone 2: pretty print to the terminal
def render(state):
    """
    Takes a given board state (state) and pretty prints the state to the terminal
    Uses a star(*) to represent live cells (value of 1) and space to represent dead cells (value of 1)
    """
    
    # print("- "*len(state[0]))
    print("")
    for i in range(len(state)):
        row = ''
        for j in range(len(state[i])):
            if state[i][j] == 0:
                char = ' '
            else:
                char = '*'
            row += char
        print("|", row, "|")
    # print("- "*len(state[0]))
    print("")
    



# milestone 3: next_board_state
def update_cell(cell_i, board):
    i = cell_i[0]
    j = cell_i[1]
    width = len(board[0])
    height = len(board)
    cell = board[i][j]
    live_neighbors = 0

    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x == i and y == j:
                continue

            if x >= height:
                x = i-x+1
            if y >= width:
                y = j-y+1
            # indexing needs to restart at zero at the above edge cases
                
            live_neighbors += board[x][y]
            
    print("cell", cell)
    print("live neighbors", live_neighbors)
            
    
    

    if cell == 0 and live_neighbors == 3:
        return 1
            # dead cell comes alive only if live_neigbors are exactly 3

    if cell == 1 and (live_neighbors == 2 or live_neighbors == 3):
            return 1
           # live cell only stays live when it has exactly 2 or 3 live_neighbors

           # since the all cells in the new state are already dead, there's no 
           # need to set cells that don't meet the above criteria dead again


    return 0



# def next_board_state(init_state):
#     if len(init_state) * len(init_state[0]) < 9:
#         raise Exception("length and height of initial stage is too small to compute")

#     new_state = dead_state(len(init_state[0]), len(init_state))

    
#     for i in range(len(init_state)):
#         for j in range(len(init_state[i])):
#             new_state[i][j] = update_cell([i, j], init_state)
#     return new_state
        
            
            
#     return new_state

if __name__ == "__main__":
    # makes sure this code runs only when I directly run it
    # and not when file is imported as a module
    state = random_state(10, 10)
    next_state = update_cell([9,9], state)

    # render(state)  
    # print("**************************************************")
    # render(next_state)
    print(state)
    print("***********************")
    print(next_state)

    



