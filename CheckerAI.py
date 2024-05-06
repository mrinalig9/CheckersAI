from Transition import BoardTransition
from CheckerGame import CheckerBoard
import numpy as np
from constants import Q_TABLE_FILE
#import tensorflow as tf

class CheckerAI:
    def __init__(self) -> None:
        self.boardTransition = BoardTransition()
        try:
            self.qTable = np.load(Q_TABLE_FILE, allow_pickle="TRUE").item()
        except:
            print("No Q Table exists")
            self.qTable = dict()
            np.save(Q_TABLE_FILE, self.qTable)

    # Utility function
    # Takes a board state evaluates it
    # Higher evaluation for kings
    def evaluateBoard(self, board:CheckerBoard) -> int:
        # AI Teams works on this
        # pass
        if board.turn == 1: 
            return board.player1NumPieces - board.player2NumPieces + board.player1NumKings - board.player2NumKings
        else: 
            return board.player2NumPieces - board.player1NumPieces + board.player2NumKings - board.player1NumKings
   
    
    # current_state (board) - current state of the game board
    # depth (int) - how deep in the minimax tree to go
    # is_max (boolean) - True for max level, False for min level
    # alpha (int) - current alpha value of tree
    # beta (int) - current beta value of tree
    # uses a get_children() function that should be made in transition
    def minimax(self, current_state, depth, is_max, alpha, beta): 
        # no move will be made
        possible_moves = self.boardTransition.getAllBoards(possible_moves)
        if depth == 0 or len(possible_moves) == 0:
            return self.evaluateBoard(current_state), current_state
        
        max_val = float('-inf')
        min_val = float('inf')
        next_move = None
        if is_max: 
            for move in possible_moves: 
                value, path = self.minimax(self, move, depth - 1, False)
                alpha = max(alpha, value)
                if value > max_val: 
                    max_val = value
                    next_move = move
                if value >= beta:
                    break
            return max_val, next_move
        else: 
            for move in possible_moves: 
                value, path = self.minimax(self, move, depth - 1, True)
                beta = min(beta, value)
                if value < min_val: 
                    min_val = value
                    next_move = move
                if value <= alpha:
                    break
            return min_val, next_move
        
    def get_path(self) -> list["CheckerBoard"]:
        path = []
        current_node = self
        while current_node:
            path.append(current_node)
            current_node = current_node.parent
        return path[::-1]
    
    # Saves q table inside binary file
    def __del__(self):
        np.save(Q_TABLE_FILE, self.qTable)