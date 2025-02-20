from Game import *

class Board:
    size = 9
    board = [' ' for _ in range(size+1)]
    
    move = True
    compMove = 5
    
    square_group = game.sprite.Group()
    squares = []
    turn = 'o'
    
    # Assets
    blank_image = None
    o_asset = None
    x_asset = None
    
    def __init__(self, size):
        self.size = size
        self.compMove = self.size // 2 
        self.board = [' ' for _ in range(size+1)]
        self.blank_image = game.image.load('Blank.png')
        self.o_asset = game.image.load('o.png')
        self.x_asset = game.image.load('x.png')
        
    
    def checkMove(self):
        self.move = True
        self.checkCentre()

        if self.move:
            self.checkCorner()

        if self.move:
            self.checkEdge()

        if not self.move:
            for square in self.squares:
                if square.number == self.compMove:
                    square.clicked(square.x, square.y, self.turn, self, self.x_asset)
                    break  # Ensure only one move is made

            
    def checkCentre(self):
        centre_index = self.size // 2
        if self.board[centre_index] == ' ':
            self.compMove = centre_index
            self.move = False

    
            
    def checkCorner(self):
        corners = [1, 3, 7, 9]
        for corner in corners:
            if self.board[corner] == ' ':
                self.compMove = corner
                self.move = False
                break


                
    def checkEdge(self):
        for i in range(2,self.size+1,2):
            if self.board[i] == ' ':
                self.compMove = i
                self.move = False
                break