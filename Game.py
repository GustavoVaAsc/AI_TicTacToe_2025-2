import pygame as game
from Square import Square
from Board import Board

# Game class
class Game: 
    # Attributes
    
    # Constants
    WIDTH = 0
    HEIGHT = 0
    
    # TODO: Change Asset name to UPPER CASE
    
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
    
    num = 0 # Gus: I think i'll name it better later
    #Constructor
    def __init__(self):
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
        self.clock = game.time.Clock()
        self.background = game.transform.scale(self.background,(self.WIDTH,self.HEIGHT))
        self.board = Board(3**2)
        
        self.num = 1
        
        for y in range (1,4):
            for x in range(1,4):
                tempSquare = Square(x,y,self.num,self.blank_image)
                self.board.square_group.add(tempSquare)
                self.board.squares.append(tempSquare)
                self.num += 1
        
    # Run game
    def run(self):
        self.is_running = True
        while self.is_running:
            self.clock.tick(60)
            for event in game.event.get():
                if event.type == game.QUIT:
                    self.is_running = False
                
                if event.type == game.MOUSEBUTTONDOWN and self.board.turn == 'o':
                    mx,my = game.mouse.get_pos()
                    for square in self.board.squares:
                        square.clicked(mx,my, self.board.turn,self.board,self.o_asset)        
            self.update()
        
    
    # Update states
    def update(self):
        self.window.blit(self.background, (0,0))
        self.board.square_group.draw(self.window)
        self.board.square_group.update()

        game.display.update()
        
        
    