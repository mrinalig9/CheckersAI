from Transition import BoardTransition
from CheckerGame import CheckerBoard

class CheckerAI:
    def __init__(self) -> None:
        # This will be implemented later on to import node weights for utility funciton
        pass

    # Utility function
    # Takes a board state evaluates it
    # Higher evaluation for kings
    def evaluateBoard(self, board:CheckerBoard, player) -> int:
        # AI Teams works on this
        # pass
        if player == 1: 
            return self.player1NumPieces - self.player2NumPieces + self.player1NumKings - self.player2NumKings
        else: 
            return self.player2NumPieces - self.player1NumPieces + self.player2NumKings - self.player1NumKings
   
    
    # current_state (board) - current state of the game board
    # depth (int) - how deep in the minimax tree to go
    # is_max (boolean) - True for max level, False for min level
    # uses a get_children() function that should be made in transition
    def minimax(self, current_state, depth, is_max): 
        # no move will be made
        if depth == 0:
            return current_state
        
        max_val = float('-inf')
        min_val = float('inf')
        next_move = None
        possible_moves = []
        if is_max: 
            # possible_moves = get_children(current_state, color)
            for move in possible_moves: 
                value, path = minimax(self, move, depth - 1, False)
                if value > max_val: 
                    max_val = value
                    next_move = move
            return max_val, next_move
        else: 
            # possible_moves = get_children(current_state, color)
            for move in possible_moves: 
                value, path = minimax(self, move, depth - 1, True)
                if value < min_val: 
                    min_val = value
                    next_move = move
            return min_val, next_move
