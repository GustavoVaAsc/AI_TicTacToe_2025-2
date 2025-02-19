import pygame as game

# Class Square, extends Sprite class from pygame library
class Square(game.sprite.Sprite):
    
    # Constructor
    def __init__(self, x_id, y_id, number,image):
        super.__init__() # Call the father class constructor
        self.width = 120 
        self.height = 120
        
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ' '
        self.number = number
        self.image = image
        self.image = game.transform.scale(self.image, self.width, self.height)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.center = (self.x, self.y)

