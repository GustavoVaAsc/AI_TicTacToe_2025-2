from Game import *
import math
from EasyAgent import EasyAgent
from MediumAgent import MediumAgent
from MinimaxAgent import MinimaxAgent

class Board:
    # Board elements
    size = 9
    board = [' ' for _ in range(size+1)]
    
    # Flag to determine if there is a game over
    is_gameover = False
    
    # Squares to render as cells
    square_group = game.sprite.Group()
    squares = [] # List of squares
    
    # Game elements
    turn = 'o'
    winning_states = []
    winner = '-'
    move_count = 0
    agent = None
    difficulty = 0
    
    # Assets
    blank_image = None
    o_asset = None
    x_asset = None
    
    # Initializer class
    def __init__(self, size, difficulty):
        # Load and initialize all the values
        self.size = size
        self.comp_move = self.size // 2 
        self.winning_states = self.generateWinningStates()
        self.board = [' ' for _ in range(size+1)]
        self.blank_image = game.image.load('Blank.png')
        self.o_asset = game.image.load('o.png')
        self.x_asset = game.image.load('x.png')
        self.move_count = 0  # Initialize the move counter
        
        # Set AI difficulty
        self.difficulty = difficulty
        if difficulty == 1:
            self.agent = EasyAgent()
        elif difficulty == 2:
            self.agent = MediumAgent()
            # Generate positions where we could lose
            self.agent.generateDangerPositions(self)
        else:
            self.agent = MinimaxAgent(self)
    
    # Check if the agent can move
    def checkMove(self):
            self.agent.checkMove(self)

    # Generate all cases where there's a winning state
    def generateWinningStates(self):
        self.winning_states = []
        n = int(math.sqrt(self.size)) # Size of the grid

        # Rows
        for i in range(n):
            for j in range(n - 2):  # Ensure 3 consecutive cells
                row = [i * n + j + 1, i * n + j + 2, i * n + j + 3]
                if all(1 <= idx <= self.size for idx in row):  # Validate indices
                    self.winning_states.append(row)

        # Columns
        for i in range(n - 2):
            for j in range(n):
                col = [(i + k) * n + j + 1 for k in range(3)]
                if all(1 <= idx <= self.size for idx in col):
                    self.winning_states.append(col)

        # Diagonals
        for i in range(n - 2):
            for j in range(n - 2):
                # Main diagonal
                main_diag = [(i + k) * n + (j + k) + 1 for k in range(3)]
                if all(1 <= idx <= self.size for idx in main_diag):
                    self.winning_states.append(main_diag)

                # Anti-diagonal
                anti_diag = [(i + k) * n + (j + 2 - k) + 1 for k in range(3)]
                if all(1 <= idx <= self.size for idx in anti_diag):
                    self.winning_states.append(anti_diag)

        return self.winning_states

    # Check if we have a winner
    def checkForWin(self, player):
        if not self.winning_states:
            self.winning_states = self.generateWinningStates()  # Ensure winning states are generated
        
        max_index = self.size  # The last valid index (size represents all tiles)

        # Iterating all triplets of winning states
        for triplet in self.winning_states:
            if any(idx < 1 or idx > max_index for idx in triplet):  # Detect invalid indices
                continue  # Skip invalid triplets to prevent crashes

            a, b, c = triplet # Check the cells of the triplet
            if self.board[a] == player and self.board[b] == player and self.board[c] == player:
                self.is_gameover = True  # Set the game-over flag
                self.winner = player
                return  # No need to continue once a winner is found

        self.is_gameover = False  # Set the game-over flag to False if no winner

    # Check all the moves are done for determine a tie
    def checkForTie(self):
        if self.move_count == self.size:  # Check if all moves are made
            if not self.checkForWin('x') and not self.checkForWin('o'):
                self.is_gameover = True  # Set game over if no winner
                self.winner = '-'  # Indicate a tie
        else:
            self.is_gameover = False  # Game is still ongoing
