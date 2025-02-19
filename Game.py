import pygame as game
from Square import Square

# Game class
class Game: 
    # Attributes
    
    # Constants
    WIDTH = 0
    HEIGHT = 0
    
    # Assets
    blank_image = None
    o_asset = None
    x_asset = None
    background = None
    
    # Window integrity elements
    window = None
    clock = None
    is_running = False
    
    square_group = game.sprite.Group()
    squares = []
    
    num = 0 # Gus: I think i'll name it better later
    
    #Constructor
    def __init__(self):
        game.init()
        
        # Load the assets
        self.blank_image = game.image.load('Blank.png')
        self.o_asset = game.image.load('o.png')
        self.x_asset = game.image.load('x.png')
        self.background = game.image.load('bg.png')
        
        # Set window dimensions
        self.WIDTH = 500
        self.HEIGHT = 500
        
        # Define window elements
        self.window = game.display.set_mode((self.WIDTH,self.HEIGHT))
        game.display.set_caption('Agent Tic-Tac-Toe by ChatGPI')
        self.clock = game.time.Clock()
        self.background = game.transform.scale(self.background,(self.WIDTH,self.HEIGHT))
        
        self.num = 1
        
        for y in range (1,4):
            for x in range(1,4):
                tempSquare = Square(x,y,self.num)
                self.square_group.add(tempSquare)
                self.squares.append(tempSquare)
        
        self.num += 1
        
    # Run game
    def run(self):
        self.is_running = True
        while isRunning:
            self.clock.tick(60)
            for event in game.event.get():
                if event.type == game.QUIT:
                    isRunning = False
        self.update()
    
    # Update states
    def update(self):
        self.window.blit(self.background, (0,0))
        self.square_group.draw(self.window)
        self.square_group.update()

        game.display.update()