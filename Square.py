import pygame as game

# Class Square, extends Sprite class from pygame library
class Square(game.sprite.Sprite):
    # Gus (Idea): Add a factor for dividing the square dimensions based on the size of the board
    
    # Constructor
    def __init__(self, x_id, y_id, number,image):
        super().__init__() # Call the father class constructor
        self.width = 240
        self.height = 240
        
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ' '
        self.number = number
        self.image = image
        self.image = game.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.center = (self.x, self.y)
        
    def clicked(self, x_val, y_val, turn, board, image):
        if self.content == ' ':
            if self.rect.collidepoint(x_val, y_val):
                self.content = turn
                board[self.number] = True
                
                if turn == 'x':
                    self.image = image
                    self.image = game.transform.scale(self.image, (self.width, self.height))
                    turn = 'o'
                
                if turn == 'o':
                    self.image = image
                    self.image = game.transform.scale(self.image, (self.width, self.height))
                    turn = 'x'
                
            
        

