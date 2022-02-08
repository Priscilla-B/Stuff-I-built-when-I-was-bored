# milestone 1: store the board state
import random
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
    



# milestone 3: next_board_state
def sum_neighbors(cell_i, board):
    i = cell_i[0]
    j = cell_i[1]
    n_i = len(board)- 1
    n_j = len(board[0]) - 1
    neighbors = []

    # for corner cells
    if cell_i == [0, 0] or cell_i == [0, n_j] or cell_i == [n_i, 0] or cell_i == [n_i, n_j]:
        return -1

    # for edge cells

    if i == 0:
        neighbors.extend(board[i+n_i][j-1:j+2])
        neighbors.extend(board[i+0][j-1:j+2])
        neighbors.extend(board[i+1][j-1:j+2])
        
    elif i == n_i:
        neighbors.extend(board[i+-1][j-1:j+2])
        neighbors.extend(board[i+0][j-1:j+2])
        neighbors.extend(board[i-n_i][j-1:j+2])
    
    elif j == 0:
        neighbors.append(board[i-1][n_j])
        neighbors.extend(board[i-1][j:j+2])
        neighbors.append(board[i+0][n_j])
        neighbors.extend(board[i+0][j:j+2])
        neighbors.append(board[i+1][n_j])
        neighbors.extend(board[i+1][j-1:j+2])

    elif j == n_j:
        neighbors.extend(board[i-1][j-1:j+1])
        neighbors.append(board[i-1][n_j-n_j])
        neighbors.extend(board[i+0][j-1:j+1])
        neighbors.append(board[i+0][n_j-n_j])
        neighbors.extend(board[i+1][j-1:j+1])
        neighbors.append(board[i+1][n_j-n_j])

    # for all other cells
    else:
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
    for i in range(len(init_state)):
        for j in range(len(init_state[i])):
            live_neighbors = sum_neighbors([i, j], init_state)

            if live_neighbors < 0:
                init_state[i][j] =  init_state[i][j] #init state remains unchanged for corner cells
            elif live_neighbors <= 1:
                init_state[i][j] = 0
            elif live_neighbors <= 3:
                init_state[i][j] = 1
            else:
                init_state[i][j] = 0
    return init_state

state = random_state(20, 20)
render(state)  
print("****************************************************")           
board_state = next_board_state(state)
render(board_state)
# print(state)
    

