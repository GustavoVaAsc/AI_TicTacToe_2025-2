from Game import *
import math

class Board:
    size = 9
    board = [' ' for _ in range(size+1)]
    
    move = True
    comp_move = 5
    is_gameover = False
    
    square_group = game.sprite.Group()
    squares = []
    turn = 'o'
    winning_states = []
    winner = '-'
    move_count = 0
    
    # Assets
    blank_image = None
    o_asset = None
    x_asset = None
    
    def __init__(self, size):
        self.size = size
        self.comp_move = self.size // 2 
        self.winning_states = self.generateWinningStates()
        self.board = [' ' for _ in range(size+1)]
        self.blank_image = game.image.load('Blank.png')
        self.o_asset = game.image.load('o.png')
        self.x_asset = game.image.load('x.png')
        self.move_count = 0  # Initialize the move counter
        
    def checkMove(self):
        self.move = True
        
        if self.move:
            self.checkForWin('o')
            
        if self.move:
            self.checkForWin('x')
        
        if not self.is_gameover:  # Only check for tie if the game isn't over
            self.checkForTie()
        
        self.checkCentre()

        if self.move:
            self.checkCorner()

        if self.move:
            self.checkEdge()

        if not self.move:
            for square in self.squares:
                if square.number == self.comp_move:
                    square.clicked(square.x, square.y, self.turn, self, self.x_asset)
                    break  # Ensure only one move is made

    def checkCentre(self):
        centre_index = self.size // 2
        if self.board[centre_index] == ' ':
            self.comp_move = centre_index
            self.move = False
            
    def checkCorner(self):
        # TODO: Generalize it for n x n grid
        corners = [1, 3, 7, 9]
        for corner in corners:
            if self.board[corner] == ' ':
                self.comp_move = corner
                self.move = False
                break
                
    def checkEdge(self):
        for i in range(2,self.size+1,2):
            if self.board[i] == ' ':
                self.comp_move = i
                self.move = False
                break

    def generateWinningStates(self):
        self.winning_states = []
        n = int(math.sqrt(self.size))  # Grid dimension

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

        print("Valid Winning States:", self.winning_states)  # Debugging output
        return self.winning_states


    
    def whoWins(self,player):
        for triplet in self.winning_states:
            a, b, c = triplet
            if (
                self.board[a] == player and self.board[b] == player and self.board[c] == ' '
            ):
                self.comp_move = c
                self.move = False
                return
            elif (
                self.board[a] == player and self.board[b] == ' ' and self.board[c] == player
            ):
                self.comp_move = b
                self.move = False
                return
            elif (
                self.board[a] == ' ' and self.board[b] == player and self.board[c] == player
            ):
                self.comp_move = a
                self.move = False
                return
    
    def checkForWin(self, player):
        if not self.winning_states:
            print("Warning: winning states are not initialized!")
            self.winning_states = self.generateWinningStates()  # Ensure winning states are generated
        
        max_index = self.size  # The last valid index (size represents all tiles)

        for triplet in self.winning_states:
            if any(idx < 1 or idx > max_index for idx in triplet):  # Detect invalid indices
                print(f"Invalid triplet detected: {triplet}")  # Debugging output
                continue  # Skip invalid triplets to prevent crashes

            a, b, c = triplet
            if self.board[a] == player and self.board[b] == player and self.board[c] == player:
                self.is_gameover = True  # Set the game-over flag
                self.winner = player
                return  # No need to continue once a winner is found

        self.is_gameover = False  # Set the game-over flag to False if no winner


    def checkForTie(self):
        if self.move_count == self.size:  # Check if all moves are made
            if not self.checkForWin('x') and not self.checkForWin('o'):
                self.is_gameover = True  # Set game over if no winner
                self.winner = '-'  # Indicate a tie
        else:
            self.is_gameover = False  # Game is still ongoing
