class UltimateTTT:
    def __init__(self):
        # creates an ultimate tic tac toe board initialized to all 0s
        # 'O' represents empty, 'x' represents X, 'y' represents 0 in the smaller gameboard
        # each individual board is an array with 10 indices with the first index representing if the smaller gameboard has been won or not by X or 0
        # [ ['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O'], ...]
        # returns an empty game board

    def print_board(self):
        # prints out the entire board

    def move(self, move):
        # takes in a move as an array of two integers
        # [smaller game index, smaller game move]
        # calculates if a smaller game board has been won
        # returns a board with the updated states
    
    def larger_game_board_state(self):
        #returns array of 9 of larger game board state indicating if subgames have been won
    
    def smaller_game_board_state(self, index):
        #returns array of smaller game board at given index
    
    def possible_moves(self, move):
        # returns all the next possible moves from the previous move
        # [[larger game index, smaller game index], [larger game index, smaller game index], [larger game index, smaller game index]...]
    


    

