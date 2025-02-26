import pygame as game
from Square import Square
from Board import Board

# Game class
class Game: 
    # Attributes
    
    # Constants
    WIDTH = 0
    HEIGHT = 0
    
    blank_image = None
    o_asset = None
    
    # Background
    background = None
    
    # Window integrity elements
    window = None
    clock = None
    is_running = False
    
    # Board
    board = None
    
    num = 0 # 
    # Initializer
    def __init__(self, difficulty, board_size):
        game.init()
        
        # Load the background
        self.blank_image = game.image.load('Blank.png')
        self.o_asset = game.image.load('o.png')
        self.background = game.image.load('bg.png')
        
        # Set window dimensions
        self.WIDTH = 1000
        self.HEIGHT = 1000
        
        # Define window elements
        self.window = game.display.set_mode((self.WIDTH,self.HEIGHT))
        game.display.set_caption('Tic-Tac-Toe by ChatGPI')
        self.clock = game.time.Clock() # Init the clock
        # Set background
        self.background = game.transform.scale(self.background,(self.WIDTH,self.HEIGHT))
        # Initialize our game board
        self.board = Board(board_size**2,difficulty)
        
        self.num = 1
        
        # Insert the rectangles to render on screen
        for y in range (1,board_size+1):
            for x in range(1,board_size+1):
                tempSquare = Square(x,y,self.num,self.blank_image,board_size)
                self.board.square_group.add(tempSquare)
                self.board.squares.append(tempSquare)
                self.num += 1
        
    # Run game
    def run(self):
        self.is_running = True
        
        # Game loop
        while self.is_running:
            self.clock.tick(60) # Update rate
            for event in game.event.get(): # Check game events
                # Check for quit
                if event.type == game.QUIT:
                    self.is_running = False
                
                # Check if the player is trying to move
                if event.type == game.MOUSEBUTTONDOWN and self.board.turn == 'o':
                    mx,my = game.mouse.get_pos()
                    for square in self.board.squares:
                        # Mark as clicked
                        square.clicked(mx,my, self.board.turn,self.board,self.o_asset)
            # Update the game        
            self.update()
        
    
    # Update states
    def update(self):
        # Rendering window elements
        self.window.blit(self.background, (0,0))
        # Draw squares on the screen
        self.board.square_group.draw(self.window)
        self.board.square_group.update()

        # Check if the game is over
        if self.board.is_gameover:
            self.board.square_group.empty() # Empty the square group
            # Show the winner on screen
            self.background = game.image.load(self.board.winner.upper()+"wins.jpg")
            self.background = game.transform.scale(self.background, (self.WIDTH,self.HEIGHT))
        # Update
        game.display.update()
        
    
    